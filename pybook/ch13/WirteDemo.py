TEST_PATH = "D:\\DevOps\\testData\\python\\pybook\\ch13\\"


def main():
    # Open file the output
    outfile = open(TEST_PATH + "Presidents.txt", "w")

    # Write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")

    outfile.close()  # Close the output file


main()  # Call the main function
