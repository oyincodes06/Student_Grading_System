from grades import GradeSystem
from report import Report

def main():
    grade_system = GradeSystem()

    # Registering students
    grade_system.register_student("71636", "Robbinson_Philips", "robphil@gmail.com")
    grade_system.register_student("71535", "Meran_Meklon", "meran66@gmail.com")
    grade_system.register_student("71434", "Danil Alves", "danilalv02@gmail.com")
    grade_system.register_student("71331", "Joshy_Benards", "joshybenards@gmail.com")    

    # Registering courses
    grade_system.register_course("Data_Analysis")
    grade_system.register_course("Python")
    grade_system.register_course("Cyber_Security")
    grade_system.register_course("Web_Development")
    
    # Adding/updating grades
    grade_system.add_or_update_grade("71636", "Data_Analysis", 85)
    grade_system.add_or_update_grade("71636", "Python", 80)
    grade_system.add_or_update_grade("71636", "Cyber_Security", 70)
    grade_system.add_or_update_grade("71636", "Web_Development", 60)
    
    # ----------------------------------------------------------
    grade_system.add_or_update_grade("71535", "Python", 90)
    grade_system.add_or_update_grade("71535", "Data_Analysis", 80)
    grade_system.add_or_update_grade("71535", "Cyber_Security", 70)
    grade_system.add_or_update_grade("71535", "Web_Development", 60)
    
    # ----------------------------------------------------------
    grade_system.add_or_update_grade("71434", "Python", 95)
    grade_system.add_or_update_grade("71434", "Data_Analysis", 85)
    grade_system.add_or_update_grade("71434", "Cyber_Security", 75)
    grade_system.add_or_update_grade("71434", "Web_Development", 65)
    
    #-----------------------------------------------------------
    grade_system.add_or_update_grade("71331", "Python", 98)
    grade_system.add_or_update_grade("71331", "Data_Analysis", 88)
    grade_system.add_or_update_grade("71331", "Cyber_Security", 78)
    grade_system.add_or_update_grade("71331", "Web_Development", 68)
    

    # Generate reports
    report = Report(grade_system)
    report.display_all_student_grades()
    report.display_all_subject_averages()

    # Highest and lowest in python
    result = report.get_highest_and_lowest("Python")
    print(f"Highest Score  in {result['course']}: {result['highest']}")
    print(f"Lowest Score  in {result['course']}: {result['lowest']} \n")
    # Highest and lowest in Data_Analysis
    result = report.get_highest_and_lowest("Data_Analysis")
    print(f"Highest Score in {result['course']}: {result['highest']}")
    print(f"Lowest Score in {result['course']}: {result['lowest']}\n")
    
     # Highest and lowest in Cyber_Security
    result = report.get_highest_and_lowest("Cyber_Security")
    print(f"Highest Score in {result['course']}: {result['highest']}")
    print(f"Lowest Score in {result['course']}: {result['lowest']}\n")
    
     # Highest and lowest in Web_Development
    result = report.get_highest_and_lowest("Web_Development")
    print(f"Highest Score in {result['course']}: {result['highest']}")
    print(f"Lowest Score in {result['course']}: {result['lowest']}\n")


main()
