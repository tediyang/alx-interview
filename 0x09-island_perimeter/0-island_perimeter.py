#!/usr/bin/python3
''' island perimeter module '''


def island_perimeter(grid):
    ''' calculates perimeter of an island '''

    row_count = len(grid)
    col_count = len(grid[0])

    p = 0
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j]:
                u = (not i) or grid[i - 1][j] == 0
                d = (i + 1 >= row_count) or grid[i + 1][j] == 0
                l = (not j) or grid[i][j - 1] == 0
                r = (j + 1 >= col_count) or grid[i][j + 1] == 0
                p += u + d + l + r
    return p
# """
# a function def island_perimeter(grid): that returns the perimeter of the
# island described in grid.
# """


# def island_perimeter(grid: List[List]) -> int:
#     """
#     return the perimeter of the island, which is the length
#     and breath surrounded by water.

#     Args:
#         grid (List[List]): List of list of zeroes and ones.
#         where 0's signifies water and 1's signify island.

#     Returns:
#         int: the perimeter.
#     """
#     length = 0
#     breadth = 0

#     for row in grid:
#         if any(row):
#             length += 1
#             # if the number of 1 is not greater than one then
#             # we won't add to the breadth.
#             b = row.count(1)
#             if breadth < 1:
#                 breadth += b if b != 1 else 0
                
#     # if length is 1 at least then breadth must be 1
#     if length and not breadth:
#         breadth = 1
#     return 2 * (length + breadth)
