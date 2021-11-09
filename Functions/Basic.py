#Functions

#function without arguments

print('Hello from outside the function..!')

def my_function():
    print('Hello from inside the function..!')

my_function()

print('*' * 98)
#-----------------------------------------------------
#function with arguments


def print_names(fName,lName):
    print(f'Hello {fName} {lName} ..!')

print_names('Ravi','Gaygol')

print('*' * 98)
#------------------------------------------------------
#function with bunch of data

def data_function(*bunch_of_data):
    print(len(bunch_of_data)-1)
    print(len(bunch_of_data))

data_function(1,2,3,4)

print('*' * 98)
#------------------------------------------------------
#function with exact value while call to function

def function1(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

function1(highest_number=150,lowest_number=10)    

print('*' * 98)
#------------------------------------------------------
#function with assign value to blank call allong with multiple call of function

def country_function(country='Somewhere on the earth'):
    print(country)

country_function('India')
country_function('swiden')
country_function() # After run the code it Assign 'Somewhere on the earth' value to these function call
country_function('Japan')
country_function('america')

print('*' * 98)
#------------------------------------------------------

#Return value through function

def return_function(number_one, number_two):
    return number_one * number_two

multiple_result = return_function(10,20)
print(multiple_result)    

print('*' * 98)
#------------------------------------------------------
# Print List with Function

def list_function(list_of_fruits):
    for fruits in list_of_fruits:
        print(fruits)

fruits_list = ['Apple','Banana','Orange','Pineapple']
list_function(fruits_list)        



