#!/usr/bin/python3
"""
    A function that rotates 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    This function rotates a 2D matrix.

    Args:
        matrix (List[List]): a n x n matrix
    """
    temp = list(map(list, matrix))
    count = 0
    start = len(matrix) - 1

    while (start > -1):

        for i, num in enumerate(temp[count]):
            matrix[i][start] = num

        count += 1
        start -= 1
