from class_DBTable import *

class Category(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Category")

        self.add_columns("idCategory", "name")
        self.set_primary_key("idCategory")

    def get_display_name(self):
        return str(self.get_primary_key_col()) + " - " + self.col_dict["name"]