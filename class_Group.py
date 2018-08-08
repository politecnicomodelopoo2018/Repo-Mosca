from class_DBTable import *

class UserGroup(DBTable):
    def __init__(self):
        DBTable.__init__(self, "UserGroup")

        self.add_columns("idGroup", "name", "permissionLevel")
        self.set_primary_key("idGroup")