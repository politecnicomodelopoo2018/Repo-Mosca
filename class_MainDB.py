from class_DataBase import DataBase
from class_Category import Category
from class_Group import UserGroup
from class_Post import Post
from class_User import User
from class_Forum import Forum
from class_Thread import Thread


class MainDB(DataBase):
    db_tables = {
        "category": Category,
        "usergroup": UserGroup,
        "post": Post,
        "user": User,
        "forum": Forum,
        "thread": Thread
    }

    def __init__(self, db_name):
        self.db_name = db_name

    def run_query(self, query):
        return DataBase.run_query(self.db_name, query)

    def getlist_table(self, table_name):
        if table_name.lower() not in self.db_tables:
            return []
        query_result = self.run_query(["SELECT * FROM %s;" % table_name, ()])

        table_list = []
        for row in query_result:
            tmp_table = self.db_tables[table_name.lower()]()  # Crear un objeto del tipo de la tabla recibido
            tmp_table.load_from_dict(row)  # Cargar el objeto con los datos recibidos de la BDD
            table_list.append(tmp_table)
        return table_list

    def get_table_row(self, table_name, row_id):
        if table_name.lower() not in self.db_tables:
            return None

        tmp_obj = self.db_tables[table_name.lower()]()
        query_string = "SELECT * FROM %s WHERE %s = %s;" % (table_name, tmp_obj.pkey_row, '%s')
        query_args = [str(row_id)]
        query_result = self.run_query([query_string, query_args])

        obj_dict = query_result.fetchone()
        if obj_dict:
            tmp_obj.load_from_dict(obj_dict)
            return tmp_obj
        return None

    def create_row(self, table_name):
        table_name = table_name.lower()
        if table_name in self.db_tables:
            return self.db_tables[table_name]()
        return None