

## Recreating Your Pandas Notes (Day 6 Summary)
Here are the essential concepts from your introduction to Pandas.

1. The Core Idea
Pandas is used for data analysis and manipulation. It's built on NumPy but adds labels (column and row names) to your data.

2. The Main Data Structures
Series: A single column of data.

DataFrame: A full table with rows and columns (the main object you'll use).

3. Loading & Inspecting Data
pd.read_csv('file.csv'): Loads data from a CSV file into a DataFrame.

.head(): Shows the first 5 rows.

.describe(): Gives a statistical summary of numerical columns.

.info(): Provides a full overview of columns, data types, and non-null values.

4. Selecting Data
df['ColumnName']: Selects a single column (returns a Series).

.loc[]: Selects data by its label (the row/column names).

.iloc[]: Selects data by its integer position.

5. Common Operations
Boolean Filtering: df[df['Column'] > 100]

Creating New Columns: df['NewColumn'] = df['OldColumn'] * 2

Combining: pd.concat([df1, df2], ignore_index=True)

Grouping: df.groupby('Category')['Sales'].sum()

