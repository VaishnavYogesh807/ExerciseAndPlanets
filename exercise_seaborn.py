import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Determine the current script directory path for reference.
os.path.join(os.path.dirname(__file__))

# Set working directory to the folder that contains the CSV file.
os.chdir('/Users/vaishnav/Library/Mobile Documents/com~apple~CloudDocs/Python')

# Load exercise data from the CSV file into a pandas DataFrame.
# Replaced np.genfromtxt with pd.read_csv for better handling of categorical columns (ChatGPT suggestion).
ex_data = pd.read_csv('Exercise_Data.csv')

# Create a heatmap from the exercise data.
# Drop non-numeric columns before normalizing numeric values.
plt.figure(figsize=(10, 8))
numeric_data = ex_data.drop(labels = ['id', 'diet', 'kind'], axis = 1)
# Normalize each numeric column to the 0-1 range for the heatmap.
numeric_data = (numeric_data - numeric_data.min()) / (numeric_data.max() - numeric_data.min())
sns.heatmap(numeric_data, cmap='viridis')
plt.title('Heatmap of Exercise Data')
plt.xlabel('pulse measurements')
plt.ylabel('individuals')
plt.show()

# Create a boxplot for 30-minute pulse values grouped by diet.
plt.figure(figsize=(10, 6))
sns.catplot(x='diet', y='30 min', data=ex_data, kind='box')
plt.title('Boxplot of Final Pulse (30 min) by Diet')
plt.xlabel('Diet')
plt.ylabel('Pulse (30 min)')
plt.show()

# Create a boxplot for 30-minute pulse values grouped by exercise kind.
plt.figure(figsize=(10, 6))
sns.catplot(x='kind', y='30 min', data=ex_data, kind='box')
plt.title('Boxplot of Final Pulse (30 min) by Exercise Kind')
plt.xlabel('Exercise Kind')
plt.ylabel('Pulse (30 min)')
plt.show()

# ANALYSIS:
# 1. The heatmap shows that there is a general increase in pulse measurements over time, with some individuals showing a more significant increase than others.
# 2. The boxplot for diet indicates that there is some variation in the final pulse (30 min) across different diets, with some diets showing higher median pulse values than others.
# 3. The boxplot for exercise kind suggests that certain types of exercise may lead to higher final pulse values, indicating that the intensity or nature of the exercise may have an impact on cardiovascular response.

# Load the built-in seaborn planets dataset for planetary visualizations.
planet_data = sns.load_dataset('planets')

# RELATIONAL PLOTS
# Scatter plot of planet distance versus planet mass with log scaling.
sns.scatterplot(x='distance', y='mass', data=planet_data)
plt.title('Scatter Plot of Planet Distance vs Mass')
plt.xlabel('Distance (light years)')
plt.ylabel('Mass (Jupiter Masses)')
plt.xscale('log')
plt.yscale('log')
plt.show()

# Line plot of planet distance versus planet mass.
sns.lineplot(x='distance', y='mass', data=planet_data)
plt.title('Line Plot of Planet Distance vs Mass')
plt.xlabel('Distance (light years)')
plt.ylabel('Mass (Jupiter Masses)')
plt.xscale('log')
plt.yscale('log')
plt.show()

# DISTRIBUTION PLOTS
# Histogram with KDE overlay to show distance distribution.
sns.histplot(planet_data['distance'], bins=30, kde=True)
plt.title('Histogram of Planet Distances')
plt.xlabel('Distance (light years)')
plt.ylabel('Count')
plt.xscale('log')
plt.show()

# KDE plot showing the density estimate of planet distances.
sns.kdeplot(planet_data['distance'], shade=True)
plt.title('KDE Plot of Planet Distances')
plt.xlabel('Distance (light years)')
plt.ylabel('Density')
plt.xscale('log')
plt.show()

# CATEGORICAL PLOTS
# Boxplot comparing distance distributions by discovery method.
sns.boxplot(x='method', y='distance', data=planet_data)
plt.title('Box Plot of Planet Distance by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Distance (light years)')
plt.xticks(rotation=45) # Rotate x-axis labels for better readability (ChatGPT suggestion).
plt.yscale('log')
plt.show()

# Barplot comparing average planet distance for each discovery method.
sns.barplot(x='method', y='distance', data=planet_data)
plt.title('Bar Plot of Planet Distance by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Distance (light years)')
plt.xticks(rotation=45) # Rotate x-axis labels for better readability (ChatGPT suggestion).
plt.yscale('log')
plt.show()

# ANALYSIS
# 1. The scatter plot shows a positive correlation between distance and mass, indicating that more massive planets tend to be farther away.
# 2. The line plot also shows a similar trend, but with more variability in the data.
# 3. The histogram and KDE plot reveal that most planets are located within a certain distance range, with a long tail of planets that are much farther away.
# 4. The box plot and bar plot indicate that certain discovery methods are more likely to find planets at greater distances, suggesting that these methods may be more effective for detecting distant planets.