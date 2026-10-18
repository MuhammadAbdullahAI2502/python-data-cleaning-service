
# Python Data Cleaning & Sales Analysis

## Overview
A Python project that cleans sales data, identifies data-quality
issues, analyzes revenue, generates charts, and exports reports
to an Excel workbook.

## Features
- Detects missing values and duplicate records
- Identifies negative prices for review
- Cleans duplicate rows and handles missing city values
- Calculates revenue by product and city
- Generates product and city revenue charts
- Exports product and city reports to Excel

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL

## Project Files
- `create_dataset.py` — creates sample sales data
- `audit_data.py` — checks data quality
- `clean_data.py` — cleans the dataset
- `sales_analysis.py` — analyzes sales and revenue
- `sales_visualization.py` — creates charts
- `create_excel_report.py` — exports Excel reports
- `sales_data.csv` — original sample data
- `sales_data_cleaned.csv` — cleaned dataset
- `product_sales_report.csv` — product-level report
- `Sales_Analysis_Report.xlsx` — Excel workbook
- `revenue_by_product.png` — product revenue chart
- `revenue_by_city.png` — city revenue chart

## How to Run
Install the required libraries:

```bash
python -m pip install pandas numpy matplotlib openpyxl
```

Run the scripts in this order:

1. `python create_dataset.py`
2. `python audit_data.py`
3. `python clean_data.py`
4. `python sales_analysis.py`
5. `python sales_visualization.py`
6. `python create_excel_report.py`

## Data Note
This project uses sample data, not real customer records.
Negative prices are excluded from revenue calculations but
preserved in the cleaned dataset for further review.

## Purpose
Demonstrates practical Python data cleaning, analysis,
visualization, and Excel reporting skills.
