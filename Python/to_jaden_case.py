# This funciton takes in a multi-word string that is lower case and capitalizes the first letter
# of each of the words in the string. More easily readable code than the other 2 solutions listed.
def toJadenCase(string):
    return ' '.join(map(str, list(map(lambda x: x.capitalize(), string.split(' ')))))


# Alternative option. Cleaner code, but requires an import.
# 
# import string
# def toJadenCase(stringy):
#     return string.capwords(stringy)


# Second alternative, very concise code, most difficult to read and understand.
# 
# from string import capwords as toJadenCase


# SAMPLE TESTS  
assert toJadenCase("hello my name is jaden") == "Hello My Name Is Jaden"
assert toJadenCase("how can mirrors be real if our eyes aren't real") == "How Can Mirrors Be Real If Our Eyes Aren't Real"
assert toJadenCase("the moment that truth is organized it becomes a lie") == "The Moment That Truth Is Organized It Becomes A Lie"
assert toJadenCase("just stare in the mirror and cry and you'll be good") == "Just Stare In The Mirror And Cry And You'll Be Good"