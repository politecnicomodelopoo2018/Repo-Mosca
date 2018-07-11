from class_DBTable import *

class User(DBTable):
    def __init__(self):
        DBTable.__init__(self, "User")

        self.add_columns("idUser", "FK_idGroup", "name", "password", "nickname", "dateCreated")
        self.set_primary_key("idUser")