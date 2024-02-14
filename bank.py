# Program prompts the user to read in 2 values in cents
# Program then adds these values together and outputs the total value in Euros and cents (€x.xx)

#Author: Myles Henehan

amountone = int(input("Please enter an amount in cent: "))
amounttwo = int(input("Please enter another amount in cent: "))
sum = amountone + amounttwo
euro = sum // 100
print(f"The total sum is €{sum // 100}.{sum % 100}")