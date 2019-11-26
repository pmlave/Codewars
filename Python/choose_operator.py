# Simple function takes arguments and completes the operation based on the operator given.
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


# Option instead using ternary operators.
# def basic_op(operator, value1, value2):
    # return value1 + value2 if operator == '+' else value1 - value2 if operator == '-' else value1 * value2 if operator == '*' else value1 / value2


# SAMPLE TESTS
assert basic_op('+', 4, 7) == 11
assert basic_op('-', 15, 18) == -3
assert basic_op('*', 5, 5) == 25
assert basic_op('/', 49, 7) == 7