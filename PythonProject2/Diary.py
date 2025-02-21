from Entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []

    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False
            return "successfully unlocked!!"
        else:
            return "Incorrect password!"

    def lock_diary(self):
        self.is_locked = True

    def is_locked(self):
        return self.is_locked

    def create_entry(self, title, body):
        if not self.is_locked:
            new_id = len(self.entries) + 1
            new_entry = Entry(new_id, title, body)
            self.entries.append(new_entry)
            return "entry created!"
        else:
            return "Diary is locked!"

    def delete_entry(self, id):
        if not self.is_locked:
            new_entries = []
            for entry in self.entries:
                if entry.id != id:
                    new_entries.append(entry)
            self.entries = new_entries
            return "entry deleted!"
        else:
            return "Diary is locked!"

    def find_entry_by_id(self, id):
        if not self.is_locked:
            for entry in self.entries:
                if entry.id == id:
                    return entry
        else:
            return "Diary is locked!"

    def update_entry(self, id, title, body):
        if not self.is_locked:
            for entry in self.entries:
                if entry.id == id:
                    entry.title = title
                    entry.body = body
                    return
        else:
            print("Diary is locked!")





