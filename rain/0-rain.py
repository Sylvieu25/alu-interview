#!/usr/bin/python3
"""Rainwater: how much water is retained between walls after it rains."""


def rain(walls):
    """Return the units of rainwater retained between the given walls.

    walls is a list of non-negative integers, each one a wall of unit
    width. The ends of the list are open, so they retain no water.
    Two pointers move inward from both ends, always advancing the side
    with the lower wall, because that side's water level is limited by
    the tallest wall seen so far on its own side. Returns 0 for an
    empty list.
    """
    if not walls:
        return 0
    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    total = 0
    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                total += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                total += right_max - walls[right]
            right -= 1
    return total
