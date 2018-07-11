from class_DBTable import *

class Thread(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Thread")

        self.add_columns("idThread", "FK_idForum", "FK_idUser", "name", "dateCreated")
        self.set_primary_key("idThread")