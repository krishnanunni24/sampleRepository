import pandas as pd

# ---------------------------------------------------------
# 1. LOAD DATASET
# ---------------------------------------------------------
sales_data = [
    {"OrderID": "ORD001", "ProductName": "Keyboard", "Category": "Accessories", "Region": "South", "Quantity": 2, "UnitPrice": 750, "UnitCost": 500},
    {"OrderID": "ORD002", "ProductName": "Mouse", "Category": "Accessories", "Region": "South", "Quantity": 3, "UnitPrice": 400, "UnitCost": 220},
    {"OrderID": "ORD003", "ProductName": "Monitor", "Category": "Electronics", "Region": "West", "Quantity": 1, "UnitPrice": 8500, "UnitCost": 6900},
    {"OrderID": "ORD004", "ProductName": "Keyboard", "Category": "Accessories", "Region": "North", "Quantity": 1, "UnitPrice": 750, "UnitCost": 500},
    {"OrderID": "ORD005", "ProductName": "Laptop Stand", "Category": "Accessories", "Region": "East", "Quantity": 2, "UnitPrice": 1200, "UnitCost": 800},
    {"OrderID": "ORD006", "ProductName": "Mouse", "Category": "Accessories", "Region": "South", "Quantity": 0, "UnitPrice": 400, "UnitCost": 220},
    {"OrderID": "ORD007", "ProductName": "Monitor", "Category": "Electronics", "Region": "West", "Quantity": 1, "UnitPrice": -8500, "UnitCost": 6900},
    {"OrderID": "ORD008", "ProductName": "Webcam", "Category": "Electronics", "Region": "North", "Quantity": 2, "UnitPrice": 1800, "UnitCost": 1200},
]

# Note: If loading from an actual file, use: df = pd.read_csv('sales.csv')
df = pd.DataFrame(sales_data)

print("=" * 50)
print("1. DATASET INSPECTION")
print("=" * 50)
print("Data Types & Non-Null Counts:")
df.info()

print("\nDataset Preview:")
print(df)

# ---------------------------------------------------------
# 2. MISSING VALUES & DUPLICATES CHECK
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("2. MISSING VALUES & DUPLICATE RECORDS")
print("=" * 50)
print("Missing values per column:")
print(df.isnull().sum())

print(f"\nDuplicate rows count: {df.duplicated().sum()}")
print(f"Duplicate OrderIDs count: {df.duplicated(subset=['OrderID']).sum()}")

# ---------------------------------------------------------
# 3. IDENTIFY INVALID RECORDS
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("3. ANOMALY & INVALID RECORD DETECTION")
print("=" * 50)

# Check for zero or negative quantities
invalid_qty = df[df['Quantity'] <= 0]
print(f"Invalid Quantity Records ({len(invalid_qty)} found):")
print(invalid_qty[['OrderID', 'ProductName', 'Quantity']])

# Check for negative or zero unit prices
invalid_price = df[df['UnitPrice'] <= 0]
print(f"\nInvalid UnitPrice Records ({len(invalid_price)} found):")
print(invalid_price[['OrderID', 'ProductName', 'UnitPrice']])

# ---------------------------------------------------------
# 4. DECISION & DATA CLEANING
# ---------------------------------------------------------
print("\n" + "=" * 50)
print("4. CLEANING DECISION & EXECUTION")
print("=" * 50)

"""
CLEANING STRATEGY:
- ORD006: Quantity = 0. Zero-item orders generate 0 sales volume/revenue and distort order metrics.
- ORD007: UnitPrice = -8500. Negative prices indicate an input error or an unhandled return, skewing revenue downwards.
- ACTION: Filter out records where Quantity <= 0 OR UnitPrice <= 0 to create a valid analysis pipeline.
"""

cleaned_df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)].copy()

print(f"Original Records Count: {len(df)}")
print(f"Cleaned Records Count:  {len(cleaned_df)}")
print("\nFinal Cleaned Dataset:")
