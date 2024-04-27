# Weekly Task 7
# Author: Myles Henehan
# Instructions: Program should read in a text file and output the number of instances of the letter "E" it contains

import sys 
# From reading the RealPython website, I can see that we need to use the sys module in Python to access command-line arguments (Ndlovu, 2019).

FILENAME = sys.argv[1]
# For this, I am using a file called moby-dick.txt, which contains randomly generated text from ChatGPT.

# From my understanding, this function treats any arguments separated by spaces after the command "Python" in the command line as list items.
# The 1 here denotes the second list item (since lists start from 0).
# Interestingly, if we use 0, the program will print itself out, since this is the first list item.


# Let's first just create a function to read this file and print out its contents:

def readtext():
    try:
        with open(FILENAME) as f:
            text = f.read()
        return (text)
# This part of the function opens, reads and returns the file as the variable "text".
    except FileNotFoundError:
        print("Error: Please enter an existing file to read")
        sys.exit(1)
# I have also added an exception in case the file cannot be found, in which case the program will be terminated.
        

# Let's test this function by asking the program to print out the contents of the txt file:
filecontents = readtext()
print(f"The file reads as follows: {filecontents}", end="")


# Now we want to calculate how many times the letter E appears in the file, so we can create another function:

def countletter(FILENAME, e):
    count = 0
# In this function, the count starts at 0. We will get it to open the file and check each character in each line. If the character is E, it will add to the count.
    with open (FILENAME) as f:
        for line in f:
            for char in line:
                if char == "e":
                    count = count + 1
                elif char == "E":
                    count = count + 1 
#iterates until the whole file has been read. We want to account for both capital and lower-case E.
    return count

# the final count is the return of this function:
finalcount = countletter(FILENAME, "e")

#depending on how many times E appears, we may want to print out a different output
if finalcount == 0:
    print(f"The letter E does not appear in this file.")
elif finalcount == 1:
    print(f"The letter E appears once in this file.")
else:
    print(f"The letter E appears {finalcount} times in this file.")

