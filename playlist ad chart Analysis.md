Playlist and Chart Analysis

Introduction:
This data analysis project explores the relationship between playlist presence and chart performance for songs listed on various music platforms. 
The project uses a dataset containing information about popular songs in 2023, including attributes, streaming statistics, playlist presence, and chart rankings on platforms like Spotify, Apple Music, and Deezer.

Dataset :check Dataset.md

## Project Steps

Step 1: Data Preparation

Loading the Dataset

The dataset is loaded using the Pandas library, which provides powerful data manipulation capabilities.
Cleaning the 'streams' Column
The 'streams' column may contain non-numeric data. A custom function `extract_numeric` is applied to convert it to numeric values.

Step 2: Correlation Analysis

Calculating Correlations

The correlation matrix is computed to measure the relationships between playlist presence and chart performance for different platforms.

Visualizing Correlations

A heatmap is created using Seaborn to visualize the correlation matrix.

Step 3: Playlist Statistics

Calculating Mean and Median

Statistics are calculated for songs that are included in different numbers of playlists for Spotify, Apple Music, and Deezer.

Conclusion

This data analysis project provides insights into the relationships between playlist presence and chart performance on various music platforms.
It includes data cleaning, correlation analysis, and playlist statistics to understand how playlist inclusion may impact a song's performance.

The findings can be used to make informed decisions about music promotion and playlist placement strategies in the music industry. 
Further analysis and visualization can be performed to gain more insights from the dataset.


Result:

Correlation Matrix:

- The correlation matrix shows the relationships between playlist presence and chart performance for different platforms (Spotify, Apple Music, Deezer).

- Positive values indicate a positive correlation, while negative values indicate a negative correlation.

- A correlation value close to 1 suggests a strong positive relationship, while a value close to -1 suggests a strong negative relationship. A value close to 0 suggests a weak or no relationship.

Here's what you can infer from the correlation matrix:

- There is a positive correlation between playlist presence and chart performance for Spotify, Apple Music, and Deezer, although the strength of the correlation varies.

- The strongest correlation is observed between the presence in Deezer playlists and Deezer chart performance (0.60), indicating that songs included in more Deezer playlists tend to have higher chart rankings on Deezer.

- Spotify and Apple Music also show positive correlations between playlist presence and chart performance, but the correlations are somewhat weaker.

Playlist Statistics:

- The statistics provide insights into the mean and median streams for songs in different numbers of playlists for Spotify, Apple Music, and Deezer.

- The 'mean' represents the average number of streams for songs in a particular number of playlists.

- The 'median' represents the middle value when all values are sorted in ascending order. It's a measure of central tendency that is less affected by outliers.

Here's what you can infer from the playlist statistics:

- For Spotify, the mean and median streams are fairly consistent across different numbers of playlists, suggesting that the number of Spotify playlists a song is included in may not strongly influence its streaming performance.

- For Apple Music, there appears to be some variation in mean and median streams based on the number of playlists, with songs in a smaller number of playlists having lower mean and median streams.

- For Deezer, there is a wide range of mean and median streams across different numbers of playlists, indicating that the number of Deezer playlists may have a more varied impact on streaming performance.

These observations provide valuable insights into the relationships between playlist inclusion and chart performance on different music platforms.

Code : Playlist & chart Analysis.py
