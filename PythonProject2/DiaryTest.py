from unittest import TestCase
from Diary import Diary

class TestDiaryApp(TestCase):

    def setUp(self):
        self.diary = Diary("hamid", "12342")

    def test_to_unlock_diary(self):
        self.assertEqual(self.diary.unlock_diary("12342"), "successfully unlocked!!")

    def test_to_lock_diary(self):
        self.diary.unlock_diary("12342")
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked)

    def test_to_create_entry_successfully(self):
        self.diary.unlock_diary("12342")
        self.create_entry = self.diary.create_entry("My Favorite Food","I love bread and beans")
        self.assertEqual(self.create_entry,"entry created!")

    def test_find_entry_by_id(self):
        self.diary.unlock_diary("12342")
        self.diary.create_entry("entry", "I am happy")
        self.assertEqual(self.diary.find_entry_by_id(1).title, "entry")
        self.assertEqual(self.diary.find_entry_by_id(1).body, "I am happy")

    def test_find_entry_by_id_when_diary_is_locked(self):
        self.diary.create_entry("entry", "I am happy")
        self.assertEqual(self.diary.find_entry_by_id(1), "Diary is locked!")


    def test_update_entry(self):
        self.diary.unlock_diary("12342")
        self.diary.create_entry("My Favorite Food", "I love bread and beans")
        self.diary.update_entry(1, "MY Mum", "I am very happy")
        self.assertEqual(self.diary.find_entry_by_id(1).title, "MY Mum")
        self.assertEqual(self.diary.find_entry_by_id(1).body, "I am very happy")




