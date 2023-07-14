#!/usr/bin/python3
"""
    You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to the other
    boxes.

    Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    * boxes is a list of lists
    * A key with the same number as a box opens that box
    * You can assume all keys will be positive integers
        There can be keys that do not have boxes
    * The first box boxes[0] is unlocked

    Return True if all boxes can be opened, else return False.
"""
import sys


def canUnlockAll(boxes):
    """ canUnlockAll - list of lists (boxes) with keys.
        Args:
            boxes (list[list]): boxes.
            @Return: true if all are unlocked or false if
            some are unlocked.
    """
    sys.setrecursionlimit(1000000)  # SET RECURSION LIMIT NUMBER.
    un_boxes = [False] * len(boxes)

    def unlock(boxes, index):
        """ unlock - use a key to unlock boxes.
            Args:
                boxes (list[list]): boxes.
                index (int): key
        """
        try:
            # change the value to true if false (box not open), but if
            # the value is true (box has already been unlocked), exit.
            if not un_boxes[index]:
                un_boxes[index] = True
            else:
                return

            keys = boxes[index]
            if not keys:
                return

            for i in keys:
                unlock(boxes, i)

        except IndexError:
            return

    unlock(boxes, 0)
    return all(un_boxes)
