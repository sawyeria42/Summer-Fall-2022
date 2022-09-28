salary = float(input("Enter Salary:"))
numDependents = float(input("Enter number of dependents:"))
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding




# Calculate stateTax here.

print("State Tax: $" + str(stateTax))

# Calculate federalTax here.

print("Federal Tax: $" + str(federalTax))

# Calculate dependantDeduction here.

print("Dependents: $" + str(dependentDeduction))

# Calculate totalWithholding here.

# Calculate takeHomePay here.

print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
