#sets are un-ordered and unique data structure
#As these are unordered so we cannot apply indexing on sets

my_set = {'apples' ,'bananas', 'oranges', 'melons', 'etc....'}

print('*' *98)
print(my_set)

print('*' *98)
print('apples' in my_set)

print('*' *98)
#Looping on sets

for x in my_set:
    print(x)

print('*' *98)
#Remove elements from sets
#using remove method- It will gives error if mentioned item is not present in set

my_set.remove('apples')
print(my_set)

print('*' *98)
#using discard method- It does not gives any error if mentioned item is not present in set
my_set.discard('bananas')
print(my_set)
my_set.discard('bananas')

print('*' *98)
#Clear method- it clear the set totally

#Union method- it combined th sets each other

set_one = {1,2,3,4,5}
set_two = {6,7,8,9}

set_three = set_one.union(set_two)
print(set_three)

print('*' *98)
#Adding element to the set
#By using add method- These method can able to add  only one element at a time

set_three.add(10)
print(set_three)

print('*' *98)
#By using update method - Thse method can able to add multiple elements at a time

set_three.update([11,12,13])
print(set_three)

print('*' *98)
#len method to calculate length of set

print(len(my_set))