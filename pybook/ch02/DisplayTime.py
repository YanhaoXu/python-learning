# Prompt the user for input
seconds = eval(input("Enter an integer for seconds: "))
# Get minutes and remaining seconds
minutes = seconds // 60
remainingSeconds = seconds % 60
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")
