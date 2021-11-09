animals = ['monkey','cat','dog','pig']

# For LOOP format-

# item_variable in List_name:
#            code Block


#example:
#1-
for animal in animals :
    print(animal.upper())
print('-' * 98)

#2-
numbers_list = [1,2,3,4,5]
sum_of_loop = 0
for x in range(3,6):
    sum_of_loop += x
    print(sum_of_loop)
print('-' * 98)


#While LOOP format-

# while condition :
#           code block

#example
#1-
index = 0
while index < len(animals) :
      print(animals[index])
      index += 1
print('-' * 98)

#2-
x = 0
while x < 10:
    x += 1
    print(x)
print('-' * 98)


#3-
a = 0
while a < 10:
    a += 1
    if a == 5:
       continue
    print(a)
print('-' * 98)

#4-

a = 0
while a < 10:
    print(a)
    a += 1
else:
    print('a is now equal to or larger than 10 !')
print('-' * 98)

#5-
i = 10
while i <= 10 and i > 5:
    if i%2 == 0 :
        print(f'{i} is divisible by 2')
    else:
        print(f'{i} is not divisible by 2')
    i -= 1 
print('-' * 98)

#6-
i = 5
while i >= 0:
    if i == 0:
        print('STOP')
    else:
        print(i)
    i -= 1         