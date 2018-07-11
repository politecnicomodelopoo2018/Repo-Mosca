from class_DBTable import *

class Forum(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Forum")

        self.add_columns("idForum", "FK_idCategory", "name", "permissionLevel")
        self.set_primary_key("idForum")