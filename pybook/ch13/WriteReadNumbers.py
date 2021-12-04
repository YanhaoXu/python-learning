from random import randint

from pybook.ch13.FIleTestConst import TEST_PATH


def main():
    # Open file for writing data
    fileName = TEST_PATH + "Numbers.txt"
    outfile = open(fileName, "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close()  # Close the file

    # Open file for reading data
    infile = open(fileName, "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for num in numbers:
        print(num, end=' ')
    infile.close()  # Close the file


main()  # Call the main method
