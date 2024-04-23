# Program prompts the user to read in 2 values in cents
# Program then adds these values together and outputs the total value in Euros and cents (€x.xx)

#Author: Myles Henehan

amountone = int(input("Please enter an amount in cent: "))
# User is prompted to input their first integer
amounttwo = int(input("Please enter another amount in cent: "))
# User is prompted to input a second integer
sum = amountone + amounttwo
# Program then adds these integers together and calls it the sum - this will be the total number of cents.
# Since we have to be conscious of the inaccuracy of floats, we now want to split what comes before and after the decimal point.
euro = sum // 100
# We can get the euro amount by dividing by 100 (without remainder)
cents = sum % 100
# Then we get the cents by getting the remainder.

print(f"The total sum is €{euro}.{cents}")


#Note to self: Could there be a more simple way using 10 to the power?