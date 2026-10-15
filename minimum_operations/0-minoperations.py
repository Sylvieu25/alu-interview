#!/usr/bin/python3
"""Minimum Operations: fewest Copy All / Paste operations to get n H's."""


def minOperations(n):
    """Return the fewest operations needed to get exactly n H characters.

    Building n characters splits into steps that each multiply the count
    by a factor f, costing f operations (1 Copy All + f - 1 Pastes).
    The cheapest split uses the prime factors of n, so the answer is the
    sum of the prime factors of n. Returns 0 if n cannot be reached.
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    if n > 1:
        operations += n
    return operations
