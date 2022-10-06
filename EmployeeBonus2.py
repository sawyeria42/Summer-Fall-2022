# EmployeeBonus2.py - This program calculates an employee's yearly bonus.

# Declare and initialize variables here
BONUS_1 = 0.25
BONUS_2 = 0.15
BONUS_3 = 0.1
NO_BONUS = 0

RATING_1 = 1
RATING_2 = 2
RATING_3 = 3

employeeFirstName = input("Enter employee's first name: ")
employeeLastName = input("Enter employee's last name: ")
employeeSalary = float(input("Enter the employee's yearly salary: "))
employeeRating = int(input("Enter employee's performance rating: "))

# Write your code here
if employeeRating == 1:
    bonus = BONUS_1 * employeeSalary
elif employeeRating == 2:
    bonus = BONUS_2 * employeeSalary
elif employeeRating == 3:
    bonus = BONUS_3 * employeeSalary
else: bonus = NO_BONUS * employeeSalary

# Output bonus here
print("Employee Name: " + employeeFirstName + " " + employeeLastName)
print("Employee Bonus: $" + str(bonus))
