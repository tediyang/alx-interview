#!/usr/bin/python3
"""
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given a
    number n, write a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
"""
def minOperations(n):
    """
        Returns a integer of the minimum operation that can occur.

    Args:
        n (integer): the number of times an operation is made to reach this
        integer.
    """
    if n < 2:
        return 0

    count = 0
    max_div = 2

    while n > 1:
        if n % max_div == 0:
            n //= max_div
            count += max_div

        else:
            if max_div == 2:
                max_div += 1
            else:
                max_div += 2

    return count
