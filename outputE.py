# Program that reads in a text file and outputs the number of e's it contains
# Author: Myles Henehan

import sys # From research, I can see that we need to use the sys module in Python to access command-line arguments

FILENAME = sys.argv[1]

# From my understanding, this function treats any arguments separated by spaces in the command line as list items.
# The 1 here denotes the second list item (since lists start from 0).
# Interestingly, if we use 0, the program will print itself out.

# Moving on...

# Let's first just create a function to read this file and print out its contents

def readtext():
    try:
        with open(FILENAME) as f:
            text = f.read()
        return (text)
    except FileNotFoundError:
        print("Error: Please enter an existing file to read")
        sys.exit(1)
        

# Test
filecontents = readtext()
print(f"The file reads as follows: {filecontents}", end="")


# Now we want to calculate how many times the letter E appears in the file, so we can create another function.

def countletter(FILENAME, e):
    count = 0
    with open (FILENAME) as f:
        for line in f:
            for char in line:
                if char == "e":
                    count = count + 1
    return count

# let's say that the final count is the return of this function
finalcount = countletter(FILENAME, "e")

#depending on how many times E appears, we may want to print out a different output
if finalcount == 0:
    print(f"The letter E does not appear in this file.")
elif finalcount == 1:
    print(f"The letter E appears once in this file.")
else:
    print(f"The letter E appears {finalcount} times in this file.")
