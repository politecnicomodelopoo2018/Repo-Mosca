class Thread(object):
    def __init__(self, id_thread, id_forum, id_user, name, date_created):
        self.id = id_thread
        self.FK_idForum = id_forum
        self.FK_idUser = id_user
        self.name = name
        self.dateCreated = date_created