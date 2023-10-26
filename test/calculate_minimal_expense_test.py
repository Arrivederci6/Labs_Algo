import unittest

from model import calculate_minimal_expense


class TestCalculateMinimalExpense(unittest.TestCase):

    def test_1(self):
        result = calculate_minimal_expense([50, 20, 30, 17, 100], 10)
        self.assertEqual(result, 207.0)

    def test_2(self):
        result = calculate_minimal_expense([1, 2, 3, 4, 5, 6, 7], 100)
        self.assertEqual(result, 15.0)

    def test_3(self):
        result = calculate_minimal_expense([1, 1, 1], 33)
        self.assertEqual(result, 2.67)


if __name__ == '__main__':
    unittest.main()
