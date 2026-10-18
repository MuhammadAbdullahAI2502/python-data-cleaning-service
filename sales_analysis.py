
import pandas as pd

# Load cleaned data
df = pd.read_csv("sales_data_cleaned.csv")

# Calculate revenue only for valid, non-negative prices
valid_sales = df[df["Unit_Price"] >= 0].copy()
valid_sales["Revenue"] = (
    valid_sales["Quantity"] * valid_sales["Unit_Price"]
)

print("\n--- SALES SUMMARY ---")
print("Valid rows:", len(valid_sales))
print("Total revenue:", valid_sales["Revenue"].sum())

print("\n--- REVENUE BY PRODUCT ---")
print(
    valid_sales.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY CITY ---")
print(
    valid_sales.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- QUANTITY SOLD BY PRODUCT ---")
print(
    valid_sales.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

# Save the analysis results
product_report = (
    valid_sales.groupby("Product", as_index=False)
    .agg(
        Units_Sold=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

product_report.to_csv("product_sales_report.csv", index=False)

print("\nReport saved: product_sales_report.csv")
