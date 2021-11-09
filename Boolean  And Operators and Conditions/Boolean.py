#Boolean are data type that return true or false

#Example:
is_human = True
do_you_love_food = False
name = 'Ravi'
roll_no = 19
#type(variable_name) = these method gives the data type of mention variable
print(type(is_human))
print(type(do_you_love_food))
print(type(name))
print(type(roll_no))
print('*' * 98)


#Comparison Operators

# == Equal
# != Not Equal
# >  Greater Than
# <  Less Than
# >= Greater Than or Equal to
# <= Less Than or Equal to

a = 10
b = 20
c = 10

print('a<b -{}'.format(a<b))
print('b<c -{}'.format(b<c))
print('a=b -{}'.format(a==b))
print('a=c -{}'.format(a==c))
print('a<=b -{}'.format(a<=b))
print('b>=c -{}'.format(b>=c))
print('b!=c -{}'.format(b!=c))


print('*' * 98)

#Logical Operators

#AND = Evaluates to True if both statements are True, Otherwise evaluates to False
#OR  = Evaluates to True if either of the statements is True, Otherwise evaluates to False
#NOT = Evaluates to Opposite of the statement

print('2 <= 3 AND 4 > 5 - {}'.format(2 <= 3 and 4>5))
print('4 > 7 OR 1==1  - {}'.format(4 > 7 or 1==1))
print('NOT(7 == 7) - {}'.format(not(7==7)))
print('NOT(5==7) - {}'.format(not(5==7)))

print(' ' * 98)
print('If Statemets :'+ '*' * 80)

#If Statements:

#(1)
age1 = 31
if age1 >= 35:
    print('You are old enough to be the President')
print('Have a nice day !')

print('.' * 95)

#(2)
age2 = 31
if age2 >=35:
    print('You are old enough to be the President') 
else:
    print('You are not old enough to be the President')
print('Have a nice day !')

print('.' * 95)

#(3)
age3 = 31
if age3 >= 35:
    print('You are old enough to be a senator or the president')
elif age3 >= 30:
    print('You are old enough to be the senator')
else:
    print('You are not old enough to be a senator or the president')
print('Have a nice day !')

print('.' * 95)

#(4)
age4 = 99
if age4 >= 35:
    print('You are old enough to be a Representative, senator or the president')
elif age4 >= 30:
    print('You are old enough to be the senator')
elif age4 >=25:
    print('You are old enough to be the Representative')
else:
    print('You are not old enough to be a Representative, senator or the president')
print('Have a nice day !')
    



