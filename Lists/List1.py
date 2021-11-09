#-list are a collection of data 
#- way to hold multiple items in a single variable

my_list1 = [1,2,3,4]
my_list2 = ['AAA','BBB','CCC','DDD']
print(my_list1)
print(my_list2)
print('-' * 80)

#--------------------------------------------------------------
# (1) Create a list variable that holds 5 colors (red,blue,green,pink,purple)
#print the index of list which value is green and print the length of list

color_list = ['red','blue','green','pink','purple']
print('Index of list which value is green = '+ color_list[2])
print('length of color_list = {}'.format(len(color_list)))
print('-' * 80)

# (2) Create a list variable that holds 5 colors (red,blue,green,pink,purple) 
# print and slice the list to print :['blue', 'green', 'pink']

print(color_list[1:4])
print('-' * 98)


#Index MEthod=
color_index = color_list.index('pink')
print(color_index)