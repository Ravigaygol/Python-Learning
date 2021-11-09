#factorial program without using recursion

def factorial(x):
    y = 1
    while x > 0:
        y *= x
        x -= 1
    return y
factorial_result = factorial(5)
print(factorial_result)

print('*' *98)
#---------------------------------------------------------
#factorial program by using recursive method

def factorial(x):
    if x == 1:
        return 1
    else:
        print(x)
        return x * factorial(x - 1)

factorial_result = factorial(5)
print(factorial_result)


print('*' *98)
#---------------------------------------------------------
#fibonacci program by using recursive method

def feb_seq(amount):
    if(amount == 0):
        return 0
    elif(amount == 1):
        return 1
    else:
        return feb_seq(amount - 2) + feb_seq(amount - 1)

for x in range(13):
    print(feb_seq(x))

