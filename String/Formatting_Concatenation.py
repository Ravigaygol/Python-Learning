#String Concatenation and String Formatting

my_first_name = 'Ravi'
my_last_name = 'Gaygol'
my_name = my_first_name + ' ' + my_last_name
print(my_first_name+ ' ' + 'Gaygol')
#OR
print(my_name)
print('-' * 100) 
#-----------------------------------------------------------------

f_name = 'Ravi'
no_of_pairs = 5
# Below line gives these error- can only concatenate str (not "int") to str
# print(f_name + 'has' + no_of_pairs + 'Number of pairs')
#so to concatenate we use following 4 formats

#1
first_name = 'Ravi'
last_name = 'Gaygol'
Name = 'Hello, {} {}'.format(first_name, last_name)
print(Name)

#2
#for long string and to make it tightly secured
Name1 = 'Hello, {first} {last}'.format(first = first_name, last =last_name)
print(Name1)

#3
#To concatenate numbers in string
F_name = 'Ravi'
no_of_shoes = 10
statement = f'{F_name} has {no_of_shoes} number of shoes'
print(statement)

#4
#Using str function
Fr_name= 'Ravi'
number_of_shoes = 100
st = Fr_name +' '+ 'has' +' '+ str(number_of_shoes) +' '+ 'number of shoes'
print(st)
print('-' * 100) 

#-------------------------------------------------------------------

#Formatting String Summary
print('I {} Python.'.format('Love'))
print('{} {} {}'.format('I','Love','Python.'))
print('I {0} {1}. {1} {0}s me.'.format('Love', 'Python') )
F = 'I'
S = 'Love'
T = 'Python'
print('{} {} {}.'.format(F,S,T))
version = 3
print('I Love Python {}'.format(version))

#Allignment = Left < ,Right >, center ^
#NF= N-Number of decimal places F-float
#print('{0:8}   |  {1:Allignment NF}'.format('Fruit', 'Quantity'))

print('{0:8}   |  {1:8}'.format('Fruit', 'Quantity'))
print('{0:8}   |  {1:8}'.format('Apple', 3))
print('{0:8}   |  {1:<8}'.format('Orange', 4))
print('{0:8}   |  {1:<8.2f}'.format('Banana', 5))
print('{0:8}   |  {1:^8.3f}'.format('Chiku', 6))
print('-' *100)

#--------------------------------------------------------------------------------------------

#Taking Input from User
fruit = input('Enter name of fruit you like :')
print('{} is very nice fruit.'.format(fruit))