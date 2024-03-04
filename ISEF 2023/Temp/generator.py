import pandas as pd

# Create the DataFrame
df = pd.DataFrame({
    "microhubs": [4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8],
    "deliverers": [4, 5, 6, 7, 8, 9, 10, 4, 5, 6, 7, 8, 9, 10, 4, 5, 6, 7, 8, 9, 10, 4, 5, 6, 7, 8, 9, 10, 4, 5, 6, 7, 8, 9, 10],
    "distance": [17, 18, 17, 17, 16, 16, 15, 16, 17, 16, 15, 14, 13, 12, 10, 8, 9, 7, 7, 8, 5, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
    "emissions": [2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8],
    "cost": [3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9]
})



# Save the DataFrame as a CSV file
df.to_csv("generate.csv", index=False)

print("Data saved as CSV file.")