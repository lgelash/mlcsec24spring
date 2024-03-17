import numpy as np
import pandas as pd

np.random.seed(0)
data = np.random.randn(200, 4)

df = pd.DataFrame(data)

df.to_csv('network_data.csv', index=False, header=False)

# Step 2: Calculate correlation matrix using Pearson formula
import csv

# Read data from CSV file
with open('network_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = [list(map(float, row)) for row in reader]


# Transpose data for correlation calculation
data_transpose = np.array(data).T

# Calculate correlation matrix
correlation_matrix = np.corrcoef(data_transpose)

# Step 3: Save correlation matrix to PDF file
import matplotlib.pyplot as plt

# Plot correlation matrix
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation')
plt.title('Correlation Matrix')
plt.xticks(range(len(df.columns)), df.columns, rotation=45)
plt.yticks(range(len(df.columns)), df.columns)
plt.savefig('correlation_matrix.pdf', format='pdf')
plt.show()

# Step 4: Identify features with highest correlation
# Find the indices of the maximum correlation (excluding the diagonal)
max_corr_index = np.unravel_index(np.argmax(np.abs(correlation_matrix - np.eye(correlation_matrix.shape[0]))), correlation_matrix.shape)

# Extract the feature names with the highest correlation
feature1_name = df.columns[max_corr_index[0]]
feature2_name = df.columns[max_corr_index[1]]

# Step 5: Save features with highest correlation to PDF file
from fpdf import FPDF

# Create PDF document
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Features with Highest Correlation:", ln=True, align="C")

# Write feature names to PDF
pdf.cell(200, 10, txt=f"Highest correlation: {feature1_name}, 2nd highest: {feature2_name}", ln=True, align="C")
pdf.output("highest_correlation.pdf")

# Print repository link
print("Repository link: <your GitHub repository link>")
