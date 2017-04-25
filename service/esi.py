from esipy import App
from esipy import EsiClient
import eos.db
from eos.db.saveddata.databaseRepair import DatabaseCleanup
from logbook import Logger
from itertools import chain

pyfalog = Logger(__name__)


class esiUpdate(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiUpdate()

        return cls.instance

    def __init__(self):
        self.esi_app = App.create('https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility')
        self.esi_client = EsiClient(
            headers={"User-Agent": "pyfa.fit_<3_snowedin"},
            retry_requests=True
        )

        gamedata_engine = eos.db.gamedata_engine
        self.gamedata_connection = gamedata_engine.connect()

    def cleanMarketGroupsFromTypes(self, market_groups):
        pyfalog.info("Removing all invalid market IDs")
        query_list = ""
        for market_group in market_groups:
            query_list = self.add_query_list(query_list, market_group)
        update_query = "UPDATE invtypes SET marketGroupID = NULL WHERE marketGroupID NOT IN ({0})".format(query_list)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, update_query)
        pyfalog.info("Removed incorrect Market Group ID from {0} items.", query_results.rowcount)

    def fetchEsiMarketID(self):
        esi_market_group_types_list = {}
        pyfalog.info("Fetching market group list from ESI")
        esi_request = self.esi_app.op['get_markets_groups']()
        esi_market_groups = self.esi_client.request(esi_request).data

        self.cleanMarketGroupsFromTypes(esi_market_groups)

        pyfalog.info("Fetching market group items from ESI")
        esi_market_group_types = self.esi_client.multi_request(
                [self.esi_app.op["get_markets_groups_market_group_id"](market_group_id=x) for x in esi_market_groups],
                threads=50,
        )

        self.cleanMarketGroups(esi_market_group_types)

        esi_market_group_types_list = [x.data for x in [x[1] for x in esi_market_group_types]]

        return esi_market_group_types_list

    def cleanMarketGroups(self, esi_market_group_types):
        pyfalog.info("Updating and cleaning market groups")
        for esi_market_group in esi_market_group_types:
            try:
                esi_market_group_id = getattr(esi_market_group[1].data, "market_group_id", None)
            except (AttributeError, KeyError):
                continue

            pyfalog.debug("Updating market group {0}.", esi_market_group_id)

            try:
                esi_market_group_name = getattr(esi_market_group[1].data, "name", None)
                esi_market_group_name = esi_market_group_name.replace("'", "''")
                if esi_market_group_name is None:
                    esi_market_group_name = ""
            except (AttributeError, KeyError):
                esi_market_group_name = ""

            try:
                esi_market_group_description = getattr(esi_market_group[1].data, "description", None)
                esi_market_group_description = esi_market_group_description.replace("'", "''")
                if esi_market_group_description is None:
                    esi_market_group_description = ""
            except (AttributeError, KeyError):
                esi_market_group_description = ""

            try:
                esi_market_group_parent_group_id = getattr(esi_market_group[1].data, "parent_group_id", None)
                if esi_market_group_parent_group_id is None:
                    esi_market_group_parent_group_id = "Null"
            except (AttributeError, KeyError):
                esi_market_group_parent_group_id = "Null"

            query = "SELECT * FROM invmarketgroups WHERE marketGroupID = '{0}'".format(esi_market_group_id)
            results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
            row = results.first()

            if row is None:
                query = "INSERT INTO invmarketgroups (marketGroupID, marketGroupName, description, parentGroupID) VALUES ({0}, {1}, {2}, {3})".format(
                    esi_market_group_id,
                    esi_market_group_name,
                    esi_market_group_description,
                    esi_market_group_parent_group_id,
                )
                DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
            else:
                query = "UPDATE invmarketgroups SET marketGroupName = '{1}', description = '{2}', parentGroupID ='{3}' WHERE marketGroupID = '{0}'".format(
                    esi_market_group_id,
                    esi_market_group_name,
                    esi_market_group_description,
                    esi_market_group_parent_group_id,
                )
                DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)

        return

    def updateTypesMarketGroup(self, market_list):
        pyfalog.info("Updating items market group.")
        for market_group in market_list:
            if market_group['types'].__len__() > 0:
                query_list = ""
                for market_group_type in market_group['types']:
                    query_list = self.add_query_list(query_list, market_group_type)
                update_query = "UPDATE invtypes SET marketGroupID = '{0}' WHERE typeID in ({1})".format(market_group['market_group_id'], query_list)
                query_results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, update_query)
                pyfalog.debug("Added Market Group ID ({0}) to {1} items.", market_group['market_group_id'], query_results.rowcount)

    def fetchEsiTypes(self):
        esi_types_list = []
        pyfalog.info("Fetching type_id list from ESI")
        for _ in range(5000):
            esi_universe_types_op = self.esi_app.op['get_universe_types'](
                page=(_ + 1),
            )
            esi_universe_types = self.esi_client.request(esi_universe_types_op)
            if esi_universe_types.data.__len__() == 0:
                break

            esi_types_list.extend(esi_universe_types.data)

        return esi_types_list

    def updateTypes(self):
        """
        Main loop.
        """
        pyfalog.info("Started updating items.")

        trans = self.gamedata_connection.begin()
        setting_to_use_all_items = False

        esi_type_list = self.fetchEsiTypes()

        esi_market_group_types_list = self.fetchEsiMarketID()
        esi_market_type_list = [i for i in chain.from_iterable([x['types'] for x in esi_market_group_types_list])]

        if not setting_to_use_all_items:
            esi_type_list = esi_market_type_list

        self.clean_types(esi_type_list, esi_market_type_list)

        self.updateTypesData(esi_type_list)

        self.updateTypesMarketGroup(esi_market_group_types_list)
        trans.commit()
        DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, "VACUUM")
        pyfalog.info("Completed updating items.")

    def updateTypesData(self, esi_type_list):
        pyfalog.info("Fetching types from ESI.")
        esi_universe_types_type_list = self.esi_client.multi_request(
                [self.esi_app.op["get_universe_types_type_id"](type_id=x) for x in esi_type_list],
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
                # DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, "BEGIN TRANSACTION")

                setting_to_allow_published = True
                if (setting_to_allow_published is True and esi_item_published is True) or setting_to_allow_published is False:
                    self.process_invItems(esi_item_id, esi_item)

                try:
                    if hasattr(esi_item, 'dogma_attributes'):
                        esi_item_attributes = getattr(esi_item, 'dogma_attributes', None)
                    else:
                        esi_item_attributes = None
                except AttributeError:
                    esi_item_attributes = None

                try:
                    if hasattr(esi_item, 'dogma_effects'):
                        esi_item_effects = getattr(esi_item, 'dogma_effects', None)
                    else:
                        esi_item_effects = None
                except AttributeError:
                    esi_item_effects = None

                self.clean_item_dogma(esi_item_id, esi_item_attributes, esi_item_effects)

                if esi_item_attributes:
                    count_insert = 0
                    count_update = 0
                    for esi_attribute in esi_item_attributes:
                        query = "SELECT * FROM dgmtypeattribs WHERE typeID = '{0}' and attributeID = '{1}'".format(esi_item_id, esi_attribute['attribute_id'])
                        results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
                        row = results.first()

                        if row is None:
                            query = "INSERT INTO dgmtypeattribs (typeID, attributeID, value) VALUES ({0}, {1}, {2})".format(
                                esi_item_id,
                                esi_attribute['attribute_id'],
                                esi_attribute['value']
                            )
                            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
                            count_insert += 1
                        else:
                            query = "UPDATE dgmtypeattribs SET value = '{0}' WHERE typeID = '{1}' and attributeID = '{2}'".format(
                                esi_attribute['value'],
                                esi_item_id,
                                esi_attribute['attribute_id']
                            )
                            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
                            count_update += 1
                    pyfalog.debug("For TypeID ({0}) updated {1} and added {2} attributes.", esi_item_id, count_update, count_insert)

                if esi_item_effects:
                    count_insert = 0
                    for esi_effect in esi_item_effects:
                        query = "SELECT * FROM dgmtypeeffects WHERE typeID = '{0}' and effectID = '{1}'".format(esi_item_id, esi_effect['effect_id'])
                        results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
                        row = results.first()

                        if row is None:
                            query = "INSERT INTO dgmtypeeffects (typeID, effectID) VALUES ({0}, {1})".format(esi_item_id, esi_effect['effect_id'])
                            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
                            count_insert += 1
                    pyfalog.debug("For TypeID ({0}) added {1} effects.", esi_item_id, count_insert)

    @staticmethod
    def add_update_query_item(update_query, attribute, value):
        if attribute and value:
            if attribute == 'published':
                # SQLite doesn't understand true/false, so set to 1/0
                if value == "True" or value is True:
                    value = 1
                elif value == "False" or value is False:
                    value = 0
                else:
                    # Unexpected value, so set to 0
                    value = 0

            # Set value to a string so we can perform string manipulations
            value = str(value)
            value = value.replace("'", "''")

            update_query = "{0}, {1}='{2}'".format(update_query, attribute, value)
            # make sure that we dont' have any commas hanging out on either side of our statement where they aren't supposed to be
            update_query = update_query.lstrip(", ").rstrip(",")
            return update_query
        else:
            return update_query

    @staticmethod
    def add_query_list(update_query, value):
        # Set value to a string so we can perform string manipulations
        value = str(value)
        value = value.replace("'", "''")

        update_query = "{0}, '{1}'".format(update_query, value)
        # make sure that we dont' have any commas hanging out on either side of our statement where they aren't supposed to be
        update_query = update_query.lstrip(", ").rstrip(",")
        return update_query

    @staticmethod
    def add_insert_query_item(columns_query, values_query, attribute, value):
        if attribute and value:
            if attribute == 'published':
                # SQLite doesn't understand true/false, so set to 1/0
                if value == "True" or value is True:
                    value = 1
                elif value == "False" or value is False:
                    value = 0
                else:
                    # Unexpected value, so set to 0
                    value = 0

            # Set value to a string so we can perform string manipulations
            value = str(value)
            value = value.replace("'", "''")

            columns_query = columns_query.lstrip("(").rstrip(")")
            columns_query = "{0}, {1}".format(columns_query, attribute)
            columns_query = columns_query.lstrip(", ").rstrip(",")
            columns_query = "({0})".format(columns_query)

            values_query = values_query.lstrip("(").rstrip(")")
            values_query = "{0}, '{1}'".format(values_query, value)
            values_query = values_query.lstrip(", ").rstrip(",")
            values_query = "({0})".format(values_query)

            return columns_query, values_query
        else:
            return columns_query, values_query

    def process_invItems(self, esi_type_id, esi_item):
        invtype_mapping = {
            "capacity"     : "capacity",
            "description"  : "description",
            "factionID"    : None,
            "groupID"      : "group_id",
            "iconID"       : "icon_id",
            "marketGroupID": None,
            "mass"         : "mass",
            "published"    : "published",
            "raceID"       : None,
            "typeName"     : "name",
            "volume"       : "volume",
        }

        check_existance_query = "SELECT * FROM invTypes WHERE typeID = '%d'" % esi_type_id
        check_existance_results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, check_existance_query)
        row = check_existance_results.first()

        if row is None:
            # It doesn't exist, create it.
            column_query = "(typeID)"
            values_query = "({0})".format(esi_type_id)

            for map_item in invtype_mapping:
                if invtype_mapping[map_item]:
                    try:
                        esi_item_attribute_value = esi_item[invtype_mapping[map_item]]
                        if esi_item_attribute_value:
                            column_query, values_query = self.add_insert_query_item(column_query, values_query, map_item, esi_item_attribute_value)
                    except Exception:
                        pass

            if column_query.__len__() > 0 and values_query.__len__() > 0:
                update_query = "INSERT INTO invtypes {0} VALUES {1}".format(column_query, values_query)
                DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, update_query)
                pyfalog.debug("Added TypeID ({0}) to the database.", esi_type_id)
        else:
            update_query = ""

            for map_item in invtype_mapping:
                if invtype_mapping[map_item]:
                    try:
                        esi_item_attribute_value = esi_item[invtype_mapping[map_item]]
                        if esi_item_attribute_value:
                            update_query = self.add_update_query_item(update_query, map_item, esi_item_attribute_value)
                    except Exception:
                        pass

            if update_query.__len__() > 0:
                update_query = "UPDATE invtypes SET {0} WHERE typeID = {1}".format(update_query, esi_type_id)
                DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, update_query)
                pyfalog.debug("Updated TypeID ({0}) in the database.", esi_type_id)

    def clean_types(self, esi_types, esi_market_types):
        pyfalog.debug("Purging items that don't exist, and cleaning market groups.")

        update_query = ""
        for type in esi_types:
            update_query = self.add_query_list(update_query, type)

        update_market_query = ""
        for type in esi_market_types:
            update_market_query = self.add_query_list(update_market_query, type)

        query = "DELETE FROM invTypes WHERE typeID NOT IN ({0})".format(update_query)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
        pyfalog.debug("Deleted {0} records out of invTypes", query_results.rowcount)

        query = "UPDATE invTypes SET marketGroupID = NULL WHERE typeID NOT IN ({0})".format(update_market_query)
        query_results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
        pyfalog.debug("Set {0} records in invTypes to market group of null.", query_results.rowcount)

    def clean_types_dogma(self, dogma_attributes_list, dogma_effects_list):
        pyfalog.debug("Purging dogma attributes and effects from items that don't exist.")
        if dogma_attributes_list:
            update_query_list = ""
            for dogma_attribute in dogma_attributes_list:
                update_query_list = self.add_query_list(update_query_list, dogma_attribute)

            query = "DELETE FROM dgmtypeattribs WHERE typeID NOT IN ({0})".format(update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
            pyfalog.debug("Cleaned obsolete records from dgmtypeattribs.")

        if dogma_effects_list:
            update_query_list = ""
            for dogma_effect in dogma_effects_list:
                update_query_list = self.add_query_list(update_query_list, dogma_effect)

            query = "DELETE FROM dgmtypeeffects WHERE typeID NOT IN ({0})".format(update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
            pyfalog.debug("vrecords from dgmtypeeffects.")

    def clean_item_dogma(self, esi_item_id, esi_item_attributes, esi_item_effects):
        pyfalog.debug("Cleaning dogma attributes and effects from items.")
        if esi_item_attributes and esi_item_id:
            esi_item_attributes_list = [x['attribute_id'] for x in esi_item_attributes]
            update_query_list = ""
            for dogma_attribute in esi_item_attributes_list:
                update_query_list = self.add_query_list(update_query_list, dogma_attribute)

            query = "DELETE FROM dgmtypeattribs WHERE typeID = '{0}' AND attributeID NOT IN ({1})".format(esi_item_id, update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
            pyfalog.debug("Deleted records from dgmtypeattribs for item ({0}).", esi_item_id)

        if esi_item_effects and esi_item_id:
            esi_item_effects_list = [x['effect_id'] for x in esi_item_effects]
            update_query_list = ""
            for dogma_effect in esi_item_effects_list:
                update_query_list = self.add_query_list(update_query_list, dogma_effect)

            query = "DELETE FROM dgmtypeeffects WHERE typeID = '{0}' AND effectID NOT IN ({1})".format(esi_item_id, update_query_list)
            DatabaseCleanup.ExecuteSQLQuery(self.gamedata_connection, query)
            pyfalog.debug("Deleted records from dgmtypeeffects for item ({0}).", esi_item_id)
