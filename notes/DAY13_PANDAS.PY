##filtering with multiple conditions.

import pandas as pd
import numpy as np

# Our sample dataset
data = {
    'InvoiceNo': ['A001', 'A001', 'A002', 'A003', 'A003', 'A004', 'A005', 'A005'],
    'StockCode': ['P1', 'P2', 'P1', 'P3', 'P4', 'P2', 'P1', 'P4'],
    'Quantity': [10, 5, 8, 3, 2, 5, 12, 15],
    'UnitPrice': [20.0, 50.0, 20.0, 100.0, 150.0, 50.0, 20.0, 150.0],
    'CustomerID': [1, 2, 1, 3, 3, 2, 1, 3],
    'Country': ['UK', 'Germany', 'UK', 'USA', 'USA', 'Germany', 'UK', 'USA']
}
df = pd.DataFrame(data)
print(df)

#  filtering code here

selected_data=df[(df['Country']=='UK') & (df['Quantity']>10)]
print(selected_data)

#.isin() method to check against a list of values.

# Our DataFrame
df

# Create a list of the countries we're interested in
countries_of_interest = ['UK', 'USA']

# Use .isin() to find all rows where the 'Country' is in our list
selected_countries = df[df['Country'].isin(countries_of_interest)]

print(selected_countries)

#Using the same df, create a new DataFrame that contains only the data for StockCode 'P1' and 'P3'.
code_of_interests=['P1','P3']
seletected_code=selected_countries[selected_countries['StockCode'].isin(code_of_interests)]
print(seletected_code)

# Using our sample DataFrame
df

# Group by 'Country' and calculate two different stats:
# - The total sum of 'Quantity'
# - The average 'UnitPrice'
summary_df = df.groupby('Country').agg({
    'Quantity': 'sum',
    'UnitPrice': 'mean'
})

print(summary_df)

itempurandaverage_df=df.groupby('CustomerID').agg({
    'Quantity': "sum",
    'UnitPrice': 'mean'
   

})
print(itempurandaverage_df)

import pandas as pd

# DataFrame of students
students_df = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

# DataFrame of grades (notice student 3 has no grade, and grade 4 has no student)
grades_df = pd.DataFrame({
    'student_id': [1, 2, 4],
    'grade': ['A', 'B', 'C']
})

# An INNER merge only keeps students 1 and 2, who are in BOTH tables
inner_merge = pd.merge(students_df, grades_df, on='student_id', how='inner')
print("--- Inner Merge ---\n", inner_merge)

# A LEFT merge keeps ALL students from the left table (students_df)
left_merge = pd.merge(students_df, grades_df, on='student_id', how='left')
print("\n--- Left Merge ---\n", left_merge)



import pandas as pd

customers_df = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'name': ['Nilesh', 'Humid', 'Gennady']
})

orders_df = pd.DataFrame({
    'order_id': [1, 2, 3],
    'customer_id': [101, 103, 101],
    'product': ['Laptop', 'Book', 'Mouse']
})

# Your left merge code here
merged_df = pd.merge(customers_df,orders_df, on='customer_id', how='left' )
print(merged_df)


