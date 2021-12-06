def main():
    index = eval(input("Enter an index for a Fibonacci number: "))
    # Find and display the Fibonacci number
    print("The Fibonacci number at index", index, "is", fib(index))


# The function for finding the Fibonacci number
def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


main()  # Call the main function
