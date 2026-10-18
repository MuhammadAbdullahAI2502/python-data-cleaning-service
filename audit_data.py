
import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print("Rows and columns:", df.shape)

print("\n--- COLUMN DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- DUPLICATE ORDER IDs ---")
print(df["Order_ID"].duplicated().sum())

print("\n--- NEGATIVE QUANTITIES OR PRICES ---")
print("Negative quantities:", (df["Quantity"] < 0).sum())
print("Negative prices:", (df["Unit_Price"] < 0).sum())
