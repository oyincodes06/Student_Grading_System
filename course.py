class Course:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, training_id, grade):
        self.grades[training_id] = grade

    def calculate_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return None

    def highest_grade(self):
        if self.grades:
            highest_training_id = max(self.grades, key= self.grades.get)
            return highest_training_id, self.grades[highest_training_id]
        return None
    def lowest_grade(self):
        if self.grades:
            lowest_training_id = min(self.grades, key=self.grades.get)
            return lowest_training_id, self.grades[lowest_training_id]
        return None