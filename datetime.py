from _datetime import datetime, time, date, timedelta

# datetime is for specific instances, date is what just what date it is,
# and time is just the time regardless of the date
today = date.today()
print(today)
# prints current date

tomorrow = date(2024, 8, 5)
print(tomorrow)
# you can print the date as an object with date constructor

next_week = date.fromisoformat('2024-08-11')
print(next_week)
# you can parse a date from a string as well
# iso format is year-month-day, widely used standard format

right_now = datetime.now()
print(right_now)
# to get timestamps, you would use datetime to
# get the exact time of the occurrence
print(right_now.timestamp())
# to get an exact timestamp, do '.timestamp' and it will
# print the exact number of seconds since January 1st, 1970.
my_date = datetime.fromtimestamp(1700000000)
print(my_date)
# can also get a readable date from an exact timestamp like this

