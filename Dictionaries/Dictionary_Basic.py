# A Dictionary is a collection which is unordered changeable and indexed

#In python dictionaries are written in curly brackets, and they have keys and values

#keys and values

user_dict = {
    'First_name' : 'Ravi' ,
    'Last_name'  : 'Gaygol',
    'Birth_year' : 1997
}

#get the values from dictionaries

print(user_dict['First_name'])
print(user_dict['Last_name'])
print(user_dict['Birth_year'])
print('.' * 90)
print(user_dict.get('First_name'))
print(user_dict.get('Last_name'))
print(user_dict.get('Birth_year'))

print('.' * 90)
#Adding the keys & values to the dictionaries

user_dict['Subject'] = 'Math'
print(user_dict.get('Subject'))
print(user_dict)

print('.' * 90)
#Print the length of dictionaries

print(len(user_dict))

print('.' * 90)
#Removing the key and value from dictionaries
#There are two methods to remove them

#1- pop
user_dict.pop('Subject')
print(user_dict)

print('.' * 90)
#popitem  - it deletes the last element of the dictionaries
user_dict.popitem()
print(user_dict)

print('.' * 90)
#2- del -it can delete the whole dictionary but if we mention key then it can delete specified
         #key-value pair

del user_dict['Last_name']
print(user_dict)

del user_dict
#print(user_dict)

print('.' * 90)
#clear method- it clear only all keys and values pairs from dictionary not the whole dictionary

user_dictionary = {
    'First_name' : 'Ravi' ,
    'Last_name'  : 'Gaygol',
    'Birth_year' : 1997
}
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)
