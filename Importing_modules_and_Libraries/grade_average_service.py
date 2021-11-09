def calculate_homework(homework_assignements_arg):
    sum_of_grades = 0
    for homework in homework_assignements_arg.values():
        sum_of_grades += homework
    final_grades = round(sum_of_grades / len(homework_assignements_arg),2)
    print(final_grades)