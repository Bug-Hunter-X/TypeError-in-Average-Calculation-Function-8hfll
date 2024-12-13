# Python Code Error: TypeError in Average Calculation

This repository demonstrates a common error in Python: a `TypeError` that occurs when calculating the average of a list containing mixed data types (numbers and non-numbers).

The `bug.py` file contains the function with the error, while `bugSolution.py` shows a corrected version.

## Bug Description
The original code fails to handle the case where the input list `numbers` contains non-numeric elements. The `sum()` function can't handle strings, leading to a `TypeError`.

## Bug Solution
The solution involves adding a check to ensure all elements in the list are numeric before calculating the average.