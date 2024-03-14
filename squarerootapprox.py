# Program that takes a positive floating-point number as input and outputs an approximation of its square root.

# Author: Myles Henehan


def sqrtof(startingnum, tolerance=1e-6): #according to documentation, this is an appropriate tolerance level for Newton's method
    if startingnum <= 0:
        raise ValueError("Please enter a positive value") # the instructions specify it must be a positive number
    
    guess = startingnum/2 # we need to guess any positive number, so let's start with half of the input
    
    while True:
        newguess = 0.5 * (guess + startingnum / guess)  # iteration of Newton's method
        if abs(newguess - guess) <= tolerance:
            break # we want the loop to stop if we meet the tolerance level
        guess = newguess  # otherwise, we update the guess for the next iteration

    return guess #if the loop stops, it means we've got quite an accurate guess, so we want that guess to be returned.


startingnum = float(input("Please enter a starting number: "))
print(sqrtof(startingnum))

#Note: Instructions for this task state "You should create a function called <tt>sqrt</tt> that does this", but python won't accept this as a function name.

