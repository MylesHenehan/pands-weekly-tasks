# Program reads in a 10 digit account number
# Program then outputs that number again but with only the last 4 digits visible (first 6 denoted by X)

#Author: Myles Henehan

accountnumber = input("Please enter your 10 digit account number: ")
lastfourdigits = accountnumber[6:10]
print(f"Account Number: XXXXXX{lastfourdigits}")

# If we were to modify the program to allow for numbers of any length, we would need to know the length of the account number before printing.
# By using length -4 to length as the range, we can still make sure there are 4 digits at the end.
# However, we will also need to ensure that the number of Xs is correct, so we should add a value Xnumber which multiplies X by the number of digits in the account number

accountnumber = input("Please enter your account number: ")
lastdigit = len(accountnumber)
firstdigit = lastdigit - 4

Xnumber = firstdigit * "X"
lastfourdigits = accountnumber[firstdigit:lastdigit]

print(f"Account Number: {Xnumber}{lastfourdigits}")