"""
Module - test.py

This module contains tests for every case possible.
"""

import unittest

from model.is_subarray import is_subarray


class TestIsSubarray(unittest.TestCase):

    """
    Tests for is_subarray function.
    """
    def test_1(self):
        """
        Test if the function can correctly recognize and compare subarray.

        Returns:
            boolean

        Expected return: True
        """
        self.assertTrue(is_subarray([1, 2, 3], [1, 2, 3, 4]))

    def test_2(self):
        """
        Test if the function can correctly recognize that it`s not subarray.

        Returns:
            boolean

        Expected return: False
        """
        self.assertFalse(is_subarray([4, 2], [1, 2, 3, 4]))

    def test_3(self):
        """
        Test if the function can correctly recognize nums1 as a subarray of nums2
        with different values.

        Returns:
            boolean

        Expected return: True
        """
        self.assertTrue(is_subarray([1, 3, 5], [1, 2, 3, 4, 5]))

    def test_4(self):
        """
        Test if the function can correctly recognize nums1 as not a subarray of nums2.

        Returns:
            boolean

        Expected return: False
        """
        self.assertFalse(is_subarray([1, 2, 3, 4, 5], [1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
