# Weekly Task 6
# Author: Myles Henehan
# Instructions: Program should take a positive floating-point number as input and output an approximation of its square root, using Newton's Method.


def sqrt(startingnum, tolerance=1e-6): 
# We start by defining a function to do this. According to Pandy(2024), this is an appropriate tolerance level for Newton's method.
    
    guess = startingnum/2
# We need to guess any positive number, so let's start with half of the input
    
    while True:
        newguess = 0.5 * (guess + startingnum / guess)  
# We do an iteration of Newton's method within a while loop
        if abs(newguess - guess) <= tolerance:
            break
# We want the loop to stop if we meet the tolerance level
        guess = newguess 
# Otherwise, we update the guess for the next iteration

    return guess 
# If the loop stops, it means we've got quite an accurate guess, so we want that guess to be returned.

# Now we have our function, we can run the main part of the code:

startingnum = float(input("Please enter a positive float: "))
# We start by asking the user to input a float. If they insert an integer, it will be converted to a float.

if startingnum <= 0:
        raise ValueError("Please enter a positive value")
# The instructions specify it must be a positive float, so we raise an error if it isn't.

answer = sqrt(startingnum)
# Now we can use our pre-made function to get the answer.

print(f'The square root of {startingnum} is {answer}')


# Reference: Pandy, H. (2024). "Newton Raphson method in Python". Last Updated 16 April 2024. Available at: https://flexiple.com/python/newton-raphson-method-python.

