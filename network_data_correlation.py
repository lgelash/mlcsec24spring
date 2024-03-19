import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generating network packet data and writing generated data to CSV file
np.random.seed(0)
data = np.random.randn(200, 4)
df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4'])
df.to_csv('network_data.csv', index=False, header=False)

# Calculate correlation matrix using Pearson formula
import csv

# Read data from CSV file
with open('network_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = [list(map(float, row)) for row in reader]

# Transpose data for correlation calculation
data_transpose = np.array(data).T

# Calculate correlation matrix
correlation_matrix = np.corrcoef(data_transpose)

# Plot correlation matrix
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')

# Add text for matrix values
for i in range(len(df.columns)):
    for j in range(len(df.columns)):
        text = f"{correlation_matrix[i, j]:.2f}"  # Format to 2 decimal places
        plt.text(j, i, text, ha="center", va="center", color="black")

# Feature names on X-axis
plt.xticks(range(len(df.columns)), df.columns, rotation=45)

# Feature names on Y-axis (reversed order for bottom placement)
plt.yticks(range(len(df.columns)), df.columns[::-1])

# Plot correlation matrix
plt.colorbar(label='Correlation')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.pdf', format='pdf')
plt.show()

# Find the indices of the maximum correlation (excluding the diagonal)
max_corr_index = np.unravel_index(np.argmax(np.abs(correlation_matrix - np.eye(correlation_matrix.shape[0]))), correlation_matrix.shape)

# Extract the feature names with the highest correlation
feature1_name = df.columns[max_corr_index[0]]
feature2_name = df.columns[max_corr_index[1]]

# Save features with highest correlation to PDF file
from fpdf import FPDF

# Create PDF document
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Features with Highest Correlation:", ln=True, align="C")

# Write feature names to PDF
pdf.cell(200, 10, txt=f" {feature1_name} and {feature2_name}", ln=True, align="C")
pdf.output("highest_correlation.pdf")

# Print features with highest correlation
print(f"Highest correlation: {feature1_name} and {feature2_name}")