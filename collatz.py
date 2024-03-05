# Program that asks the user to input any positive integer and outputs the successive values of the following calculation: if it is even, divide it by two, but if it is odd, multiply it by three and add one

# Author: Myles Henehan

numbers = []
startinginteger = int(input("Please enter any integer: "))

while startinginteger != 1:
    numbers = numbers.append(startinginteger)

print(numbers)