# Declare a named constant for array size here.
MAX_AVERAGES = 8

# Declare array here.
averages = []

# Write a loop to get batting averages from user
# and assign to array.
for i in range(MAX_AVERAGES):
    averageString = input("Enter a batting average: ")
    battingAverage = float(averageString)
    # Assign value to array.
    averages.append(battingAverage)

# Assign the first element in the array to be the
# minimum and the maximum.
minAverage = averages[0]
maxAverage = averages[0]

# Start out your total with the value of the
# first element in the array.
total = 0

# Write a loop here to access array values
# starting with averages[1]
for i in range(MAX_AVERAGES):
    # Within the loop test for minimum and 
    # maximum batting averages.
    if averages[i] < minAverage:
        minAverage = averages[i]

    if averages[i] > maxAverage:
        maxAverage = averages[i]
    # Also accumulate a total of all batting averages.   
    total = total + averages[i]

# Calculate the average of the 8 batting averages.
average = total / MAX_AVERAGES

# Print the batting averages stored in the averages array.
print("Minimum batting average is " + str(minAverage))
print("Maximum batting average is " + str(maxAverage))

# Print the maximum batting average, minimum batting average, and average batting average.
print("Average batting average is " + str(average))
