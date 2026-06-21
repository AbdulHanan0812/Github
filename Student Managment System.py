from datetime import datetime

class Student:
    def __init__(self, name, class_level, parents_name, emergency_contact):
        self.name = name 
        self.class_level = class_level
        self.parents_name = parents_name 
        self.emergency_contact = emergency_contact
        self.adm_date = datetime.now().strftime("%Y-%m-%d")

        self.attandance = {}
        self.leave = []
        self.marks = {}

    def teacher_attandance(self, date, status):
        self.attandance[date] = status

    def teacher_leave(self, date, reason): 
        self.leave.append(f"{date} ({reason})")
   
    def teaher_updateMarks(self, sub_name, obtaind_marks):
        self.marks[sub_name] = obtaind_marks
#================================== Print Section ==================================

class academy_portal:
    def __init__(self):
        self.student_db = {}

    def student_report_card(self, name):
        if name not in self.student_db:
            print("Student Is Not Added Yet!")
        else:
            s = self.student_db[name]
            print("===================================================================================")
            print("                             Student Details                                       ")
            print("===================================================================================")
            
            print(f"Student Name = {s.name:<20}  Class = {s.class_level}\n ")
            print(f"\n Guardein Name(Father/Mother) = {s.parents_name:<20}   Contact No: {s.emergency_contact}")
            print(f"Admission Date :{s.adm_date:<20}")

            print("===================================================================================")
            print("                             Student Attandance Details                            ")
            print("===================================================================================")
            
            print(f" Attandance :{s.attandance if s.attandance else 'No Record Yet!'}")
            print(f"Leave : {s.leave if s.leave else 'No Leave Yet! '}")
            
            print("===================================================================================")
            print("                             Student Marks Details                                 ")
            print("===================================================================================")
           
            if s.marks:
                total_obtained = 0
                total_subject = len(s.marks) 
                for sub, m in s.marks.items():
                    print(f"\n {sub:<20} : {m} /100")
                    total_obtained += m
                    
                max_total_subject = total_subject * 100
                percentage = (total_obtained / max_total_subject) * 100
                   
                print(f"Total Obtained Marks : {total_obtained:<20}")
                print(f"Percentage :{percentage:.2f}%")
            else:
                print("No Marks Entered By Teacher! ")
#================================== Main Execution Section ==================================  
if __name__ == "__main__":
    portal = academy_portal()
    date_time = datetime.now().strftime("%Y-%m-%d") 
    
    print("====================(Admin) New Comers Details===================")
    
    adm_name = input("Enter Student Name  = ").strip()
    adm_class = input("Enter Class (e.g 1 - 12) = ").strip()
    adm_parents_name = input("Enter Father/Mother Name = ").strip()
    adm_parents_contact = input("Enter Father/Mother No : ").strip()
    portal.student_db[adm_name] = Student(adm_name, adm_class, adm_parents_name, adm_parents_contact)
    print(f"\n {adm_name} is Added !")
  
    print("==================== Student (Attandance / Leave) Details===================")
    
    att_input = input(f" Mark Attandance {adm_name} (Present for P and Absent For A) =  ").strip().lower()
    if att_input == "p":
        status = 'Present'
    else:
        status = "Absent"
    portal.student_db[adm_name].teacher_attandance(date_time, status)
    
    leave_input = input("Do You Want Leave (YES /NO ) = ").strip().upper()
    if leave_input == "YES":
        leave_reason = input("Enter Leave Reason = ").strip()
        portal.student_db[adm_name].teacher_leave(date_time, leave_reason)
    else:
        print("No Leave Record Yet!")

    print("==================== Student Marks Update Details===================")
    while True:
        subject_name = input("Enter Subject Name (Done For Exit) = ").strip().upper()
        if subject_name == "DONE":
            break
        else:
            try:
                score = int(input(f"Enter Marks For {subject_name} = "))
                portal.student_db[adm_name].teaher_updateMarks(subject_name, score)
            except ValueError:
                print('Please Enter Correct Number!')
                
    portal.student_report_card(adm_name)


