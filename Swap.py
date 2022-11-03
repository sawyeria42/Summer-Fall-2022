# Swap.py - This program determines the minimum and maximum
# of three values input by the user and performs necessary swaps.  
# Input: Three int values. 
# Output: The numbers in numerical order.

first = 0
second = 0
third = 0

# Prompt user for input
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

# Test to see if the first number is greater than the second number
if first > second:
    temp = second
    second = first
    first = temp

# Test to see if the second number is greater than the third number
if second > third:
    temp = third
    third = second
    second = temp

# Test to see if the first number is greater than the second number again
if first > second:
    temp = second
    second = first
    first = temp

# Print numbers in numerical order
print("Smallest: " + str(first))
print("Next smallest: " + str(second))
print("Largest: " + str(third))
