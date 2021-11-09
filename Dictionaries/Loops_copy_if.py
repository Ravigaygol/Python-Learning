user_dictionary = {
    'First_name' : 'Ravi' ,
    'Last_name'  : 'Gaygol',
    'Birth_year' : 1997
}

contacts = {
    'Ravi' : ['12345'],
    'Nitin': '78945'
}

print('78945' in contacts.values())

print('.' * 90)
#*************************************************************************
#loops
for x, y in user_dictionary.items():
    print(x,':',y)

for number in contacts['Ravi']:
    print(f'Phone :{number}')

for contact in contacts:
    print("The Number of {0} is {1}".format(contact, contacts[contact]))  

for person, phone_number in contacts.items():
    print("The contact number of {0} is {1}".format(person, phone_number))
print('.' * 90)
#*************************************************************************
#if statement

if 'Birth_year' in user_dictionary:
    print('yes birth year exist in the dictionary')    


if 'Ravi' in contacts.keys():
    print("Ravi's contact number = {}".format(contacts['Ravi'][0]))

print('.' * 90)
#*************************************************************************
#copy one dictionary to another one without using copy method
#in these same memory reference get share for both dictionaries
user_dictionary2 = user_dictionary
print(f'before remove user disctionary one : {user_dictionary}')
print(f'before remove user disctionary two : {user_dictionary2}')   

print('.' * 90)
user_dictionary2.popitem()
print(f'after remove user disctionary one : {user_dictionary}')
print(f'after remove user disctionary two : {user_dictionary2}')   

print('.' * 90)
#copy one dictionary to another one by using copy method
#in these copy method the different memory reference get created for second dictionary so
#when we remove anything from first dict it does not affect to first dict

user_dictionary3 = user_dictionary.copy()
print(f'before remove user disctionary one : {user_dictionary}')
print(f'before remove user disctionary three : {user_dictionary3}')   

print('.' * 90)
user_dictionary3.popitem()
print(f'after remove user disctionary one : {user_dictionary}')
print(f'after remove user disctionary three : {user_dictionary3}') 
