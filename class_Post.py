class Post(object):
    def __init__(self, id_post, id_thread, id_user, title, content, date_posted):
        self.id = id_post
        self.FK_idThread = id_thread
        self.FK_idUser = id_user
        self.title = title
        self.content = content
        self.datePosted = date_posted