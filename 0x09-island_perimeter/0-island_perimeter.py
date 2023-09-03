#!/usr/bin/python3
"""
a function def island_perimeter(grid): that returns the perimeter of the
island described in grid.
"""
from typing import List


def island_perimeter(grid: List[List]) -> int:
    """
    return the perimeter of the island, which is the length
    and breath surrounded by water.

    Args:
        grid (List[List]): List of list of zeroes and ones.
        where 0's signifies water and 1's signify island.

    Returns:
        int: the perimeter.
    """
    length = 0
    breadth = 0

    for row in grid:
        if any(row):
            length += 1
            # if the number of 1 is not greater than one then
            # we won't add to the breadth.
            b = row.count(1)
            breadth += b if b != 1 else 0

    return 2 * (length + breadth)
