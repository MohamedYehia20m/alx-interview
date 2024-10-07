#!/usr/bin/python3
"""
    0-lockboxes
"""


def canUnlockAll(boxes):
    """

    """
    distinct_keys = set(boxes[0])
    keys = list(distinct_keys)
    n = len(boxes)

    for i in range(1, n):
        if len(distinct_keys) == n - 1:
            return True
        if i > len(distinct_keys):
            return False
        distinct_keys.update(boxes[keys[i - 1]])
        keys = list(distinct_keys)

    return False
