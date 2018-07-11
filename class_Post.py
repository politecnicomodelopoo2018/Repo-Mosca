from class_DBTable import *

class Post(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Post")

        self.add_columns("idPost", "FK_idThread", "FK_idUser", "title", "content", "datePosted")
        self.set_primary_key("idPost")