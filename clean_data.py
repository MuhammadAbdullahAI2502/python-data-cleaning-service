
import pandas as pd

# Load the original dataset
df = pd.read_csv("sales_data.csv")

print("Original rows:", len(df))

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

# 2. Flag invalid prices for review
invalid_prices = df["Unit_Price"] < 0
print("Rows with negative prices:", invalid_prices.sum())

# 3. Replace missing city values with "Unknown"
df["City"] = df["City"].fillna("Unknown")

# 4. Save the cleaned dataset
df.to_csv("sales_data_cleaned.csv", index=False)

print("Cleaned rows:", len(df))
print("Missing values remaining:", df.isnull().sum().sum())
print("Cleaned file saved: sales_data_cleaned.csv")

# Display cleaned data
print(df)
