from student import Student
from course import Course

class GradeSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def register_student(self, training_id, name, email):
        self.students[training_id] = Student(training_id, name, email)

    def register_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name)
        else:
            print(f"{course_name} is already registered.")

    def add_or_update_grade(self, training_id, course_name, grade):
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name)
        self.courses[course_name].add_grade(training_id, grade)

    def get_student_grades(self, student_id):
        if student_id in self.students:
            return self.students[student_id].get_grades()
        return None

    def get_course_average(self, course_name):
        if course_name in self.courses:
            return self.courses[course_name].calculate_average()
        return None
