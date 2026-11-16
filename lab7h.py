# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/11/16
# Purpose: Create Histograms.
# Usage: ./lab7h.py

# TO DO 1: Import pandas and matplotlib modules.
import pandas as pd
import matplotlib.pyplot as plt
# TO DO 2: Draw histogram of the data from movies database.

url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(url)
# TO DO 3: Perform the operations provided in readme.md file on this data.

years = df["Year"].copy()
print(years, '\n')

years = years.sort_values()
print(years, '\n')

year_counts = years.value_counts().sort_index()
print(year_counts)

plt.bar(
    year_counts.head(10).index.astype(str),
    year_counts.head(10).values
)
plt.show()
# TO DO 4: Run the script.
