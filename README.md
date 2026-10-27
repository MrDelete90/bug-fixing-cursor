# Bug Fixing Using Cursor AI

This project shows a buggy Python program that was identified and corrected using Cursor AI.

## Files
- **buggy_program.py**: the original program with two bugs
- **fixed_program.py**: the corrected version

## Bugs Found and Fixed
1. **calculate_average**: the function added `+ 1` to the result, so the average was always 1 too high. The `+ 1` was removed.
2. **find_largest**: the comparison used `<` and the starting value was 0, so it never found the largest number. It now uses `>` and starts from the first item in the list.

## Technologies Used
Python, Cursor AI

## Author
AKASH KUMAR
