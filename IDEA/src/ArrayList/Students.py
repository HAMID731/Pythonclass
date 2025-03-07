from exceptions.exception import NotFoundException, EmailAlreadyExistException, NameAlreadyExistException
from src.course import Course
from src.grade import Grade
from src.student import Student


class Students:
    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError("Expected a Student object.")

        for existing_student in self.__students:
            if existing_student.email == student.email:
                raise EmailAlreadyExistException("Email already registered.")
            if existing_student.name == student.name:
                raise NameAlreadyExistException("Name already registered.")

        self.__students.append(student)

    def remove_student(self, email: str):
        student = self.find_student_by_email(email)
        if student:
            self.__students.remove(student)
        else:
            raise NotFoundException("Student not found.")

    def find_student_by_email(self, email: str) -> Student:
        for student in self.__students:
            if student.email == email:
                return student
        raise NotFoundException("Student not found.")

    def find_student_by_name(self, name: str) -> Student:
        for student in self.__students:
            if student.name == name:
                return student
        raise NotFoundException("Student not found.")

    def get_all_students(self) -> list:
        return self.__students

    def get_number_of_students(self) -> int:
        return len(self.__students)

    def is_student_registered(self, email: str) -> bool:
        try:
            self.find_student_by_email(email)
            return True
        except NotFoundException:
            return False

    def clear_all_students(self):
        self.__students.clear()

    def enroll_student_in_course(self, student_email: str, course: Course):
        student = self.find_student_by_email(student_email)
        if not isinstance(course, Course):
            raise TypeError("Expected a Course object.")
        student.add_course(course)

    def get_student_courses(self, student_email: str) -> list:
        student = self.find_student_by_email(student_email)
        return student.view_courses()

    def assign_grade_to_student(self, student_email: str, course: Course, first_ca: int, second_ca: int, exam: int):
        student = self.find_student_by_email(student_email)
        if not isinstance(course, Course):
            raise TypeError("Expected a Course object.")

        if course not in student.view_courses():
            raise NotFoundException("Student is not enrolled in this course.")

        grade = Grade(first_ca, second_ca, exam)
        course.add_grade(student_email, grade)

    def get_student_grade(self, student_email: str, course: Course):
        student = self.find_student_by_email(student_email)
        if not isinstance(course, Course):
            raise TypeError("Expected a Course object.")

        if course not in student.view_courses():
            raise NotFoundException("Student is not enrolled in this course.")

        return course.get_grade(student_email)

    def get_students_in_course(self, course: Course) -> list:

        if not isinstance(course, Course):
            raise TypeError("Expected a Course object.")

        students_in_course = []
        for student in self.__students:
            if course in student.view_courses():
                students_in_course.append(student)
        return students_in_course