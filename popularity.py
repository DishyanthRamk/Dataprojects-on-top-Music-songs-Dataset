import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load the dataset
dataset_path = 'dataset/spotify-2023.csv' # Replace with the actual path to your dataset
data = pd.read_csv(dataset_path, encoding='latin1')  # or encoding='utf-16'


# Define a function to extract numerical values from strings
def extract_numeric(value):
    numeric_part = re.search(r'\d+', value)  # Extract digits from the value
    if numeric_part:
        return int(numeric_part.group())  # Convert to integer
    return None  # Return None if no numeric value found

# Apply the function to clean 'streams' column
data['streams'] = data['streams'].apply(extract_numeric)

# Now you can calculate the median without errors
popularity_threshold = data['streams'].median()


#  Exploratory Data Analysis (EDA)
# Visualize the distribution of attributes and popularity indicators
plt.figure(figsize=(12, 8))
sns.histplot(data['streams'], kde=True)
plt.xlabel('Streams')
plt.ylabel('Number of Songs')  # Change y-axis label
plt.title('Distribution of Streams')
plt.show()

#  Correlation Analysis
correlation_matrix = data[['danceability_%', 'valence_%', 'energy_%', 'acousticness_%',
                           'instrumentalness_%', 'liveness_%', 'speechiness_%', 
                           'streams', 'in_spotify_charts', 'in_spotify_playlists']].corr()

# Visualization of Correlation Matrix
# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Create a heatmap with annotations
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, linewidths=0.5, square=True)

# Customize the plot
plt.title("Correlation Heatmap")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()

# Display the plot
plt.show()

# Statistical Analysis
# Divide songs into high-popularity and low-popularity based on a threshold (e.g., median)
popularity_threshold = data['streams'].median()
high_popularity_songs = data[data['streams'] >= popularity_threshold]
low_popularity_songs = data[data['streams'] < popularity_threshold]

# Perform t-tests to compare attribute values between high and low popularity songs
p_values = {}
attributes = ['danceability_%', 'valence_%', 'energy_%', 'acousticness_%',
              'instrumentalness_%', 'liveness_%', 'speechiness_%']
for attribute in attributes:
    t_stat, p_value = ttest_ind(high_popularity_songs[attribute], low_popularity_songs[attribute])
    p_values[attribute] = p_value

# Print p-values for attribute analysis
print("P-values for attribute analysis:")
for attribute, p_value in p_values.items():
    print(f"{attribute}: {p_value}")
          
# Create violin plots
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
sns.violinplot(data=data[attributes], palette="Set2", cut=0)
plt.xticks(rotation=45)
plt.xlabel('Attributes')
plt.ylabel('Attribute Value')
plt.title('Attribute Differences between High and Low Popularity Songs')
plt.tight_layout()

# Display the plot
plt.show()



#If you want to make a chart after the output of p_values 
# Attributes and corresponding p-values
Attributes = ['danceability_%', 'valence_%', 'energy_%', 'acousticness_%','instrumentalness_%', 'liveness_%', 'speechiness_%']
P_values = [0.024267232457656298, 0.1776528750097465, 0.18970576996990404,0.32208605068639967, 0.9002071840872985, 0.16836994916078127,6.225989824309345e-05]

# Create a bar chart for p-values
plt.figure(figsize=(10, 6))
plt.barh(Attributes, P_values, color='blue')
plt.xlabel('P-value')
plt.ylabel('Attributes')
plt.title('Significance of Attributes on Popularity')
plt.xscale('log')  # Use logarithmic scale for better visualization of small values
plt.tight_layout()

# Display the plot
plt.show()


# Model Building (Optional)
# You can proceed with building regression models to predict popularity based on attributes.

