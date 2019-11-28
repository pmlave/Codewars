# Simple function takes 3 input numbers and returns true if the first number is divisible by both
# of the second two numbers; false otherwise.
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0