# even_or_odd takes in a number and evaluates if it is even or odd, returning the result.
def even_or_odd(number):
    return "Odd" if number % 2 else "Even"

# SAMPLE TESTS
assert even_or_odd(-1) ==  "Odd"
assert even_or_odd(10) == "Even"
assert even_or_odd(73) == "Odd"
assert even_or_odd(140) == "Even"
