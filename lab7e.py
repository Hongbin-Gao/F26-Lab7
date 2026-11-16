# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/11/16
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.

import pandas as pd

# TO DO 2: Create a series according to instructions given in readme.md file.

data = {'F':'<50', 'D':'50-59', 'C':'60-69', 'B':'70-79', 'A':'80-89', 'A+':'90-100'}
grades = pd.Series(data)

# TO DO 3: Perform the operations on this series given in readme.md file.

print('Grade series:\n', grades, '\n')

print('C and A+:\n', grades.loc[['C', 'A+']], '\n')

print('Value at C:\n', grades.loc['C'], '\n')

print('Series multiplied by 2:\n', grades * 2)

# TO DO 4: Run the script.

