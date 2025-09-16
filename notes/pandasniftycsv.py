import pandas as pd

nifty_data=pd.read_csv("D:/365-Day-Data-AI-Roadmap/notes/nifty_sample.csv")
print(nifty_data)#loads the data
print(nifty_data.head())#first 5 rows 
print(nifty_data.tail())#last 5
missing_values=nifty_data.isnull().sum()#used for findig missing values 
print(missing_values)

#Select only Date and Close columns.
new_col=nifty_data[['Date','Close']]
print(new_col)

#Extract first 10 rows of Close column as a Series.

column=nifty_data['Close']
print(column.head(10))

#Print dataset shape & column names

print(nifty_data.shape)
print(nifty_data.columns)
#fancy indexing
import pandas as pd

data = {
    'Product': ['A', 'B', 'A', 'C'],
    'Sales': [150, 200, 180, 220],
    'Region': ['North', 'South', 'North', 'West'],
    'CustomerID': [1, 2, 1, 3]
}
df = pd.DataFrame(data)

#reordered_df that
#  contains only the CustomerID and Product columns, in that specific order.
reordered_df=df[['CustomerID','Product']]
print(reordered_df)

## Next: MultiIndex (Hierarchical Indexing)

import pandas as pd
import numpy as np

# Create tuples for our index levels
index_tuples = [
    ('Group A', 'Item 1'), ('Group A', 'Item 2'),
    ('Group B', 'Item 1'), ('Group B', 'Item 2')
]
# Create the MultiIndex
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Group', 'Item'])

# Create a DataFrame with this index
df_multi = pd.DataFrame(np.random.rand(4, 2), index=multi_index, columns=['Value A', 'Value B'])

print("DataFrame with MultiIndex:\n", df_multi)

# --- Selecting Data ---
# Select an entire outer group
print("\nSelecting 'Group A':\n", df_multi.loc['Group A'])

# The data for the index and values
index_data = [
    ('Q1', 'Laptops'), ('Q1', 'Monitors'),
    ('Q2', 'Laptops'), ('Q2', 'Monitors')
]
sales_data = [500, 200, 550, 225]

multi_index=pd.MultiIndex.from_tuples(index_data, names=['Quarter','Products'])
sales_series=pd.Series(index=multi_index,data=sales_data)
print(sales_series.loc['Q1'])

# 1. Create a MultiIndex from 'index_data'. Name the levels 'Quarter' and 'Product'.
# 2. Create a Series named 'sales_series' using the sales_data and your new MultiIndex.
# 3. Select all the data for 'Q1'.