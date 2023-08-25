#!/usr/bin/python3
"""
    A function that rotates 2D matrix
"""
from typing import List
from copy import deepcopy


def rotate_2d_matrix(matrix: List[List]) -> List[List]:
    """
    This function rotates a 2D matrix.

    Args:
        matrix (List[List]): a n x n matrix
    """
    temp = deepcopy(matrix)
    count = 0
    start = len(matrix) - 1

    while (start > -1):

        for i, num in enumerate(temp[count]):
            matrix[i][start] = num

        count += 1
        start -= 1
