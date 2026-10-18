
import pandas as pd

# Read the existing datasets
cleaned_data = pd.read_csv("sales_data_cleaned.csv")
product_report = pd.read_csv("product_sales_report.csv")

# Exclude negative prices from revenue calculations
valid_sales = cleaned_data[
    cleaned_data["Unit_Price"] >= 0
].copy()

valid_sales["Revenue"] = (
    valid_sales["Quantity"] * valid_sales["Unit_Price"]
)

# Create a city-wise report
city_report = (
    valid_sales.groupby("City", as_index=False)
    .agg(
        Total_Orders=("Order_ID", "nunique"),
        Total_Revenue=("Revenue", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

# Export all reports to one Excel workbook
with pd.ExcelWriter(
    "Sales_Analysis_Report.xlsx",
    engine="openpyxl"
) as writer:
    cleaned_data.to_excel(
        writer, sheet_name="Cleaned Data", index=False
    )
    product_report.to_excel(
        writer, sheet_name="Product Report", index=False
    )
    city_report.to_excel(
        writer, sheet_name="City Report", index=False
    )

print("Excel report created successfully!")
print("File: Sales_Analysis_Report.xlsx")
