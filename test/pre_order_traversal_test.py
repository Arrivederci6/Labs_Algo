"""
Module - pre_order_traversal_test.py

This module contains a test for pre_order_traversal function.
"""
import unittest

from models.pre_order_traversal import BT, pre_order_traversal


class TestBinaryTreeTraversal(unittest.TestCase):
    """
    Unit tests for the pre_order_traversal function.
    """
    def setUp(self):
        """
        Set up the test by creating a binary tree for testing.
        """
        self.root = BT(1)
        self.root.left = BT(2)
        self.root.left.right = BT(5)
        self.root.right = BT(3)
        self.root.right.left = BT(6)
        self.root.right.right = BT(7)

    def test_pre_order_traversal(self):
        """
        Test the pre_order_traversal function.
        """
        result = pre_order_traversal(self.root)
        expected = [1, 2, 5, 3, 6, 7]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
