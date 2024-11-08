class Student:
    def __init__(self, training_id, name, email):
        self.training_id = training_id
        self.name = name
        self.email = email
        self.grades = {}

    def register_course(self, course_name):
        if course_name not in self.grades:
            self.grades[course_name] = 0
        else:
            print(f"{course_name} is already registered for {self.name}.")

    def update_grade(self, course_name, grade):
        if course_name in self.grades:
            self.grades[course_name] = grade
        else:
            print(f"{course_name} is not registered for {self.name}.")

    def get_grades(self):
        return self.grades
