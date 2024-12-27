import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("imdb_movies.csv")
print(movies.head())
print("Shape of dataset:", movies.shape)
print("Columns of dataset:", movies.columns)
print("Missing Values: ", movies.isnull().sum())
# List unique genres
print("Unique Genres:\n", movies["genre"].unique())
print(movies.loc[0, "overview"])

print(movies.duplicated().sum()) # no need to drop duplicates there aren't any 

print(movies.isnull().sum())

rows_with_nulls = movies[movies.isnull().any(axis=1)]
print("Rows with null values:\n", rows_with_nulls)

movies = movies.dropna()
print(movies.shape)
movies.to_csv("imdb_movies_cleaned.csv", index=False)

###############################
################Visualisation
# 1.Distribution of Scores
movies["score"].plot(kind="hist", bins=20, title="Distribution of Movie Scores", color="blue")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# 2. Top Genres by Count
movies["genre"].value_counts().head(10).plot(kind="bar", title="Top 10 Genres by Count", color="purple")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.show()

# 3. Budget vs. Revenue
movies.plot.scatter(x="budget_x", y="revenue", title="Budget vs Revenue", color="red")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.show()

# 4. Revenue Distribution
movies["revenue"].plot(kind="hist", bins=20, title="Distribution of Movie Revenues", color="orange")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# 5. Scores by Genres
genre_scores = movies.groupby("genre")["score"].mean().sort_values(ascending=False).head(10)
genre_scores.plot(kind="bar", title="Top 10 Genres by Average Score", color="green")
plt.xlabel("Genre")
plt.ylabel("Average Score")
plt.show()