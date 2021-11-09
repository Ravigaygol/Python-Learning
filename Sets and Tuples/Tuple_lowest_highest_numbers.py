def high_and_low(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)

lottery_numbers = [15,123,10,5,120,3,5]
(highest_number, lowest_number) = high_and_low(lottery_numbers)
print(highest_number)
print(lowest_number)