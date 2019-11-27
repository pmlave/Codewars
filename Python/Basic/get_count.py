# Simple function takes an input string and returns a count of how many vowels are in the string.
def getCount(inputStr):
    vowel_str = "aeiou"
    return len([each for each in inputStr if each in vowel_str])