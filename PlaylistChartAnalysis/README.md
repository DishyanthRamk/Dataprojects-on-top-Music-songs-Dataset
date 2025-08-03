Playlist and Chart Analysis

Introduction
This data analysis project explores the relationship between playlist presence** and **chart performance** for songs across major music platforms, including Spotify, Apple Music, and Deezer.

The dataset includes:
- Song attributes
- Streaming statistics
- Playlist presence
- Chart rankings from 2023

The goal is to understand how inclusion in playlists affects a song's streaming performance and chart visibility.

---

Project Steps

Step 1: Data Preparation

- Loading the Dataset:
  Used `pandas` to load and manipulate the dataset efficiently.

- Cleaning the 'streams' column: 
  Applied a custom `extract_numeric` function to convert string-based stream counts into clean numeric values.

---

Step 2: Correlation Analysis

- Calculating Correlations: 
  Measured relationships between playlist presence and chart performance for all three platforms.

- Visualizing with a Heatmap:
  Created a correlation heatmap using `seaborn` to easily spot trends and patterns.

---

Step 3: Playlist Statistics

- Mean & Median Calculations:  
  Computed the average and median streams for songs based on the number of playlists they appeared in (across Spotify, Apple Music, Deezer).

---

Results & Insights

Correlation Matrix:
- Deezer: Strongest correlation between playlist presence and chart performance (0.60).
- Spotify & Apple Music: Also show positive correlations, but weaker than Deezer.
- Correlations suggest playlist inclusion does impact performance, though the strength varies by platform.

Playlist Stats:
- Spotify:Mean & median streams remained fairly stable regardless of playlist count.
- Apple Music: Some correlation — more playlists = slightly better performance.
- Deezer: Wide variations, showing deeper impact of playlist presence on streaming stats.

---

Dataset
See: [Dataset.md](./Dataset.md)

---

Conclusion
This project provides key insights into how playlist inclusion affects chart performance. Deezer shows the strongest playlist-to-chart impact, followed by Apple Music and Spotify. These findings can inform music promotion strategies, helping artists and labels prioritize platforms and placements for maximum visibility.

---

 Tools Used
- Python
- Pandas
- Seaborn
- Matplotlib
