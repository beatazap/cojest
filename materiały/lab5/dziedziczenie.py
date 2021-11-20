class Student:
    def __init__(self, first_name, last_name, group, prog2):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.mark_prog2 = prog2
         

class GraduatedStudent(Student):
    def __init__(self, first_name, last_name, group, prog2, final_mark):
        super().__init__(first_name, last_name, group, prog2)
        self.final_mark = final_mark
        
    def show_diploma(self):
        print(f"""
            {self.first_name} {self.last_name}
            Ukończył studia z oceną {self.final_mark}          
            """)
