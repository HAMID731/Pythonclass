import unittest
from exceptions.exception import NotFoundException, EmailAlreadyExistException, NameAlreadyExistException
from src.Students import Students
from src.student import Student
from src.student import Course

class TestStudents(unittest.TestCase):

    def setUp(self):
        self.students_manager = Students()
        self.student1 = Student("favour Ike", "Favourites@gmail.com", "password123")
        self.student2 = Student("favor", "favor@gmail.com", "password456")
        self.course1 = Course("CS101", "Introduction to Computer Science")
        self.course2 = Course("MATH101", "Introduction to Mathematics")

    def test_add_student(self):
        self.students_manager.add_student(self.student1)
        self.assertEqual(len(self.students_manager.get_all_students()), 1)

        with self.assertRaises(EmailAlreadyExistException):
            self.students_manager.add_student(Student("hamid", "abarihamid@gmail.com", "password789"))

        with self.assertRaises(NameAlreadyExistException):
            self.students_manager.add_student(Student("favor", "another.favor@gmail.com", "password789"))

    def test_remove_student(self):
        self.students_manager.add_student(self.student1)
        self.students_manager.remove_student("abarihamid@gmail.com")
        self.assertEqual(len(self.students_manager.get_all_students()), 0)

        with self.assertRaises(NotFoundException):
            self.students_manager.remove_student("non.existent@example.com")