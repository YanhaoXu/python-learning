# Receive an input
num = eval(input("Enter an integer: "))

if num % 2 == 0 and num % 3 == 0:
    print(num, "is divisible by 2 and 3")

if num % 2 == 0 or num % 3 == 0:
    print(num, "is divisible by 2 or 3")

if (num % 2 == 0 or num % 3 == 0) and \
        not (num % 2 == 0 and num % 3 == 0):
    print(num, "is divisible by 2 or 3, but not both")
