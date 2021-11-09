#Create the function called remove elements that takes a single list argument within the function
# remove the first and last index of the list back and print the new list

def remove_elements(number_list_arg):
    number_list_arg.pop(0)
    number_list_arg.pop(-1)
    return number_list_arg

number_list = [1,2,3,4,5,6]
updated_list = remove_elements(number_list)
print(updated_list)    