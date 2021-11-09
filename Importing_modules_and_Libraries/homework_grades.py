#Modules get used all the time throughout the programming 

#- It helps with creating more files , with unique purposes ,to help with
# clean maintainable code

import Importing_modules_and_Libraries.grade_average_service as grade_service
homework_assignment_grades = {
    'homework_1' : 85,
    'homework_2' : 100,
    'homework_3' : 80
}


grade_service.calculate_homework(homework_assignment_grades)
#calculate_homework(homework_assignment_grades)        