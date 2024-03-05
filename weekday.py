# Program that runs and tells you whether or not it's a weekday
# Author: Myles Henehan

import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")