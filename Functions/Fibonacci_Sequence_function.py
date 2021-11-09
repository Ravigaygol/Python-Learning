#Fibonacci sequence is the series of numbers:
# 0,1,1,2,3,5,8,13,21,34,.....

#next number is found by adding up the two numbers before it.

def fib_sequence(amount):
    n1 = 0
    n2 = 1
    if(amount <= 0):
        print('Please change to a positive integer')
    elif(amount == 1):
        print('Feb Seq:')
        print(n1)
    else:
        print('feb Seq:')
        count = 0
        while count < amount:
            print(n1)
            feb_sum = n1 + n2
            n1 = n2
            n2 = feb_sum
            count += 1
        
#fib_sequence(input('Enter the febonacci sequence you want to print...!'))
sequence = int(input('Enter the febonacci terms you want to print...!'))
fib_sequence(sequence)

#-----------------------------------------------------------------------------
print('*' *98)
#Fibonacci program without using function:

nTerms = int(input('How many terms you want ???'))
#first two terms
n1 = 0
n2 = 1
count = 2
#check if the number of terms is valid
if nTerms <= 0:
    print('Please enter the positive integer')
elif (nTerms == 1):
    print('Fibonacci Sequence :')
    print(n1)
else:
    print('fibonacci Sequence :')
    print(n1 ,',', n2, end=',  ')
    while count < nTerms:
        sum = n1 + n2
        print(sum, end=',  ')
        #update values
        n1 = n2
        n2 = sum
        count += 1        