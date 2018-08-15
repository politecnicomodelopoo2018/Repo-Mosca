from class_DBTable import *

class Thread(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Thread")

        self.add_columns("idThread", "FK_idForum", "FK_idUser", "name", "dateCreated")
        self.set_primary_key("idThread")
        self.set_default_column("dateCreated", "NOW()")
        self.add_foreign_key("FK_idForum", "Forum", "idForum")
        self.add_foreign_key("FK_idUser", "User", "idUser")

    def get_display_name(self):
        return str(self.get_primary_key_col()) + " - " + self.col_dict["name"]