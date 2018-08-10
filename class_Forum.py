from class_DBTable import *

class Forum(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Forum")

        self.add_columns("idForum", "FK_idCategory", "name", "permissionLevel")
        self.set_primary_key("idForum")
        self.add_foreign_key("FK_idCategory", "Category", "idCategory")

    def get_display_name(self):
        return str(self.get_primary_key_col()) + " - " + self.col_dict["name"]