import random

# Generate random numbers
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(num1) + " + " + str(num2) + "? "))

# Display result
print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)
