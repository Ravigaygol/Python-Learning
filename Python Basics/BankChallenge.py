# Create a variable "bank_amount" asign to the value of 100

# Create 3 more variables : item_one = 25
#                           item_two = 30
#                           item_three = 15
# -Subtract each item from bank_amount
# -Print how much is left at the bank account at the end
# -write a comment at the top explaining what your application does
# 
# 

bank_amount = 100

item_one = 25
item_two = 30
item_three = 15

bank_amount = bank_amount - item_one
bank_amount -= item_two
bank_amount -= item_three

print('At the end remaining bank amount = {0}'.format(bank_amount))

