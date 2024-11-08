class Report:
    def __init__(self, grade_system):
        self.grade_system = grade_system

    def display_all_student_grades(self):
        for training_id, student in self.grade_system.students.items():
            print(f"Grades for {student.name} ({training_id}): {student.get_grades()}\n")

    def display_all_subject_averages(self):
        for course_name, course in self.grade_system.courses.items():
            print(f"Average Score for {course_name}: {course.calculate_average()}\n")

    def get_highest_and_lowest(self, course_name):
        if course_name in self.grade_system.courses:
            course = self.grade_system.courses[course_name]
            highest = course.highest_grade()
            lowest = course.lowest_grade()
            if highest:
                highest_info = f"Training_ID {highest[0]} with score {highest[1]}"
            else:
                return 'No grades'
            if lowest:
                lowest_info = f"Training_ID {lowest[0]} with score {lowest[1]}"
            else:
                return 'No grades'
            return {
                "course" : course_name,
                "highest" : highest_info,
                "lowest" : lowest_info
            }
        else:
            print(f"Course: {course_name} not found.")
            return None
