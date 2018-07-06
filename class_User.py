class User(object):
    def __init__(self, id_user, id_group, name, password, nickname, date_created):
        self.id = id_user
        self.FK_idGroup = id_group
        self.name = name
        self.password = password
        self.nickname = nickname
        self.dateCreated = date_created