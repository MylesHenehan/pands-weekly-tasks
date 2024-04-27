# Weekly Task 3
# Author: Myles Henehan
# Instructions: Create a program reads in a 10 digit account number. This program should then output that number again but with only the last 4 digits visible (first 6 denoted by X).


accountnumber = input("Please enter your 10 digit account number: ")
#First, we ask the user to input a 10 digit number.

if len(accountnumber) != 10:
        raise ValueError("Invalid input. Account number must be exactly 10 digits.")
# Coming back to this, I decided to add some code to give an error message if the user did not enter a 10 digit number.

lastfourdigits = accountnumber[6:10]
#Then we work out the last 4 digits of this account number, so that we only print these.

print(f"Account Number: XXXXXX{lastfourdigits}")
# Now we can print 6 Xs, followed by the last 4 digits.

#EXTRA:
# If we were to modify the program to allow for numbers of any length, we would need to know the length of the account number before printing.
# By using length - 4 to length as the index range, we can still make sure there are 4 digits at the end.
# However, we will also need to ensure that the number of Xs is correct, so we should define a value Xnumber which multiplies X by the number of digits in the account number

accountnumber = input("Please enter your account number: ")
#The user enter their account nunber again
numlength = len(accountnumber)
#We found out how how many digits are in the input.
startingnum = numlength - 4
# Then we get the index of the 4th last number.

Xnumber = startingnum * "X"
# We know that everything up to the startingnum should be hidden as "X" so we multiply the number of digits by X to get our "Xnumber"
lastfourdigits = accountnumber[startingnum:numlength]
# Now we get the last 4 digits using the index range from startingnum to numlength.

print(f"Account Number: {Xnumber}{lastfourdigits}")
# We then print both together.