import RandomCharacter

NUMBER_OF_CHARS = 175  # Number of characters to generate
CHARS_PRE_LINE = 25  # Number of characters to display per line

# Print random characters between 'a' and 'z', 25 chars per line
for i in range(NUMBER_OF_CHARS):
    print(RandomCharacter.getRandowLowerCaseLetter(), end="")
    if (i + 1) % CHARS_PRE_LINE == 0:
        print()
