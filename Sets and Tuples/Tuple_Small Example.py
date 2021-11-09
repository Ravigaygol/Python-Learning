#1
# Create tuple holding 5 computer brands 
my_tuple = ('Apple', 'Dell', 'LG', 'HP', 'Acer')

print('*' *98)
#Print the third index
print(my_tuple[3])

print('*' *98)
#Print the first 3 elements by slicing
print(my_tuple[0:3])

print('*' *98)
#Print the length of tuple
print(len(my_tuple))

print('*' *98)
#Write a loop to print all elements in the tuple
for x in my_tuple:
    print(x)