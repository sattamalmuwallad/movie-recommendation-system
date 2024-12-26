import pandas as pd
data = {
    "Title": ["Inception", "The Dark Knight", "Interstellar", "Memento", "Dunkirk"],
    "Genre": ["Sci-Fi", "Action", "Sci-Fi", "Thriller", "War"],
    "Rating": [8.8, 9.0, 8.6, 8.4, 7.9]
}
movies = pd.DataFrame(data)
movies.index = range(1,len(movies)+1) 
#print(movies)
import sys
print(sys.executable)
