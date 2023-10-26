"""
Module - calculate_minimal_expense.py

This module contains a function to calculate minimal expense.
"""


def calculate_minimal_expense(prices_arr, discount):
    """
        A function to calculate the most profitable sum for which we can purchase all products,
        while applying a discount for every 3rd good.

        Args:
            - prices_arr (List)
            - discount (int)

        Returns:
            - float (round(sum(prices_arr)))
        """

    while True:
        swapped = False
        for i in range(1, len(prices_arr)):
            if prices_arr[i - 1] > prices_arr[i]:
                prices_arr[i - 1], prices_arr[i] = prices_arr[i], prices_arr[i - 1]

                swapped = True
        if not swapped:
            break

    prices_arr = list(reversed(prices_arr))

    for i in range(len(prices_arr) // 3):
        prices_arr[i] *= (1 - discount / 100)
    return round(sum(prices_arr), 2)


print(calculate_minimal_expense([50, 20, 30, 17, 100], 10))
print(calculate_minimal_expense([1, 2, 3, 4, 5, 6, 7], 100))
print(calculate_minimal_expense([1, 1, 1], 33))
