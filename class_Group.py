from class_DBTable import *

class UserGroup(DBTable):
    def __init__(self):
        DBTable.__init__(self, "UserGroup")

        self.add_columns("idGroup", "name", "permissionLevel")
        self.set_primary_key("idGroup")

    def get_display_name(self):
        return str(self.get_primary_key_col()) + " - " + self.col_dict["name"] + " (" + str(self.col_dict["permissionLevel"]) + ")"