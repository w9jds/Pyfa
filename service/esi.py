from esipy import App
from esipy import EsiClient
import eos.db
from eos.db.saveddata.databaseRepair import DatabaseCleanup
from logbook import Logger
from itertools import chain

pyfalog = Logger(__name__)


class esiConnection(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiConnection()

        return cls.instance

    def __init__(self):
        self.esi_app = App.create('https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility')
        self.esi_client = EsiClient(
            headers={"User-Agent": "pyfa.fit_<3_snowedin"},
            retry_requests=True
        )

        gamedata_engine = eos.db.gamedata_engine
        self.gamedata_connection = gamedata_engine.connect()


class esiMarket(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiMarket()

        return cls.instance

    def __init__(self):
        self.sESIConnection = esiConnection.getInstance()
        self.sESIHelpers = esiHelpers.getInstance()

    def fetchEsiMarketID(self):
        pyfalog.info("Fetching market group list from ESI")
        esi_request = self.sESIConnection.esi_app.op['get_markets_groups']()
        esi_market_groups = self.sESIConnection.esi_client.request(esi_request).data

        pyfalog.info("Fetching market group items from ESI")
        esi_market_group_types = self.sESIConnection.esi_client.multi_request(
                [self.sESIConnection.esi_app.op["get_markets_groups_market_group_id"](market_group_id=x) for x in esi_market_groups],
                threads=50,
        )

        self.deleteOldMarketGroups(esi_market_groups)
        self.cleanMarketGroups(esi_market_group_types)

        esi_market_group_types_list = [x.data for x in [x[1] for x in esi_market_group_types]]

        return esi_market_groups, esi_market_group_types_list

    def deleteOldMarketGroups(self, esi_market_groups):
        pyfalog.info("Removing all invalid market groups")
        query_list = ""
        for market_group in esi_market_groups:
            query_list = self.sESIHelpers.addQueryList(query_list, market_group)
        update_query = "DELETE FROM invmarketgroups WHERE marketGroupID NOT IN ({0})".format(query_list)
        DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, update_query)

    def cleanMarketGroups(self, esi_market_group_types):
        pyfalog.info("Updating and cleaning market groups")
        for esi_market_group in esi_market_group_types:
            esi_market_group_data = esi_market_group[1].data

            esi_market_group_id = self.sESIHelpers.getAttribute(esi_market_group_data, "market_group_id")
            if esi_market_group_id is None:
                continue

            pyfalog.debug("Updating market group {0}.", esi_market_group_id)

            esi_market_group_name = self.sESIHelpers.getAttribute(esi_market_group_data, "name")
            if esi_market_group_name is None:
                esi_market_group_name = ""

            esi_market_group_description = self.sESIHelpers.getAttribute(esi_market_group_data, "description")
            if esi_market_group_description is None:
                esi_market_group_description = ""

            esi_market_group_parent_group_id = self.sESIHelpers.getAttribute(esi_market_group_data, "parent_group_id")
            if esi_market_group_parent_group_id is None:
                esi_market_group_parent_group_id = "Null"

            query = "SELECT * FROM invmarketgroups WHERE marketGroupID = '{0}'".format(esi_market_group_id)
            results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            row = results.first()

            if row is None:
                query = "INSERT INTO invmarketgroups (marketGroupID, marketGroupName, description, parentGroupID) VALUES ({0}, {1}, {2}, {3})".format(
                    esi_market_group_id,
                    esi_market_group_name,
                    esi_market_group_description,
                    esi_market_group_parent_group_id,
                )
                DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            else:
                query = "UPDATE invmarketgroups SET marketGroupName = '{1}', description = '{2}', parentGroupID ='{3}' WHERE marketGroupID = '{0}'".format(
                    esi_market_group_id,
                    esi_market_group_name,
                    esi_market_group_description,
                    esi_market_group_parent_group_id,
                )
                DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)

        return


class esiItems(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiItems()

        return cls.instance

    def __init__(self):
        self.sesiMarket = esiMarket.getInstance()
        self.sESIConnection = esiConnection.getInstance()
        self.sESIHelpers = esiHelpers.getInstance()

    def cleanMarketGroupsFromTypes(self, market_groups):
        pyfalog.info("Removing all invalid market IDs")
        query_list = ""
        for market_group in market_groups:
            query_list = self.sESIHelpers.addQueryList(query_list, market_group)
        update_query = "UPDATE invtypes SET marketGroupID = NULL WHERE marketGroupID NOT IN ({0})".format(query_list)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, update_query)
        pyfalog.info("Removed incorrect Market Group ID from {0} items.", query_results.rowcount)

    def updateTypesMarketGroup(self, market_list):
        pyfalog.info("Updating items market group.")
        for market_group in market_list:
            if market_group['types'].__len__() > 0:
                query_list = ""
                for market_group_type in market_group['types']:
                    query_list = self.sESIHelpers.addQueryList(query_list, market_group_type)
                update_query = "UPDATE invtypes SET marketGroupID = '{0}' WHERE typeID in ({1})".format(market_group['market_group_id'], query_list)
                query_results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, update_query)
                pyfalog.debug("Added Market Group ID ({0}) to {1} items.", market_group['market_group_id'], query_results.rowcount)

    def fetchEsiTypes(self):
        esi_types_list = []
        pyfalog.info("Fetching type_id list from ESI")
        for _ in range(5000):
            esi_universe_types_op = self.sESIConnection.esi_app.op['get_universe_types'](
                page=(_ + 1),
            )
            esi_universe_types = self.sESIConnection.esi_client.request(esi_universe_types_op)
            if esi_universe_types.data.__len__() == 0:
                break

            esi_types_list.extend(esi_universe_types.data)

        return esi_types_list

    def updateTypes(self):
        """
        Main loop.
        """
        pyfalog.info("Started updating items.")

        trans = self.sESIConnection.gamedata_connection.begin()
        setting_to_use_all_items = False

        esi_type_list = self.fetchEsiTypes()

        esi_market_groups, esi_market_group_types_list = self.sesiMarket.fetchEsiMarketID()

        self.cleanMarketGroupsFromTypes(esi_market_groups)

        esi_market_type_list = [i for i in chain.from_iterable([x['types'] for x in esi_market_group_types_list])]

        if not setting_to_use_all_items:
            esi_type_list = esi_market_type_list

        self.clean_types(esi_type_list, esi_market_type_list)

        self.updateTypesData(esi_type_list)

        self.updateTypesMarketGroup(esi_market_group_types_list)
        trans.commit()
        DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, "VACUUM")
        pyfalog.info("Completed updating items.")

    def updateTypesData(self, esi_type_list):
        pyfalog.info("Fetching types from ESI.")
        esi_universe_types_type_list = self.sESIConnection.esi_client.multi_request(
                [self.sESIConnection.esi_app.op["get_universe_types_type_id"](type_id=x) for x in esi_type_list],
                threads=50,
        )

        esi_universe_types_type_list = [x[1].data for x in esi_universe_types_type_list]

        esi_types_with_dogma_attributes_list = [x.type_id for x in esi_universe_types_type_list if hasattr(x, 'dogma_attributes')]
        esi_types_with_dogma_effects_list = [x.type_id for x in esi_universe_types_type_list if hasattr(x, 'dogma_effects')]
        self.clean_types_dogma(esi_types_with_dogma_attributes_list, esi_types_with_dogma_effects_list)

        pyfalog.info("Updating database with items.")
        for esi_item in esi_universe_types_type_list:

            if esi_item:
                try:
                    esi_item_published = getattr(esi_item, "published", False)
                    esi_item_name = getattr(esi_item, "name", None)
                    esi_item_id = getattr(esi_item, "type_id", None)
                except AttributeError:
                    # Missing name, ID, or not published, skip.
                    esi_item_published = False
                    esi_item_name = None
                    esi_item_id = None
                    continue

                if not esi_item_id or not esi_item_name:
                    # Missing name, ID, or not published, skip.
                    continue

                pyfalog.debug("Updating item {0}", esi_item_id)

                setting_to_allow_published = True
                if (setting_to_allow_published is True and esi_item_published is True) or setting_to_allow_published is False:
                    self.process_invItems(esi_item_id, esi_item)

                esi_item_attributes = self.sESIHelpers.getAttribute(esi_item, "dogma_attributes")
                esi_item_effects = self.sESIHelpers.getAttribute(esi_item, "dogma_effects")

                self.clean_item_dogma(esi_item_id, esi_item_attributes, esi_item_effects)

                if esi_item_attributes:
                    count_insert = 0
                    count_update = 0
                    for esi_attribute in esi_item_attributes:
                        query = "SELECT * FROM dgmtypeattribs WHERE typeID = '{0}' and attributeID = '{1}'".format(esi_item_id, esi_attribute['attribute_id'])
                        results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
                        row = results.first()

                        if row is None:
                            query = "INSERT INTO dgmtypeattribs (typeID, attributeID, value) VALUES ({0}, {1}, {2})".format(
                                esi_item_id,
                                esi_attribute['attribute_id'],
                                esi_attribute['value']
                            )
                            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
                            count_insert += 1
                        else:
                            query = "UPDATE dgmtypeattribs SET value = '{0}' WHERE typeID = '{1}' and attributeID = '{2}'".format(
                                esi_attribute['value'],
                                esi_item_id,
                                esi_attribute['attribute_id']
                            )
                            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
                            count_update += 1
                    pyfalog.debug("For TypeID ({0}) updated {1} and added {2} attributes.", esi_item_id, count_update, count_insert)

                if esi_item_effects:
                    count_insert = 0
                    for esi_effect in esi_item_effects:
                        query = "SELECT * FROM dgmtypeeffects WHERE typeID = '{0}' and effectID = '{1}'".format(esi_item_id, esi_effect['effect_id'])
                        results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
                        row = results.first()

                        if row is None:
                            query = "INSERT INTO dgmtypeeffects (typeID, effectID) VALUES ({0}, {1})".format(esi_item_id, esi_effect['effect_id'])
                            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
                            count_insert += 1
                    pyfalog.debug("For TypeID ({0}) added {1} effects.", esi_item_id, count_insert)

    def process_invItems(self, esi_type_id, esi_item):
        capacity = self.sESIHelpers.getAttribute(esi_item, "capacity")
        if capacity is None:
            capacity = ""

        description = self.sESIHelpers.getAttribute(esi_item, "description")
        if description is None:
            description = ""

        groupID = self.sESIHelpers.getAttribute(esi_item, "group_id")
        if groupID is None:
            groupID = ""

        iconID = self.sESIHelpers.getAttribute(esi_item, "icon_id")
        if iconID is None:
            iconID = ""

        mass = self.sESIHelpers.getAttribute(esi_item, "mass")
        if mass is None:
            mass = ""

        published = self.sESIHelpers.getAttribute(esi_item, "published")
        if published is None:
            published = ""

        typeName = self.sESIHelpers.getAttribute(esi_item, "name")
        if typeName is None:
            typeName = ""

        volume = self.sESIHelpers.getAttribute(esi_item, "volume")
        if volume is None:
            volume = ""

        columns = {
            'capacity'   : capacity,
            'description': description,
            # 'factionID': None,
            'groupID'    : groupID,
            'iconID'     : iconID,
            # 'marketGroupID': None,
            'mass'       : mass,
            'published'  : published,
            # 'raceID': raceID,
            'typeName'   : typeName,
            'volume'     : volume,
        }

        identifier = "typeID = '{0}'".format(esi_type_id)
        self.sESIHelpers.addRecord("dgmattribs", identifier, columns)

    def clean_types(self, esi_types, esi_market_types):
        pyfalog.debug("Purging items that don't exist, and cleaning market groups.")

        update_query = ""
        for type in esi_types:
            update_query = self.sESIHelpers.addQueryList(update_query, type)

        update_market_query = ""
        for type in esi_market_types:
            update_market_query = self.sESIHelpers.addQueryList(update_market_query, type)

        query = "DELETE FROM invTypes WHERE typeID NOT IN ({0})".format(update_query)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
        pyfalog.debug("Deleted {0} records out of invTypes", query_results.rowcount)

        query = "UPDATE invTypes SET marketGroupID = NULL WHERE typeID NOT IN ({0})".format(update_market_query)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
        pyfalog.debug("Set {0} records in invTypes to market group of null.", query_results.rowcount)

    def clean_types_dogma(self, dogma_attributes_list, dogma_effects_list):
        pyfalog.debug("Purging dogma attributes and effects from items that don't exist.")
        if dogma_attributes_list:
            update_query_list = ""
            for dogma_attribute in dogma_attributes_list:
                update_query_list = self.sESIHelpers.addQueryList(update_query_list, dogma_attribute)

            query = "DELETE FROM dgmtypeattribs WHERE typeID NOT IN ({0})".format(update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            pyfalog.debug("Cleaned obsolete records from dgmtypeattribs.")

        if dogma_effects_list:
            update_query_list = ""
            for dogma_effect in dogma_effects_list:
                update_query_list = self.sESIHelpers.addQueryList(update_query_list, dogma_effect)

            query = "DELETE FROM dgmtypeeffects WHERE typeID NOT IN ({0})".format(update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            pyfalog.debug("vrecords from dgmtypeeffects.")

    def clean_item_dogma(self, esi_item_id, esi_item_attributes, esi_item_effects):
        pyfalog.debug("Cleaning dogma attributes and effects from items.")
        if esi_item_attributes and esi_item_id:
            esi_item_attributes_list = [x['attribute_id'] for x in esi_item_attributes]
            update_query_list = ""
            for dogma_attribute in esi_item_attributes_list:
                update_query_list = self.sESIHelpers.addQueryList(update_query_list, dogma_attribute)

            query = "DELETE FROM dgmtypeattribs WHERE typeID = '{0}' AND attributeID NOT IN ({1})".format(esi_item_id, update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            pyfalog.debug("Deleted records from dgmtypeattribs for item ({0}).", esi_item_id)

        if esi_item_effects and esi_item_id:
            esi_item_effects_list = [x['effect_id'] for x in esi_item_effects]
            update_query_list = ""
            for dogma_effect in esi_item_effects_list:
                update_query_list = self.sESIHelpers.addQueryList(update_query_list, dogma_effect)

            query = "DELETE FROM dgmtypeeffects WHERE typeID = '{0}' AND effectID NOT IN ({1})".format(esi_item_id, update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            pyfalog.debug("Deleted records from dgmtypeeffects for item ({0}).", esi_item_id)


class esiDogma(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiDogma()

        return cls.instance

    def __init__(self):
        self.sESIConnection = esiConnection.getInstance()
        self.sESIHelpers = esiHelpers.getInstance()

    def updateAllDogmaTables(self):
        trans = self.sESIConnection.gamedata_connection.begin()

        self.updateDogmaAttributes()
        self.updateDogmaEffects()

        trans.commit()

    def updateDogmaAttributes(self):
        dogma_attribute_list = self.getDogmaAttributeIDs()
        dogma_attribute_data = self.getDogmaAttributeData(dogma_attribute_list)

        self.deleteBadDogmaAttributes(dogma_attribute_list)
        self.updateDogmaAttributeData(dogma_attribute_data)

    def getDogmaAttributeIDs(self):
        pyfalog.info("Fetching dogma attribute list from ESI")
        esi_request = self.sESIConnection.esi_app.op['get_dogma_attributes']()
        esi_return = self.sESIConnection.esi_client.request(esi_request).data

        return esi_return

    def getDogmaAttributeData(self, dogma_attribute_list):
        pyfalog.info("Fetching dogma attribute data from ESI")
        dogma_return = self.sESIConnection.esi_client.multi_request(
                [self.sESIConnection.esi_app.op["get_dogma_attributes_attribute_id"](attribute_id=x) for x in dogma_attribute_list],
                threads=50,
        )
        return [x[1].data for x in dogma_return]

    def deleteBadDogmaAttributes(self, dogma_attribute_list):
        pyfalog.info("Purging dogma attributes that don't exist.")

        update_query = ""
        for _ in dogma_attribute_list:
            update_query = self.sESIHelpers.addQueryList(update_query, _)

        self.sESIHelpers.deleteBadRecords("dgmattribs", "attributeID", update_query)

    def updateDogmaAttributeData(self, dogma_attribute_data):
        for dogma_attribute in dogma_attribute_data:
            attributeID = self.sESIHelpers.getAttribute(dogma_attribute, "attribute_id")
            if attributeID is None:
                continue

            attributeName = self.sESIHelpers.getAttribute(dogma_attribute, "name")
            if attributeName is None:
                attributeName = ""

            defaultValue = self.sESIHelpers.getAttribute(dogma_attribute, "default_value")
            if defaultValue is None:
                defaultValue = ""

            description = self.sESIHelpers.getAttribute(dogma_attribute, "description")
            if description is None:
                description = ""

            published = self.sESIHelpers.getAttribute(dogma_attribute, "published")
            if published is None:
                published = ""

            displayName = self.sESIHelpers.getAttribute(dogma_attribute, "display_name")
            if displayName is None:
                displayName = ""

            highIsGood = self.sESIHelpers.getAttribute(dogma_attribute, "high_is_good")
            if highIsGood is None:
                highIsGood = ""

            columns = {
                # 'attributeID': attributeID,
                'attributeName': attributeName,
                'defaultValue' : defaultValue,
                # 'maxAttributeID': None,
                'description'  : description,
                'published'    : published,
                'displayName'  : displayName,
                'highIsGood'   : highIsGood,
                # 'iconID': None,
                # 'unitID': None,
            }

            identifier = "attributeID = '{0}'".format(attributeID)
            self.sESIHelpers.addRecord("dgmattribs", identifier, columns)

    def updateDogmaEffects(self):
        dogma_effect_list = self.getDogmaEffectIDs()
        dogma_effect_data = self.getDogmaEffectData(dogma_effect_list)

        self.deleteBadDogmaEffects(dogma_effect_list)
        self.updateDogmaEffectData(dogma_effect_data)

    def getDogmaEffectIDs(self):
        pyfalog.info("Fetching dogma effect list from ESI")
        esi_request = self.sESIConnection.esi_app.op['get_dogma_effects']()
        esi_return = self.sESIConnection.esi_client.request(esi_request).data

        return esi_return

    def getDogmaEffectData(self, dogma_effect_list):
        pyfalog.info("Fetching dogma effect data from ESI")
        dogma_return = self.sESIConnection.esi_client.multi_request(
                [self.sESIConnection.esi_app.op["get_dogma_effects_effect_id"](effect_id=x) for x in dogma_effect_list],
                threads=50,
        )
        return [x[1].data for x in dogma_return]

    def deleteBadDogmaEffects(self, dogma_effect_list):
        pyfalog.info("Purging dogma effects that don't exist.")

        update_query = ""
        for _ in dogma_effect_list:
            update_query = self.sESIHelpers.addQueryList(update_query, _)

        self.sESIHelpers.deleteBadRecords("dgmeffects", "effectID", update_query)

    def updateDogmaEffectData(self, dogma_effect_data):
        for dogma_effect in dogma_effect_data:
            effectID = self.sESIHelpers.getAttribute(dogma_effect, "effect_id")
            if effectID is None:
                continue

            effectName = self.sESIHelpers.getAttribute(dogma_effect, "name")
            if effectName is None:
                effectName = ""

            description = self.sESIHelpers.getAttribute(dogma_effect, "description")
            if description is None:
                description = ""

            published = self.sESIHelpers.getAttribute(dogma_effect, "published")
            if published is None:
                published = ""

            isAssistance = self.sESIHelpers.getAttribute(dogma_effect, "is_assistance")
            if isAssistance is None:
                isAssistance = ""

            isOffensive = self.sESIHelpers.getAttribute(dogma_effect, "is_offensive")
            if isOffensive is None:
                isOffensive = ""

            # TODO: There are a lot more attributes we aren't getting here. :(

            columns = {
                # 'effectID': effectID,
                'effectName'  : effectName,
                'description' : description,
                'published'   : published,
                'isAssistance': isAssistance,
                'isOffensive' : isOffensive,
            }

            identifier = "effectID = '{0}'".format(effectID)
            self.sESIHelpers.addRecord("dgmeffects", identifier, columns)


class esiHelpers(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiHelpers()

        return cls.instance

    def __init__(self):
        self.sESIConnection = esiConnection.getInstance()

    @staticmethod
    def getAttribute(source, attribute, default=None):
        # We roll our own attribute getter because we need to handle special butterflies
        try:
            value = getattr(source, attribute, default)

            if attribute in ('published', 'high_is_good', 'is_assistance', 'is_offensive'):
                # SQLite doesn't understand true/false, so set to 1/0
                if value == "True" or value is True:
                    value = 1
                elif value == "False" or value is False:
                    value = 0
                else:
                    # Unexpected value, so set to 0
                    value = 0

            value = str(value).replace("'", "''")

            if value is None:
                return default
            else:
                return value

        except (AttributeError, KeyError):
            return default

    def deleteBadRecords(self, table, attribute, value_list):
        query = "DELETE FROM {0} WHERE {1} NOT IN ({2})".format(table, attribute, value_list)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
        pyfalog.info("Deleted {0} records from {1}.", query_results.rowcount, table)

    def addRecord(self, table, identifier, columns):
        """
        :param table:
        Name of the table

        :param identifier:
        the query used to identify the record
        Example: attributeID = '1'

        :param columns:
        A named dict with column names and values.
        Example:
            columns = {
                # 'attributeID': attributeID,
                'attributeName': attributeName,
                'defaultValue': defaultValue,
                # 'maxAttributeID': None,
                'description': description,
                'published': published,
                'displayName': displayName,
                'highIsGood': highIsGood,
                # 'iconID': None,
                # 'unitID': None,
            }

        :return:
        Returns nothing.
        """

        query = "SELECT * FROM {0} WHERE {1}".format(table, identifier)
        results = DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
        row = results.first()

        if row is None:
            query_columns = ""
            query_values = ""
            for column in columns:
                query_columns = self.addQueryList(query_columns, column, True)
                query_values = self.addQueryList(query_values, columns[column])

            query_columns = "{0}, {1}".format(query_columns, identifier.split("=")[0])
            query_values = "{0}, {1}".format(query_values, identifier.split("=")[1])

            query = "INSERT INTO {0} ({1}) VALUES ({2})".format(
                    table,
                    query_columns,
                    query_values,
            )
            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            pyfalog.info("Insert new record for ID ({0}) into {1}.", identifier, table)
        else:
            query_values = ""
            for column in columns:
                query_values = self.addUpdateQueryItem(query_values, column, columns[column])

            query = "UPDATE {0} SET {1} WHERE {2}".format(
                    table,
                    query_values,
                    identifier,
            )
            DatabaseCleanup.ExecuteSQLQuery(self.sESIConnection.gamedata_connection, query)
            pyfalog.debug("Updated existing record for ID ({0}) into {1}.", identifier, table)

    @staticmethod
    def addUpdateQueryItem(update_query, attribute, value, skipQuotes=False):
        if attribute and value:
            if skipQuotes:
                update_query = "{0}, {1}={2}".format(update_query, attribute, value)
            else:
                update_query = "{0}, {1}='{2}'".format(update_query, attribute, value)

            # make sure that we dont' have any commas hanging out on either side of our statement where they aren't supposed to be
            update_query = update_query.lstrip(", ").rstrip(",")
            return update_query
        else:
            return update_query

    @staticmethod
    def addQueryList(update_query, value, skipQuotes=False):
        if skipQuotes:
            update_query = "{0}, {1}".format(update_query, value)
        else:
            update_query = "{0}, '{1}'".format(update_query, value)
        # make sure that we dont' have any commas hanging out on either side of our statement where they aren't supposed to be
        update_query = update_query.lstrip(", ").rstrip(",")
        return update_query
