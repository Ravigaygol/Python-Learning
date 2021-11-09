# A tuple is a collection which is ordered and unchangeable. In python tuples are
# written with round parentheses.

#In tuples values are accessed by index
#Iteration, looping, concatenation
#Use when data should not change
#We cannot able to add or remove elements from tuples

print('*' *98)
#Tuples can be converted to list by using the list() built-in-function
weekend_tuple = ('Sat', 'Sun')
weekend_list = list(weekend_tuple)
print(type( weekend_tuple))
print(type(weekend_list))

print('*' *98)
#List can be converted to tuples by using the tuple() built-in-function
animal_list = ['horse','Monkey','tiger']
animal_tuple = tuple(animal_list)
print(type(animal_list))
print(type(animal_tuple))

print('*' *98)

my_tuple = (1,2,3,4,5)
print(my_tuple)

print('*' *98)
print(my_tuple[2])

print('*' *98)
print(my_tuple[-2])

print('*' *98)
print(len(my_tuple))

print('*' *98)
#Looping on tuples :
for x in my_tuple:
    print(x)

print('*' *98)
contact_info = ('112-4566', 'Ravi@gmail.com') 
(phone_no, mail) = contact_info
print(phone_no)
print(mail)

print('*' *98)
contacts = [('Ravi','1001'),('gaygol','554-455')]

for (name , contact) in contacts:
    print("{} phone number is :{}".format(name, contact))


print('*' *98)
#Delete the tuple by using del method: 

del contacts
print(contacts)    