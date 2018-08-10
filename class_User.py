from class_DBTable import *

class User(DBTable):
    def __init__(self):
        DBTable.__init__(self, "User")

        self.add_columns("idUser", "FK_idGroup", "name", "password", "nickname", "dateCreated")
        self.set_primary_key("idUser")
        self.add_foreign_key("FK_idGroup", "UserGroup", "idGroup")

    def get_display_name(self):
        return str(self.get_primary_key_col()) + " - " + self.col_dict["name"] + " / " + self.col_dict["nickname"]