# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/11/16
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

# TO DO 1: create a new data frame from the link of csv file provided in readme.md file.

url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(url)

# TO DO 2: Perform the operations provided in readme.md file on this data frame.

print('Summary:\n', df.describe(include='all'))

print('\nFirst 10:\n', df.head(10))
print('\nLast 10:\n', df.tail(10))

print('\nEarliest year:', df['Year'].min())
print('Latest year:', df['Year'].max())

print('\nUnique genres:\n', df['Genre'].unique())

non_usa_movies = (df['Origin'] != 'USA').sum()
print('\nMovies not made in USA:', non_usa_movies)

highest_rating = df.sort_values('IMDB rating').tail(10)
print('\nTop 10 highest-rated movies:\n', highest_rating['IMDB rating'])

def get_decade(year):
    return (year // 10 * 10)

df['decade'] = get_decade(df['Year'])

decade_rating = df.groupby('decade')['IMDB rating'].mean()
best_decade = decade_rating.idxmax()
print("\nBest Decade:", best_decade)

plt.scatter(decade_rating.index, decade_rating.values)
plt.show()

# TO DO 3: Run the script.

