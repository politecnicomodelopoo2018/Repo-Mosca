from class_DBTable import *

class Post(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Post")

        self.add_columns("idPost", "FK_idThread", "FK_idUser", "title", "content", "datePosted")
        self.set_primary_key("idPost")
        self.set_default_column("datePosted", "NOW()")
        self.add_foreign_key("FK_idThread", "Thread", "idThread")
        self.add_foreign_key("FK_idUser", "User", "idUser")

    def get_display_name(self):
        return str(self.get_primary_key_col()) + " - " + self.col_dict["title"]