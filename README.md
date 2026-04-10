# ExerciseAndPlanets
## Overview

This project explores how data visualization can be used to understand patterns in two datasets:

1. Exercise data (pulse rates affected by diet and exercise)
2. Planet data (characteristics of discovered planets)

The goal is to use different types of graphs—heatmaps, relational plots, distribution plots, and categorical plots—to identify trends and communicate insights clearly.

## Design

This project is implemented using Python with the following libraries:

* **pandas** for data handling
* **seaborn** for visualization
* **matplotlib** for customization

The program follows a simple procedural design:

1. Load datasets
2. Clean and prepare data
3. Generate visualizations
4. Analyze and interpret results

No custom classes were used, as the project focuses on data analysis and visualization rather than object-oriented design.

## Key Concepts

### Data Handling

* CSV file is loaded using `pandas.read_csv()`
* Non-numeric columns are removed when needed (e.g., for heatmaps)
* Data normalization is applied for better visualization

### Visualizations

* **Heatmap**: Shows changes in pulse over time
* **Categorical plots (boxplots, barplots)**: Compare pulse by diet and exercise type
* **Relational plots (scatter, line)**: Show relationships between planet features
* **Distribution plots (histogram, KDE)**: Show how planet distances are spread

## Limitations

* The exercise dataset is small, so the results may not apply to other situations.
* Some visualizations, like line plots, may not show unordered data exactly as it is.
* The accuracy of the planets dataset may be affected by missing values.
* The scale is logarithmic, which might be harder for beginners to understand.

## Conclusion

This project shows how different ways of visualizing data can bring out different parts of it. It shows that when health data and space data are displayed well, they can show important patterns.
