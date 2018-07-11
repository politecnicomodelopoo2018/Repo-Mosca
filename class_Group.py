from class_DBTable import *

class Group(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Group")

        self.add_columns("idGroup", "name", "permissionLevel")