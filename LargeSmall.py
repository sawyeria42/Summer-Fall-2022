# LargeSmall.py - This program calculates the largest
# and smallest of three integer values. 
# Declare and initialize variables here

largest = None
smallest = None

# Prompt the user to enter 3 integer values

int1 = int(input("Enter integer one"))
int2 = int(input("Enter integer two"))
int3 = int(input("Enter integer three"))

# Write assignments, and necessary if else statements
# here as appropriate

if int1 > int2 and int3:
    largest = int1
if int2 > int1 and int3:
    largest = int2
if int3 > int1 and int2:
    largest = int3
    
if int1 < int2 and int3:
    smallest = int1
if int2 < int1 and int3:
    smallest = int2
if int3 < int1 and int2:
    smallest = int3

# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))
