"""
Module - pre_order_traversal.py

This module contains a Binary Tree Node class which represents a node in Binary Tree.
Also contains a function to perform pre-order traversal on a Binary Tree.
"""
class BT:
    """
    Binary Tree Node.

    Represents a node in a binary tree.

    Attributes:
        value: The value stored in the node.
        left: The left child of the node.
        right: The right child of the node.
    """
    def __init__(self, value, left=None, right=None):
        """
        Initializes a new instance of the Binary Tree Node.

        Args:
            value: The value to be stored in the node.
            left: The left child of the node (default is None).
            right: The right child of the node (default is None).
        """
        self.value = value
        self.left = left
        self.right = right


def pre_order_traversal(root):
    """
    Perform pre-order traversal on a binary tree.

    Traverses the binary tree in pre-order (root, left, right) and returns the values of
    the nodes in the traversal order.

    Args:
        root: The root node of the binary tree to be traversed.

    Returns:
        A list of node values in pre-order traversal order.
       """
    if root is None:
        return []

    result = [root.value]

    if root.left:
        result.extend(pre_order_traversal(root.left))

    if root.right:
        result.extend(pre_order_traversal(root.right))

    return result


root = BT(1)
root.left = BT(2)
root.left.right = BT(5)
root.right = BT(3)
root.right.left = BT(6)
root.right.right = BT(7)

result = pre_order_traversal(root)
print(result)
