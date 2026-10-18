
import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1005, 1007, 1008],
    "Customer": ["Ali", "Sara", "Ahmed", "Hina", "Usman", "Usman", "Zara", "Bilal"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse", "Mouse", "Laptop", "Keyboard"],
    "Quantity": [1, 2, 1, 1, 3, 3, 1, 2],
    "Unit_Price": [150000, 2500, 4500, 35000, 2500, 2500, -150000, 4500],
    "City": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi", "Karachi", None, "Lahore"],
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)

print("Dataset created successfully!")
print(df)
