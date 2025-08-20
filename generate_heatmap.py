import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the raw data from Excel
raw_data = pd.read_excel('q-excel-correlation-heatmap.xlsx')

# Compute the correlation matrix
corr = raw_data.corr()

# Save the correlation matrix to CSV
corr.to_csv('correlation.csv')


# Set up the matplotlib figure for 400x400 pixels (5x5 inches at 80 dpi)
plt.figure(figsize=(5, 5), dpi=80)

# Draw the heatmap with the red-white-green color map
sns.heatmap(corr, annot=True, cmap='RdYlGn', center=0, fmt='.2f', square=True, cbar=True)

# Save the heatmap
plt.tight_layout()
plt.savefig('heatmap.png', dpi=100)
plt.close()
