import datetime

today = datetime.date.today()
print(today)

#********************************************************
print(today.year)
print(today.day)
print(today.month)
print(today.weekday())
print(today.isoweekday())

print('*' *98)
#********************************************************
#how close are we to end this year??

new_year = datetime.date(2022, 1, 1)

days_remaining = new_year - today
print(days_remaining) 

#********************************************************
print('*' *98)
#Working with time
#                   (HR : MIN : SEC : MILISEC)
time = datetime.time(1, 2, 45,100)
print(time)

date_time = datetime.datetime(2021, 11, 6, 12, 44, 12, 100)
print(date_time)

#********************************************************
print('*' *98)

#Move forward with time delta

time_delta = datetime.timedelta(days = 20)
print(date_time + time_delta)

#********************************************************
print('*' *98)
#convert string date to date object

date_string = '2021-11-06'
print(date_string)
date_object = datetime.date.fromisoformat(date_string)
print(date_object)