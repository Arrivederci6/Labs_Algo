"""
Module - is_subarray.py

This module contains a function to check if one array is a subarray of another array.
"""


def is_subarray(nums1, nums2):
    """
    Checks if a nums1 is a sub array of nums2.

    Args:
        - nums1 (List)
        - nums2 (List)

    Returns:
        - boolean (True - if nums1 is a sub array of nums2,
                    False - if nums1 is not a sub array of nums2)
    """
    if len(nums1) > len(nums2):
        return False

    i = j = 0

    while i < len(nums2) and j < len(nums1):
        if nums1[j] == nums2[i]:
            i += 1
            j += 1
        else:
            i += 1

    return j == len(nums1)
