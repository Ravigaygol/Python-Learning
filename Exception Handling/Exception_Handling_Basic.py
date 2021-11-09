#Errors and Exceptions (Try/Catch)
#1
try:
    #x = 10 *(1/0)
    x = '2' + 2
    print(x)
except ZeroDivisionError as e:
    print(f'{e} Cannot divide by Zero.!')

except TypeError as e:
    print(f'{e} : Cannot add string to int')

except Exception as e:
    print(f'{e} : Parent Exception')

finally:
    print('In the finally block....!')

print('*' * 98)

#2

try:
    x = None
    if x is None:
        raise Exception
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print('X is none couuld not find answer.....!')
finally:
    print("In the FINALLY Block...!")        


print('*' * 98)
#3

try:
    gateway = 'Gateway : Opened'
    print(gateway)
    x = 2 + '2'
except TypeError as e:
    print('ERROR : Must convert string to int...!')
finally:
    gateway = 'Gateway : Closed'
    print(gateway)        
