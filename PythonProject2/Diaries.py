from Diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.username == username:
                return diary
        return None

    def delete(self, username, password):
        diary = self.find_by_username(username)
        if diary and diary.password == password:
            self.diaries.remove(diary)