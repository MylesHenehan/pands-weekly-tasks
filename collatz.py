# Program that asks the user to input any positive integer and outputs the successive values of the following calculation: 
# if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1
# this should stop when it reaches 1

# Author: Myles Henehan

startinginteger = int(input("Please enter any integer: "))

while startinginteger != 1:
    print(startinginteger)
    if startinginteger % 2 == 0:
        startinginteger = startinginteger // 2
    else:
        startinginteger = (startinginteger * 3) +1

print(startinginteger)