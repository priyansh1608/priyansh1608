"""
3.  Given a CSV file with columns: song_name, artist, streams, and genre 
    (simulate a mini Spotify dataset with at least 10 rows), write Python 
    code to load the data using pandas and display the number of songs in 
    each genre.
"""

import pandas as pd

data = {
    "song_name": [
        "Song A", "Song B", "Song C", "Song D", "Song E",
        "Song F", "Song G", "Song H", "Song I", "Song J"
    ],
    "artist": [
        "Artist 1", "Artist 2", "Artist 3", "Artist 4", "Artist 5",
        "Artist 6", "Artist 7", "Artist 8", "Artist 9", "Artist 10"
    ],
    "streams": [
        1000, 2500, 1800, 3200, 1500,
        4000, 2200, 1700, 3500, 2800
    ],
    "genre": [
        "Pop", "Rock", "Pop", "Hip-Hop", "Rock",
        "Pop", "Jazz", "Hip-Hop", "Jazz", "Pop"
    ]
}

df = pd.DataFrame(data)

print("Number of songs in each genre:")
print(df["genre"].value_counts())