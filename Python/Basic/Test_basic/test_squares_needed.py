import unittest
from squares_needed import squares_needed

class test_squares_needed(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(squares_needed(0), 0)
        self.assertEqual(squares_needed(1), 1)
        self.assertEqual(squares_needed(2), 2)
        self.assertEqual(squares_needed(3), 2)
        self.assertEqual(squares_needed(4), 3)

if __name__ == '__main__':
    unittest.main()