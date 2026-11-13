# Advance Leetcode

This repository contains Python solutions for selected LeetCode-style problems. Each file includes a focused implementation and a brief explanation of the approach.

## Files

- [image.py](image.py) — Rotates a square matrix by 90 degrees clockwise using in-place transpose + row reversal.
- [jump.py](jump.py) — Determines whether you can reach the end of the array using the greedy "maximum reach" strategy.
- [search.py](search.py) — Finds the correct insertion index using binary search.

## File Details

### [image.py](image.py)

Problem type: Matrix manipulation

This solution rotates a square matrix in place:

1. Transpose the matrix by swapping values across the main diagonal.
2. Reverse each row to achieve a clockwise rotation.

Why it works:
- Transposing moves the matrix toward the desired orientation.
- Reversing each row converts the orientation from a counterclockwise result to a clockwise one.

Time complexity: O(n²)
Space complexity: O(1)

### [jump.py](jump.py)

Problem type: Greedy algorithm

This solution checks if it is possible to reach the last index of the array:

- Track the farthest index reachable so far.
- If the current index exceeds the maximum reachable position, stop immediately because it is impossible to continue.
- Update the maximum reach using the current value in the array.

Why it works:
- At each index, the best decision is to keep the farthest possible reachable position.
- If you can keep moving forward without falling behind, the end is reachable.

Time complexity: O(n)
Space complexity: O(1)

### [search.py](search.py)

Problem type: Binary search

This solution returns the index where a target should be inserted into a sorted array.

<details>
<summary><strong>Hidden explanation (click to reveal)</strong></summary>

This is a classic binary search problem. Instead of scanning the whole array, it keeps two pointers:

- `left` starts at the beginning of the array.
- `right` starts at the end of the array (represented as `len(nums)`).

Then it repeatedly checks the middle element:

- If `nums[mid] < target`, the target should be to the right, so `left = mid + 1`.
- Otherwise, the target is at `mid` or to the left, so `right = mid`.

The loop stops when `left == right`, which means the search space has collapsed to the exact insertion position.

Why it works:
- The array is sorted, so numbers smaller than the target are always on the left.
- Numbers greater than or equal to the target are always on the right.
- By halving the search range each time, the algorithm reaches the correct insertion point in logarithmic time.

Time complexity: O(log n)
Space complexity: O(1)

</details>

## How to Use

Open any file in this repository and run the solution with Python:

```bash
python image.py
python jump.py
python search.py
```

If you want, I can also turn this into a more polished README with a project banner, badges, and a table of contents.
