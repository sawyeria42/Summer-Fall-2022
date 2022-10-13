"""
LeftOrRight.py - This program calculates the total number of 
left-handed and right-handed students in a class.

Input:  L for left-handed; R for right handed; X to quit.
Output: Prints the number of left-handed students and the number
of right-handed students.
"""

rightTotal = 0  # Number of right-handed students.
leftTotal = 0  # Number of left-handed students.
leftOrRight = "R"

# Write your loop here.
while (leftOrRight == "L") or (leftOrRight == "R"):
    leftOrRight = input("Enter an L if you are left-handed,a R if you are right-handed or X to quit.")
    if leftOrRight  == "L":
        leftTotal = leftTotal + 1
    elif leftOrRight == "R":
        rightTotal = rightTotal + 1

# Output number of left or right-handed students.
print("Number of left-handed students: " + str(leftTotal))
print("Number of right-handed students: " + str(rightTotal))
