import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("data.csv")

# Display data
print("Data:\n", df)

# Basic Analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Plot graph (Bar Chart)
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()