import pandas as pd

movies = pd.read_csv("imdb_movies_cleaned.csv")
print(movies.head())
print("Shape of dataset:", movies.shape) # should be 10052, 12
