import datetime

class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.dateCreated = datetime.datetime.now()


