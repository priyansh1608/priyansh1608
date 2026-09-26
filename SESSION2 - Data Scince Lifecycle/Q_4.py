"""
4.   Create a simple bar chart using matplotlib to visualize the number of movies 
     per genre from a dataset (you can make up a small dataset with at least 3 
     genres and 10 movies, like BookMyShow's movie listings).
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "movie_name": [
        "Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5",
        "Movie 6", "Movie 7", "Movie 8", "Movie 9", "Movie 10"
    ],
    "genre": [
        "Action", "Comedy", "Drama", "Action", "Comedy",
        "Action", "Drama", "Comedy", "Action", "Drama"
    ]
}

df = pd.DataFrame(data)

genre_count = df["genre"].value_counts()

plt.bar(genre_count.index, genre_count.values)

plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.title("Number of Movies per Genre")

plt.show()