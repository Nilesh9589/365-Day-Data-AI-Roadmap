# The standard way to import NumPy
import numpy as np


my_list=[10,20,45,920,8481]
my_array = np.array(my_list)
print(f'this is the numpy array {my_array}')
print(f"this is of type {type(my_array)}")
print(f"its shape is {my_array.shape}")

#example 2 

import numpy as np
# A list containing two inner lists
my_2d_list=[[1,2,3],
            [4,5,6]]
#create a 2d numpy array 

my2d_array=np.array(my_2d_list)

print(f'this is the 2d array {my2d_array}')
print(f'its shape is {my2d_array.shape}')
print(f'the number of dimension is {my2d_array.ndim}')

#np.zeros(): Creates an array filled with zeros.

zeroes_array=np.zeros((2,4))
print(f"zero array :{zeroes_array}")

#np.ones(): Creates an array filled with ones.
ones_array=np.ones((3,2))
print(f"ones array :{ones_array}")

#np.arange(): NumPy's version of Python's range(). Creates an array with a sequence of numbers.
sequence_array=np.arange(10)  # Create an array from 0 to 9
print(f'this is the seuqunce array: {sequence_array}')

# Create a 3x3 matrix (a 2D array) where all the values are 9.

ones_array=np.ones((3,3))
nines_array=ones_array+8
print(nines_array)

#another way
import numpy as np

# np.full((shape), fill_value)
nines_array_alt = np.full((3, 3), 9)

print(nines_array_alt)

### Replacing a Single Element: Indexing

import numpy as np

# 1. Start with a 3x3 array of zeros
arrays=np.zeros((3,3))
print(f'orignal array:{arrays}')
# 2. Change the element at row 0, column 1 to a 9
arrays[0,1]=9
print(f'array after changing the element :{arrays}')
# 3. Let's change the bottom-right corner (row 2, column 2)
arrays[2,2]=9
print(f'array after changing the element :{arrays}')
"""The square brackets [] are used for indexing into the array to access and modify its values. So, when you write:
my_array[0, 1] = 9
You are saying, "Go into the mutable my_array object and change the value at location [0, 1]."""

## Slicing: Selecting Parts of an Array
#The format is array[row_slice, column_slice]

import numpy as np
# Create a sample 3x4 array (3 rows, 4 columns)
sample_array = np.arange(12).reshape((3, 4))
print("Original Array:\n", sample_array)

# 1. Get an entire row (e.g., the second row, index 1)
row = sample_array[1]
print("\nSecond row:\n", row)

# 2. Get an entire column (e.g., the third column, index 2)
# The ':' for the rows means "get all rows"
column = sample_array[:, 2]
print("\nThird column:\n", column)

# 3. Get a sub-grid (rows 0 and 1, columns 1 and 2)
sub_grid = sample_array[0:2, 1:3]
print("\nSub-grid (2x2):\n", sub_grid)

#From the sample_array created above, write a single line of code to slice and print a new array 
#that contains only the last two rows and the last two columns.
##The format is array[row_slice, column_slice]
last_array=sample_array[1:3, 2:4]
print(f"this is the {last_array}")

#boolean indexing
#The idea is simple: you give NumPy a condition (e.g., "all numbers greater than 5"),
#and it gives you back only the elements that meet that condition.

import numpy as np

arrays=np.array([1,2,3,4,5,6,7,8,9])
# 1. Create a condition. This returns a "mask" of True/False values.
condition_mask=arrays>5
print(f"the boolean mask is {condition_mask}")
# 2. Use the mask to select only the True elements.
filtered_array = arrays[condition_mask]
print(f"The filtered array is: {filtered_array}")

# You can also do it in a single, clean line:
filtered_array_short = arrays[arrays > 5]
print(f"The short way: {filtered_array_short}")
#exercise
import numpy as np

data = np.array([
    [10, 80, 25],
    [95, 45, 60]
])

#num greater than 50

condition_mask=data>50
print(condition_mask)

filtered_array=data[condition_mask]
print(filtered_array)

one_line=data[data>50]
print(one_line)


#operations on array

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Sum of all elements: {arr.sum()}")
print(f"Mean of all elements: {arr.mean()}")
print(f"Max value in the array: {arr.max()}")

# --- Operations along an axis ---
# axis=0 collapses the rows -> operates on columns
print(f"\nSum of each COLUMN: {arr.sum(axis=0)}") # [1+4, 2+5, 3+6]

# axis=1 collapses the columns -> operates on rows
print(f"Sum of each ROW: {arr.sum(axis=1)}") # [1+2+3, 4+5+6]


#Task: First, calculate the mean of each row. Then, find the maximum value among those row means.
data = np.array([
    [10, 20, 30],
    [5, 15, 25],
    [100, 50, 75]
])

print(f"The mean of each row is {data.mean(axis=1)}")

array1d=data.mean(axis=1)
print(f"The max of each row is {array1d.max()}")


#another short way of doingg the same
import numpy as np

data = np.array([
    [10, 20, 30],
    [5, 15, 25],
    [100, 50, 75]
])

# Calculate the mean of each row, and then immediately find the max of that result.
max_of_means = data.mean(axis=1).max()

print(f"The max of the row means is: {max_of_means}")

#linspace conecpt 
import numpy as np
# Create an array of 5 evenly spaced numbers between 0 and 100
# np.linspace(start, stop, num_of_elements)

my_linspace=np.linspace(0,100,5)
print(my_linspace)

#fancy indexing .
import numpy as np
# A sample array of letters (pretend they are data points)
data=np.array(["A","B","C","D","E","F"])
# Use a list to select the elements at indices 0, 3, and 5
indices_to_get = [0, 3, 5]
selected_data = data[indices_to_get]
print(f"The selected data is: {selected_data}")

import numpy as np

# A 2D array with 5 rows
matrix = np.array([
    [1, 2],    # Row 0
    [3, 4],    # Row 1
    [5, 6],    # Row 2
    [7, 8],    # Row 3
    [9, 10]    # Row 4
])

# Task: Use fancy indexing to create a new array containing
# only the first, third, and fourth rows (indices 0, 2, and 3).
indices_to_get=[0,2,3]
new_array=matrix[indices_to_get]
print(new_array)

## Final Concept: Broadcasting

import numpy as np
matrix=np.array([[1,2,3],
                [4,5,6]])
# A 1D array (1 row, 3 columns)
row_to_add = np.array([10, 20, 30])
# Broadcast the addition
result = matrix + row_to_add
print("Matrix shape:", matrix.shape) # (2, 3)
print("Row shape:", row_to_add.shape)  # (3,)
print("\nResult of broadcasting:\n", result)

#mineturn pratice for above
import numpy as np

sales = np.array([
    [100, 110, 120], # Product A's sales for Day 1, 2, 3
    [150, 160, 170]  # Product B's sales for Day 1, 2, 3
])

daily_bonus = np.array([5, 10, 15]) # Bonus for Day 1, 2, 3

# Add the daily_bonus to the sales array.
final=daily_bonus+sales
print(final)