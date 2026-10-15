# alu-interview

Interview preparation algorithm problems, written in Python 3.

## minimum_operations

Given a file containing a single `H`, and an editor that can only `Copy All`
and `Paste`, find the fewest operations needed to get exactly `n` H's.

**Approach:** each Copy All followed by k Pastes multiplies the count by
(k + 1) at a cost of (k + 1) operations. The minimum total is the sum of
the prime factors of `n`, for example 12 = 2 × 2 × 3 → 7 operations.
Returns `0` when `n` cannot be reached (n < 2).
