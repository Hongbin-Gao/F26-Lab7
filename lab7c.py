# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/11/13
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

# TO DO 1: Create numArray according to instructions given in readme.md file.

numArray = np.random.randint(1,100,100)
print(numArray)

# TO DO 2: Perform the operations on numArray given in readme.md file.

print('First 10 values:')
print(numArray[:10])

print('Last 10 values:')
print(numArray[-10:])

print('30 values starting from 21:')
print(numArray[21:51])

print('Change all values to 101 from index 50 to 65:')
numArray[50:66] = 101
print(numArray)

# TO DO 3: Run the script.

