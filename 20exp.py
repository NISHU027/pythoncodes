import numpy as np

# Input array
arr = np.array([10, 20, 30, 40, 50])

# Another array for correlation
arr2 = np.array([15, 25, 35, 45, 55])

# Calculations
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
variance = np.var(arr)

# Correlation coefficient
correlation = np.corrcoef(arr, arr2)

# Display results
print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Correlation Coefficient:\n", correlation)