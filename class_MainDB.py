from class_DataBase import DataBase
from class_Category import Category
from class_Group import Group
from class_Post import Post
from class_User import User
from class_Forum import Forum
from class_Thread import Thread


class MainDB(DataBase):
    db_tables = {
        "category": Category,
        "group": Group,
        "post": Post,
        "user": User,
        "forum": Forum,
        "thread": Thread
    }

    def getlist_table(self, target_db, table_name):
        if table_name.lower() not in self.db_tables:
            return []
        query_result = self.run_query(target_db, "SELECT * FROM " + table_name)

        category_list = []
        for row in query_result:
            tmp_table = self.db_tables[table_name.lower()]()
            tmp_table.load_from_dict(row)
            category_list.append(tmp_table)
        return category_list

    def create_row(self, table_name):
        table_name = table_name.lower()
        if table_name in self.db_tables:
            return self.db_tables[table_name]()
        return None