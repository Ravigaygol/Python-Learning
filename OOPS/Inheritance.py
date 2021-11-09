class Student_class:
    #instance variable
    school = 'GHRCEM'
    No_of_students = 0

    def __init__(self,f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        
    
    def greetings(self):
        return f'Hello I am {self.f_name} {self.l_name}'    

#****************************************************************
class child_student(Student_class):
    def __init__(self, f_name, l_name, subject):
        super().__init__(f_name, l_name)
        self.subject = subject


st_1 = child_student('ravi', 'Gaygol','Math')
print(st_1.greetings())

print('*' *98)
#****************************************************************

class college_student(Student_class):
    def __init__(self, f_name, l_name, profile):
        super().__init__(f_name, l_name)
        self.profile = profile

    #overriding parent method
    def greetings(self):
        return f'My first name is {self.f_name}...!'    
    
    #own another method
    def info(self):
        return f'My last name is {self.l_name}...!'

st_2 = college_student('raj', 'kumar','devloper')
print(st_2.greetings())    

print('*' *98)
print(st_2.info())