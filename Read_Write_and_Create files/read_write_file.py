#Different File MODES -
#       Mode                    Discription
#       r          -            Open for reading
#       w          -            Open for writing
#       x          -            Create new file and open it for writing
#       a          -            open for writing, appending to file
#       +          -            open file for updating(read/ write)
#       b          -            binary mode
#       t          -            text mode

# Reading a text file

from os import write


print('*' *98)

f = open('/home/rgaygol/Documents/Python Learning/Read_Write_and_Create files/text.txt','r')
print(f.read())

#Must close or it may leads to memory leak
f.close()

print('*' *98)
#****************************************************************************
# By using CONTEXT MANAGER - it will open and close the file automatically

with open('/home/rgaygol/Documents/Python Learning/Read_Write_and_Create files/text.txt','r') as f:
    #print(f.read())
       #readline will read first line of that file
    #print(f.readline())
     #reading the file by using for loop
    for line in f:
        print(line, end= '')

    print('.'*98)    
    #to getting the exact written value at mentioned placed
    print(f.read(10))
          
print('*' *98)
#****************************************************************************   
#Reading the photos - we use rb as read binary
with open('/home/rgaygol/Documents/Python Learning/Read_Write_and_Create files/Happy Diwali.png', 'rb') as f:
    print(f.read())

print('*' *98)
#**************************************************************************** 
#*************************************************************************************
#*************************************************************************************
#*************************************************************************************
#*************************************************************************************
#*******************************CREATE AND WRITE THE FILE*****************************
#*************************************************************************************
#*************************************************************************************
#*************************************************************************************

print('*' * 98)
#If the file exist it will overwrite the file
#If the file does not exist, It will create a new file

with open('/home/rgaygol/Documents/Python Learning/Read_Write_and_Create files/text2.txt', 'w') as f:
    f.write('I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed.\
     I’ve failed over and over and over again in my life and that is why I succeed.')

#*************************************************************************************

print('*' * 98)

#Mimic another file

with open('/home/rgaygol/Documents/Python Learning/Read_Write_and_Create files/text.txt', 'r') as read_file:
    with open('/home/rgaygol/Documents/Python Learning/Read_Write_and_Create files/text2.txt','w') as write_file:
        write_file.write(read_file.read()) 
