#Create a new dictionary called vehicle holding the keys :
#model, make, year, and mileage
#fill in the values of your choice

vehicle = {
    'model' : 'accord',
    'make' : 'Honda',
    'year' : 2016,
    'mileage' : 80000
}

print('.' * 90)
#print the year of vehicle
print(vehicle['year'])


print('.' * 90)
#change the year to different year
vehicle['year'] = 2018
print(vehicle['year'])

print('.' * 90)
#Add a new key called type,
#fill in the value(car, truck etc)
vehicle['type'] = 'car'
print(vehicle)


print('.' * 90)
#Remove the make key and value
vehicle.pop('make')
print(vehicle)

print('.' * 90)
#print the dictionary
print(vehicle)