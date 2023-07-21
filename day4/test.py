import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution([1, 2, 3, 5, 6, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_two(self):
        self.assertEqual(solution([1, 2, 3, 12]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    def test_three(self):
        self.assertEqual(solution([6, 9]), [6, 7, 8, 9])
    def test_four(self):
        self.assertEqual(solution([-1, 4]), [-1, 0, 1, 2, 3, 4])
if __name__ == '__main__':
    unittest.main()