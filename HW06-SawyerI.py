# Isaac Sawyer - 10/02/2022
# HW06
# To Calculate Rental Car Transaction

# Declare variables

Compact = "Compact"
Standard = "Standard"
Suv = "SUV"
Van = "Van"
CarType = ""
CustomerName = ""
TotalChrg = 0
DaysRented = 0
DailyChrg = 0

# Declare constants

BASE_CHRG = 65
STANDARD_CHRG = 10
SUV_CHRG = 15
VAN_CHRG = 25
DISCOUNT = 0.2

# Prompt user for inputs regarding transaction

CustomerName = (input("Enter customer name: "))
CarType = (input("Enter car type (Compact, Standard, SUV, Van): "))
DaysRented = int(input("Enter days of rental: "))

# Stacked if statements to evaluate car type, days rented, and corresponding charges

if CarType == Compact:
    TotalChrg = BASE_CHRG

if CarType == Standard:
    DailyChrg = STANDARD_CHRG
    TotalChrg = (BASE_CHRG + (DailyChrg * DaysRented))
    
if CarType == Suv:
    DailyChrg = SUV_CHRG
    TotalChrg = (BASE_CHRG + (DailyChrg * DaysRented))

if CarType == Van:
    DailyChrg = VAN_CHRG
    TotalChrg = (BASE_CHRG + (DailyChrg * DaysRented))
    
if DaysRented > 7:
    TotalChrg = TotalChrg - ((BASE_CHRG + (DailyChrg * DaysRented)) * DISCOUNT)
     
# Diplay transaction details to user

print(str(CustomerName) + " rented " + (CarType) + " for " + str(DaysRented) + " days ")
print("The total charge for " + str(CustomerName) + " is: $" + str(TotalChrg))
