#Create two new functions
# 1- function that convert Fahrenheit degrees to Celsius
# 2- function that convert Celsius to Fahrenheit

#Fahrenheit to celsius Formula:
# (Fahrenheit - 32)*5/9 = Celsius or first subtract 32, then multiple by , then divide by 9.

#Celsius to Fahrenheit Formula:
# (Celsius * 9/5) + 32 = Fahrenheit or multiple by 9,then divide by 5, then add 32.

#Print results from both functions working correctly.


def fahrenheit_to_celsius_converter(f_degree):
    c_degree = (f_degree - 32) * 5.0 / 9.0
    return c_degree

def celsius_to_fahrenheit_converter(c_degree):
    f_degree = 9.0 / 5.0 * c_degree + 32
    return f_degree

print(fahrenheit_to_celsius_converter(81))
print(celsius_to_fahrenheit_converter(10))