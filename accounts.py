# Program reads in a 10 digit account number
# Program then outputs that number again but with only the last 4 digits visible (first 6 denoted by X)

#Author: Myles Henehan

accountnumber = input("Please enter your 10 digit account number: ")
lastfourdigits = accountnumber[6:10]
print(f"Account Number: XXXXXX{lastfourdigits}")