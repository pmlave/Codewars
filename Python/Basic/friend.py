# Simple function takes in a list and returns all elements with length less than 4.
def friend(x):
    return [name for name in x if len(name) <= 4]


# One alternative, using filter instead of list comprehension.
# def friend(x):
#     return list(filter(lambda y: len(y) == 4, x))


# SAMPLE TESTS
assert friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
assert friend(["Constance", "Philip", "Gary",]) == ["Gary"]
assert friend(["Harriet", "William", "Ed", "Jim", "Frank"]) == ["Ed", "Jim"]
assert friend(["Bob", "Cassandra", "Karl", "Paula"]) == ["Bob", "Karl"]