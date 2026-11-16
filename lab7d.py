# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/11/13
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

# Creating a 2D NumPy array
arr_2d = np.array([[10, 20, 30, 40, 50],
                   [60, 70, 80, 90, 100],
                   [110, 120, 130, 140, 150],
                   [160, 170, 180, 190, 200]])

slice_1 = arr_2d[:2, -3:]
print('first two rows and the last three columns:')
print(slice_1)

slice_2 = arr_2d[1:3, 1:3]
print('middle 2x2 subarray:')
print(slice_2)

slice_3 = arr_2d[::2, ::2]
print('every other row and every other column:')
print(slice_3)