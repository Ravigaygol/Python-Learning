#write the program that print the number 1-50 
#but for multiple of 3 print 'Fizz
#instead of the number and for the multiple of five print 'Buzz
# for the numbers which are multiple of both three and five print 'FizzBuzz

for number in range (1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number & 5 == 0:
        print('Buzz')
    else:
        print(number)             