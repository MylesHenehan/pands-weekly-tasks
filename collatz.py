# Program that asks the user to input any positive integer and outputs the successive values of the following calculation.

# Author: Myles Henehan

numbers = []
startinginteger = int(input("Please enter any integer: "))


while startinginteger != 1:
    if (startinginteger % 2) == 0:
       numbers.append(startinginteger)
       numbers = numbers / 2
    print(numbers)

print("end of program")