import unittest
from squares_needed import squares_needed
from get_count import getCount
from longest import longest
from is_divisible import is_divisible
from find_uniq import find_uniq

class test_basic(unittest.TestCase):
    def test_squares_needed(self):
        self.assertEqual(squares_needed(0), 0)
        self.assertEqual(squares_needed(1), 1)
        self.assertEqual(squares_needed(2), 2)
        self.assertEqual(squares_needed(3), 2)
        self.assertEqual(squares_needed(4), 3)
    def test_get_count(self):
        self.assertEqual(getCount("abracadabra"), 5)
        self.assertEqual(getCount("hello there world friends"), 7)
        self.assertEqual(getCount("what a lovely day for coding"), 8)
        self.assertEqual(getCount("you never know until you try"), 9)
    def test_longest(self):
        self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        self.assertEqual(longest("noloopinghere", "keepingitclean"), "aceghiklnoprt")
    def test_is_divisible(self):
        self.assertEqual(is_divisible(3,3,4),False)
        self.assertEqual(is_divisible(12,3,4),True)
        self.assertEqual(is_divisible(8,3,4),False)
        self.assertEqual(is_divisible(48,3,4),True)
    def test_find_uniq(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        self.assertEqual(find_uniq([ 0, 0, 0, 0.55, 0, 0 ]), 0.55)
        self.assertEqual(find_uniq([ 0, 1, 1, 1, 1 ]), 0)
        self.assertEqual(find_uniq([ 2345, 10, 2345, 2345, 2345, 2345, 2345 ]), 10)
        

        
# By default, running this test file will test for all Basic Python challenges that do not have in-file testing.      
if __name__ == '__main__':
    unittest.main()