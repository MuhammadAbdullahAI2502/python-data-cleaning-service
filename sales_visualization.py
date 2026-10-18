
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data_cleaned.csv")

# Exclude invalid prices from this sales analysis
valid_sales = df[df["Unit_Price"] >= 0].copy()
valid_sales["Revenue"] = (
    valid_sales["Quantity"] * valid_sales["Unit_Price"]
)

# Chart 1: Revenue by product
product_revenue = (
    valid_sales.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (PKR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("revenue_by_product.png", dpi=150)
plt.show()

# Chart 2: Revenue by city
city_revenue = valid_sales.groupby("City")["Revenue"].sum()

plt.figure(figsize=(8, 5))
city_revenue.plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue (PKR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("revenue_by_city.png", dpi=150)
plt.show()

print("Charts saved successfully!")