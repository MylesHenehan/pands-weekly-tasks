# Weekly Task 2
# Author: Myles Henehan 
# Instructions: Program should prompt the user to read in 2 values in cents. Program should then add these values together and output the total value in Euros and cents (€x.xx)

amountone = int(input("Please enter an amount in cent: "))
# User is prompted to input their first integer in cents.
amounttwo = int(input("Please enter another amount in cent: "))
# User is prompted to input a second integer in cents.
# In both cases, we use int() to convert the inputs straight to integers.

sum = amountone + amounttwo
# We then add these integers together and call it the sum - this will be the total number of cents.

# Since we have to be conscious of the inaccuracy of floats, we now want to split what comes before and after the decimal point.

euro = sum // 100
# We can get the euro amount by dividing by 100 (without remainder)
cents = sum % 100
# Then we get the cents by getting the remainder.

# Coming back to this, I can see an issue here. If the value after the decimal is less than 10 cent, we are going to get the wrong answer.
# Eg. If we add 102 cents and 100 cents, the output is going to be €2.2 instead of €2.02.
# There may be a more efficient way, which we would need for bigger programs, but for the sake of this task, I will use the following solution:

if cents < 10:
    cents = f'0{cents}'

# As written above, I've written an if statement so that if the cents value is less than 10, we add a 0 to the start, essentially converting it into a string.

print(f"The total sum is €{euro}.{cents}")
# Now we can print the correct total.
