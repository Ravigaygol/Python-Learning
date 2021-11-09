#Sorting of list methods:
#sorted()
#sort()  

animals = ['monkey','cat','dog','pig','Anaconda','Horse']

sorted_animals = sorted(animals)

print('Animals List : {}'.format(animals))
print('Sorted Animals List: {}'.format(sorted_animals))
animals.sort()
print('Animals after sort() Method: {}'.format(animals))
print('-' * 98)

#RANGES:
#format is like:
#range(start, stop, step)

#for number in range(3) :
 #    print(number)
 #    print('-' * 98)
     

#for number in range(1,3) :
 #    print(number)

#for number in range(1,10,2) :
 #    print(number)

for number in range(0, len(animals), 2) :
      print(animals[number])