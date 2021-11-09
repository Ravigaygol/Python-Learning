class Student:
    pass

student1 = Student()
student2 = Student()

student1.first_name = 'Ravi'
student1.last_name = 'Gaygol'
student1.subject = 'Math'

student2.first_name = 'Ankit'
student2.last_name = 'Kumar'
student2.subject = 'Science'

print(student1.first_name)
print(student1.last_name)
print(' '*98)

print(student2.first_name)
print(student2.last_name)

print('*' *98)

#****************************************************************

#Instead of initializing the varibles like above we can initialize it like below

class Student_class:
    #instance variable
    school = 'GHRCEM'
    No_of_students = 0

    def __init__(self,f_name, l_name, sub):
        self.f_name = f_name
        self.l_name = l_name
        self.sub = sub

        Student_class.No_of_students += 1

    def full_name_with_subject(self):
        return f'{self.f_name} {self.l_name} like {self.sub} subject..!'

    def First_name_with_school(self):
        return f'{self.f_name} belongs to {self.school} school...!'   

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

#****************************************************************
print(f'Number of students : {Student_class.No_of_students}')
print('*' *98)

student_one = Student_class('Rahul','Kumar','Env')
student_two = Student_class('Ranveer','Singh','Polity')


print(f'Number of students : {Student_class.No_of_students}')
print('*' *98)

print(student_one.f_name)
print(student_two.f_name)

print('*' *98)
print(student_one.full_name_with_subject())
print(student_two.full_name_with_subject())

print('*' *98)

print(student_one.First_name_with_school())
print(student_two.First_name_with_school())


print('*' *98)
#Or we can call the child class by using parent class like

print(Student_class.full_name_with_subject(student_one))
print(Student_class.full_name_with_subject(student_two))

print('*' *98)

#****************************************************************

print(student_one.school)
print(student_two.school)

print('*' *98)
Student_class.set_online_school('I use youtube for learning anything..!')

print(student_one.school)
print(student_two.school)
