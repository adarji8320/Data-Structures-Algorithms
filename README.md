# Data Structures & Algorithms

A collection of Python solutions to common data structures and algorithms problems, focused on array-based patterns. Each file is a self-contained script: a problem statement in the comments, a `Solution` class implementing the algorithm, and a runnable example at the bottom.

## Problems

| # | File | Problem | Approach |
|---|------|---------|----------|
| 1 | [1_set_matrix_zero.py](1_set_matrix_zero.py) | Set Matrix Zero (solution 1) | Boolean row/column marker arrays — O(1) extra space per cell lookup |
| 2 | [2_set_matrix_zero.py](2_set_matrix_zero.py) | Set Matrix Zero (solution 2) | Track zero coordinates in a list, then zero out their rows/columns |
| 3 | [3_pascals_triangle.py](3_pascals_triangle.py) | Pascal's Triangle | Binomial coefficient formula, row by row |
| 4 | [4_kadane_algorithm.py](4_kadane_algorithm.py) | Kadane's Algorithm | Maximum sum contiguous subarray in O(n) |
| 5 | [5_dutch_national_flag_algorithm.py](5_dutch_national_flag_algorithm.py) | Sort an array of 0s, 1s, 2s | Three-way partition (Dutch National Flag), single pass, O(1) space |
| 6 | [6_stock_buy_and_sell.py](6_stock_buy_and_sell.py) | Best Time to Buy and Sell Stock | Two one-pass variants tracking min price / max profit |
| 7 | [7_rotate_matrix_clockwise.py](7_rotate_matrix_clockwise.py) | Rotate Matrix 90° Clockwise | Transpose, then reverse each row |
| 8 | [8_rotate_matrix_counterclockwise.py](8_rotate_matrix_counterclockwise.py) | Rotate Matrix 90° Counterclockwise | Transpose, then reverse the row order |
| 9 | [9_merge_intervals.py](9_merge_intervals.py) | Merge Overlapping Intervals | Sort by start, then merge in a single linear pass |
| 10 | [10_merge_two_sorted_arrays_without_extra_space_1.py](10_merge_two_sorted_arrays_without_extra_space_1.py) | Merge Two Sorted Arrays | Combine and sort (see note below) |

## Requirements

- Python 3.10+ (file 5 uses the `match` statement introduced in 3.10)

## Running a solution

Each file runs standalone and prints its result:

```bash
python 4_kadane_algorithm.py
```

## Notes

- File 10 is named "without extra space" but currently merges via `sorted(arr1 + arr2)`, which uses O(n+m) auxiliary space. A true in-place two-pointer/gap-method solution is a good next addition.
- Solutions favor clarity over micro-optimization and are meant as a study reference rather than a library — copy what's useful into your own projects.
