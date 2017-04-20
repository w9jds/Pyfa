from esipy import App
from esipy import EsiClient
import eos.db
from eos.db.saveddata.databaseRepair import DatabaseCleanup
from eos.gamedata import Item
from eos.db.gamedata import queries
import collections

# dogma_attributes = esi_app.op['get_dogma_attributes']()
# attributes = esi_client.request(dogma_attributes)


class esiUpdate(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = esiUpdate()

        return cls.instance

    def __init__(self):
        self.esi_app = App.create('https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility')
        self.esi_client = EsiClient()

        self.gamedata_engine = eos.db.gamedata_engine

    def updateTypes(self):
        """
        Main loop.
        """
        esi_universe_types_op = self.esi_app.op['get_universe_types']()
        esi_universe_types = self.esi_client.request(esi_universe_types_op)

        item_attribute_translation = {
            "type_id": "ID",
            "icon_id": "iconID",
        }

        for esi_type_id in esi_universe_types.data:
            esi_universe_types_type_id_op = self.esi_app.op['get_universe_types_type_id'](
                    type_id=esi_type_id,
            )
            esi_universe_types_type_id = self.esi_client.request(esi_universe_types_type_id_op)
            esi_item = esi_universe_types_type_id.data

            if esi_item:
                try:
                    esi_item_published = getattr(esi_item, "published", False)
                    esi_item_name = getattr(esi_item, "name", None)
                    esi_item_id = getattr(esi_item, "type_id", None)
                except:
                    # Missing name, ID, or not published, skip.
                    continue

                if not esi_item_id or not esi_item_published or not esi_item_name:
                    # Missing name, ID, or not published, skip.
                    continue

                esiUpdate.process_invItems(esi_type_id)

    @staticmethod
    def add_update_query_item(update_query, attribute, value):
        if attribute and value:
            value = value.replace("'", "''")
            update_query = "{0}, {1}='{2}'".format(update_query, attribute, value)
            # make sure that we dont' have any commas hanging out on either side of our statement where they aren't supposed to be
            update_query = update_query.lstrip(", ").rstrip(",")
            return update_query
        else:
            return update_query

    @staticmethod
    def add_insert_query_item(columns_query, values_query, attribute, value):
        if attribute and value:
            if attribute == 'published':
                # SQLite doesn't understand true/false, so set to 1/0
                if value:
                    value = 1
                else:
                    value = 0

            try:
                value = value.replace("'", "''")
            except AttributeError:
                # Not working with a string, that's okay. Skip.
                pass

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

    def process_invItems(esi_type_id):
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
        check_existance_results = DatabaseCleanup.ExecuteSQLQuery(self.gamedata_engine, check_existance_query)
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
                            column_query, values_query = add_insert_query_item(column_query, values_query, map_item, esi_item_attribute_value)
                    except:
                        pass

            if column_query.__len__() > 0 and values_query.__len__() > 0:
                update_query = "INSERT INTO invtypes {0} VALUES {1}".format(column_query, values_query)
                DatabaseCleanup.ExecuteSQLQuery(self.gamedata_engine, update_query)
        else:
            update_query = ""

            for map_item in invtype_mapping:
                if invtype_mapping[map_item]:
                    try:
                        esi_item_attribute_value = esi_item[invtype_mapping[map_item]]
                        if esi_item_attribute_value:
                            update_query = add_update_query_item(update_query, map_item, esi_item_attribute_value)
                    except:
                        pass

            if update_query.__len__() > 0:
                update_query = "UPDATE invtypes SET {0} WHERE typeID = {1}".format(update_query, esi_type_id)
                DatabaseCleanup.ExecuteSQLQuery(self.gamedata_engine, update_query)
