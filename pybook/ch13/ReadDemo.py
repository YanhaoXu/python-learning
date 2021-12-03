TEST_PATH = "D:\\DevOps\\testData\\python\\pybook\\ch13\\"


def main():
    # Open file for input
    infile = open(TEST_PATH + "Presidents.txt", "r")
    print("(1) Using read(): ")
    print(infile.read())
    infile.close()  # Close the input file


main()  # Call the main function
