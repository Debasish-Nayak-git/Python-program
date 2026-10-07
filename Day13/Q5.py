class University:
    def display(self):
        print("University name:BPUT")
class student(University):
    def name(self):
        print("Student class!")
class teacher(University):
    def teacher_name(self):
        print("Teacher class!")
class Assistant(student,teacher):
    pass
A=Assistant()
A.display(),A.name(),A.teacher_name()
