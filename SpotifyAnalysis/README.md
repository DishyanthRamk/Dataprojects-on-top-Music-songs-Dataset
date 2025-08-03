Spotify Song Popularity Analysis 🎵

Analysis of Attributes Impact on Song Popularity

Introduction
This project analyzes how various audio features — including **danceability, valence, energy, acousticness, instrumentalness, liveness, and speechiness** — impact the **popularity of songs**.

Popularity is measured using:
- Number of streams
- Presence in Spotify charts
- Inclusion in playlists

The goal is to identify which features play the strongest role in making a song popular.

---

Steps and Analysis

Step 1: Load the Dataset
Used `pandas` to load a dataset containing song attributes and popularity metrics.

Step 2: Exploratory Data Analysis (EDA)
Visualized the distribution of song popularity using histograms (streams).

Step 3: Correlation Analysis
Created a correlation matrix to explore relationships between features and popularity.

Step 4: Heatmap Visualization
Used a heatmap to show strength and direction of relationships.

Step 5: Statistical Analysis
Divided songs into high and low popularity groups using median stream value.  
Performed **t-tests** to compare audio features across both groups.

Step 6: Violin Plots
Visualized feature distributions for high vs. low popularity songs.

Step 7: Attribute Significance Visualization
Bar chart (log-scale) of p-values showed which features were statistically significant.

Step 8: Model Building (Optional)
Suggested regression modeling to predict popularity — currently commented out.

---

 Conclusion
- Danceability, speechiness, and valence showed statistically significant impact on song popularity.
- Energy, acousticness, instrumentalness, and liveness** had weaker or no impact.

---

Technologies Used
- Python
- Pandas
- Seaborn
- Matplotlib
- Statistical Analysis (t-tests)

---

Dataset
Spotify audio features and popularity metrics (Kaggle dataset)
