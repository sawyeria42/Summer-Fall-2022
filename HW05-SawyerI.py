# Isaac Sawyer - 09/28/2022
# HW05
# Guessing a number between 1 and 100

# Declare correct number constant and user's variable input
CORRECT_NUM = 23
GuessNum = int(input("Guess a number between 1 and 100: "))

# Evaluate whether or not number is guessed correctly
while GuessNum != CORRECT_NUM:
    
    if GuessNum > CORRECT_NUM:
        print("Too high!")
        GuessNum = int(input("Guess a number between 1 and 100: "))
        
    else:
        print("Too low")
        GuessNum = int(input("Guess a number between 1 and 100: "))

# Display correctly guessed number message    
print("You are correct! The number is " + str(CORRECT_NUM))