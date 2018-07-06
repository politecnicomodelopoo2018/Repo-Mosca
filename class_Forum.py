class Forum(object):
    def __init__(self, id_forum, id_category, name, permissionLevel):
        self.id = id_forum
        self.FK_idCategory = id_category
        self.name = name
        self.permissionLevel = permissionLevel