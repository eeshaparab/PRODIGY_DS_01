import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path =r"C:\Users\eesha\OneDrive\Desktop\prodigy\Task1\bank-additional.csv"
data = pd.read_csv(file_path, sep=';')  # Assuming the separator is a semicolon

# Display the first few rows to understand the structure
print(data.head(266))
print(data.columns)

# Plotting a histogram for the age distribution
plt.figure(figsize=(10, 6))
plt.hist(data['age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
