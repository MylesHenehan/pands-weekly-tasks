# Weekly Task 5
# Author: Myles Henehan
# Instructions: Program should run and tell you whether or not it's a weekday.

import datetime
# For this, we need the module datetime (according to W3Schools)

currentdate = datetime.datetime.today()
# We first use this function to get today's date

dayofweek = currentdate.weekday()
# Then we use the .weekday function to get an integer that represents the day of the week, where Monday is 0 and Sunday is 6.

# Coming back to this at a later date, let's use a dictionary to let the program know what each day is assigned to.

daysoftheweek = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

today = daysoftheweek[dayofweek]
print(f'Today is {today}')
# We retrieve the correct day from the dictionary and print it.

if dayofweek <= 4:
    print("Unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")
# Depending on whether or not it's the weekend, the program will send a different message.


# Source: W3Schools: https://www.w3schools.com/python/python_datetime.asp). 
# Note: On this website, it says that Sunday is 0 in the weekday function. But when testing, this appears not to be the case.