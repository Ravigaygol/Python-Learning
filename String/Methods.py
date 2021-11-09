#Some Important String Methods or functions as follows

text = 'Hello Ravi Gaygol.'
text2 = '12345'
text3 = '  ABC  '
text4 = 'Hello Ravi Gaygol'
text5 = 'Ravi Gaygol'

#Slicing of String
text1 = 'ravi'[1:3]
print(text1)
print('-' * 98)


#1- print()= Display values
#Example:
print(text) 
print('-' * 100)

#2- len()= Return the length of an item
#Example:
print(len(text))
print('-' * 100)

#3- str()= Return a string object
#Example:
print('Hello My name is'+' '+text5 +' '+'and my account password is' +' '+ str(text2))
print('-' * 100)

#4- input()= Take the input from user or Read the imput
#Example:
#name = input('Enter you name:')
#BirthYear = input('Enter your birth year:')
#print(f'{name} was born in {BirthYear}')
print('-' * 100)

#5- upper()= Return the copy of the string in uppercase
#Example:
print(text.upper())
print('-' * 100)


#6- lower()= Return the copy of the string in lowercase
#Example:
print(text.lower())
print('-' * 100)


#7- format()= Return the formatted version of string
#Example:
print('Hello everyone my name is {}'.format(text5))
print('-' * 100)


#8- capitalize()= Convert First letter to upper case
#Example:
print(text.capitalize())
print('-' * 100)


#9- count()= Return number of times a specified value occurs in a string
#Example:
print(text.count('a'))
print('-' * 100)


#10- endswith()= Return true if the string ends with specified value
#Example:
print(text.endswith('.'))
print(text.endswith('!'))
print('-' * 100)


#11- isDigit()= Return true if all characters in the string are digits
#Example:
print(text.isdigit())
print(text2.isdigit())
print('-' * 100)


#12- split()= Split the string at the specified seperator and return a list
#Example
print(text.split())
print(text.split(','))
print('-' * 100)

#13- find()= Searches the string for a specified value and return the position of where it was found
#Example:
print(text.find('Ravi'))
print('-' * 100)


#14- join()= Convert the elements of an itrable into a string
#Example:
print(text, ','.join('abcdefg'))
print(text, ':'.join('abcdefg'))
print(text, ':'.join(('10','12','2015')))
print('-' * 100)


#15- strip()= Return the trimmed version of the string(elaminated front and backside spaces from string)
#Example:
print(text3)
print(text3.strip())
print('-' * 100)


#16- replace()= Return the string where a specified value is replace with the specified value
#Example:
print(text4)
new_text4 = text4.replace('Hello','Welcome')
print(new_text4)
print('-' * 100)  
