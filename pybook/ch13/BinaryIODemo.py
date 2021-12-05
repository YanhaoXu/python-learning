import pickle

from pybook.ch13.FIleTestConst import TEST_PATH


def main():
    # Open file for writing binary
    outfilename = TEST_PATH + "pickle.dat"
    outfile = open(outfilename, "wb")
    pickle.dump(45, outfile)
    pickle.dump(56.6, outfile)
    pickle.dump("Programming is fun", outfile)
    pickle.dump([1, 2, 3, 4], outfile)
    outfile.close()  # Close the output file

    # Open file for reading binary
    infile = open(outfilename, "rb")
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    infile.close()  # Close the input file


main()  # Call the main function
