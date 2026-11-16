# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: hongbin
# Date: 2026/11/16
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd

# TO DO 1: Create dataframe from provided dictionaries in readme.md file.

data = {
'colors':{
    'Apple': 'Green',
    'Carrot': 'Red',
    'Radish': 'Purple'
},
'shapes':{
    'Okra': 'Thin',
    'Potato': 'blob',
    'Radish': 'Round'
},
'weights':{
    'Apple': 2.1,
    'Okra': 3.5,
    'Carrot': 1.3,
    'Potato': 2.0,
    'Radish': 3.0
}
}

# TO DO 2: create a data frame provided in dataframe.jpg file.

frame = pd.DataFrame(data)
print('Combined dataframe:\n', frame)

# TO DO 3: Run the script.

