import pandas as pd
import numpy as np

# Original data dictionary
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)

# Rename columns using a function
def rename_col(col_name):
    mapping = {
        'First Name': 'first_name',
        'Age': 'age'
    }
    return mapping.get(col_name, col_name)  # Return new name if in mapping, else original

df.rename(columns=rename_col, inplace=True)

# Print first 3 rows
print("First 3 rows of the DataFrame:")
print(df.head(3), "\n")

# Calculate mean age
mean_age = df['age'].mean()
print(f"Mean age of individuals: {mean_age}\n")

# Select and print only 'first_name' and 'City' columns
print("Selected columns (first_name and City):")
print(df[['first_name', 'City']], "\n")

# Add a new column 'Salary' with random salary values (e.g. between 50000 and 100000)
np.random.seed(0)  # For reproducible results
df['Salary'] = np.random.randint(50000, 100001, size=len(df))

# Display updated DataFrame
print("DataFrame with new 'Salary' column:")
print(df, "\n")

# Display summary statistics of the DataFrame
print("Summary statistics:")
print(df.describe(include='all'))


#Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
import pandas as pd

# Create the DataFrame with the given data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

print("Sales and Expenses DataFrame:")
print(sales_and_expenses, "\n")

# Calculate maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

print(f"Maximum Sales: {max_sales}")
print(f"Maximum Expenses: {max_expenses}\n")

# Calculate minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

print(f"Minimum Sales: {min_sales}")
print(f"Minimum Expenses: {min_expenses}\n")

# Calculate average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print(f"Average Sales: {avg_sales:.2f}")
print(f"Average Expenses: {avg_expenses:.2f}")


#Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
import pandas as pd

# Create the DataFrame with given data
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Set 'Category' as the index
expenses = expenses.set_index('Category')

print("Expenses DataFrame with 'Category' as index:")
print(expenses, "\n")

# Calculate max expense for each category (row-wise max)
max_expense = expenses.max(axis=1)
print("Maximum expense for each category:")
print(max_expense, "\n")

# Calculate min expense for each category (row-wise min)
min_expense = expenses.min(axis=1)
print("Minimum expense for each category:")
print(min_expense, "\n")

# Calculate average expense for each category (row-wise mean)
avg_expense = expenses.mean(axis=1)
print("Average expense for each category:")
print(avg_expense)
