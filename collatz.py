# Weekly Task 4
# Author: Myles Henehan
# Instructions: Program should ask the user to input any positive integer and output the successive values of the following calculation: 
# if it is even, divide it by 2, but if it is odd, multiply it by 3 and add 1.
# this should stop when it reaches 1

startinginteger = int(input("Please enter any integer: "))
# The user inputs a number and we convert it to an integer.

while startinginteger != 1:
# We use a while loop here to make sure that once the output reaches 1, the program stops.
    print(startinginteger)
# We start by printing the inputted number. We want it to keep printing the new number so long as we are inside the while loop.
    if startinginteger % 2 == 0:
# if the remainder of the integer is zero after being divided by 2, this means it's even.
        startinginteger = startinginteger // 2
# in this case, we want to divide it by 2
    else:
        startinginteger = (startinginteger * 3) + 1
# if the integer is odd, we want to multiply it by 3 and add 1