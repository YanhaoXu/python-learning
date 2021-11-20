# Prompt the user for input
purchaseAmount = eval(input("Enter purchase amount: "))

# Compute sales tax
tax = purchaseAmount * 0.06

# Display tax amount with digits after decimal point
print("Sales tax is", int(tax * 100) / 100.0)
