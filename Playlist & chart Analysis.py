import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

# Load the dataset
dataset_path = 'C:/Users/Dishu/Desktop/sample project/New folder/dataset/spotify-2023.csv' # Replace with the actual path to your dataset
data = pd.read_csv(dataset_path, encoding='latin1')
# Define a function to extract numerical values from strings
def extract_numeric(value):
    numeric_part = re.search(r'\d+', value)  # Extract digits from the value
    if numeric_part:
        return int(numeric_part.group())  # Convert to integer
    return None  # Return None if no numeric value found

# Apply the function to clean 'streams' column
data['streams'] = data['streams'].apply(extract_numeric)

# Select relevant columns
playlist_columns = ['in_spotify_playlists', 'in_apple_playlists', 'in_deezer_playlists']
chart_columns = ['in_spotify_charts', 'in_apple_charts', 'in_deezer_charts']
# Display the selected columns
playlist_chart_data = data[playlist_columns + chart_columns]
print(playlist_chart_data.head())


# Calculate correlations using Pandas' corr() function
correlation_matrix = playlist_chart_data.corr()

# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Print the correlation values
print(correlation_matrix)

# Calculate the mean and median streams for songs in different numbers of Spotify playlists
spotify_playlist_stats = data.groupby('in_spotify_playlists')['streams'].agg(['mean', 'median'])
print("Spotify Playlist Statistics:")
print(spotify_playlist_stats)

apple_playlists_stats = data.groupby('in_apple_playlists')['streams'].agg(['mean', 'median'])
print("apple playlists Statistics:")
print(apple_playlists_stats)

deezer_playlist_stats = data.groupby('in_deezer_playlists')['streams'].agg(['mean', 'median'])
print("deezer Playlist Statistics:")
print(deezer_playlist_stats)
