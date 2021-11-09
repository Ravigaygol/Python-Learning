#Adding and deleting elements in List

#append()= adding specified element at the end of the list
#insert(index, value)= adding specified element to specified index in the list
#extend()= adding multiple elements or adding a list to another list

#remove()= deleting specified element directly
#pop(index) = deleting specified element according to index

my_list = [1,2,3,4,5]


print(my_list)
my_list.append(100)
my_list.insert(1,10)
print(my_list)
print('-' * 98)

my_list.remove(2)
print(my_list)
my_list.pop(3)
print(my_list)

print('-' * 98)
new_list = ['a','b','c']
my_list.extend(new_list)
my_list.extend(['x','y','z'])
print(my_list)

