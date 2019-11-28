# Simple function returns the unique characters from two passed in strings.
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))
