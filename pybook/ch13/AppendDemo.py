from pybook.ch13.FIleTestConst import TEST_PATH


def main():
    # Open file for appending data
    fileName = TEST_PATH + "Info.txt"
    outfile = open(fileName, "a")
    outfile.write("\nPython is interpreted\n")
    outfile.close()  # Close the file


main()  # Call the main function
