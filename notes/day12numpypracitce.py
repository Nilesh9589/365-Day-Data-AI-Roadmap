import numpy as np

# Sales for each day of the week
sales_data = np.array([50, 65, 82, 48, 95, 110, 76])

# 1. Calculate the total sales for the week.
# 2. Find the maximum number of sales in a single day.
# 3. Find the index of the day with the highest sales (0=Monday, 1=Tuesday, etc.).
print(f'total sales for the week is {sales_data.sum()}')
print(f'the maximum number of sales in a single day {sales_data.max()}')


print(f"the index of the day with the highest sales {np.argmax(sales_data)}  ")

import numpy as np

# A small 4x4 grayscale image
image_pixels = np.array([
    [15,  80,  210, 240],
    [45,  225, 180, 190],
    [90,  195, 255, 10],
    [230, 50,  120, 160]
])

# 1. Create a new array containing only the bright pixels (> 200).
# 2. Count how many bright pixels there are.

new_array=image_pixels[image_pixels>200]
print(f"new array containing only the bright pixels (> 200). {new_array}")
count=0
for i in new_array: 
    count=count+1
print(f"bright pixels there are:{count}")
print(f"bright pixels there are:{new_array.size}")

import numpy as np

# Temperature readings for a day
temperatures = np.array([25.2, 25.4, -999, 26.1, 26.5, 24.9, -999, 27.0])

# 1. Create a "clean" array that excludes all the -999 values.
#    (Hint: You want the values that are NOT equal to -999. The operator for "not equal" is !=)
#
# 2. Calculate the average temperature from the "clean" array.
new=[]
for check in temperatures:
    if check !=-999:
         new.append(check)
cleanlist=np.array(new)
print(cleanlist)

sorted_array=temperatures[temperatures!=(-999)]
print(sorted_array)
print(sorted_array.mean())

import numpy as np

# Current (x, y) positions of 3 players
player_positions = np.array([
    [10, 20],  # Player 0
    [50, 60],  # Player 1
    [80, 90]   # Player 2
])

# Movement vectors (dx, dy) for each player
movement_vectors = np.array([
    [1, -1],   # Player 0 moves right and down
    [-2, 0],   # Player 1 moves left
    [0, 3]    # Player 2 moves up
])

# 1. Calculate the new positions of all players by adding their
#    current positions to their movement vectors.
newpostion =player_positions+movement_vectors
print(newpostion)

#normalized_value = (value - min_value) / (max_value - min_value)
#Task: Apply this formula to an entire array of house prices using NumPy's vectorization.

import numpy as np

house_prices = np.array([150000, 250000, 180000, 500000, 320000])

# 1. Find the minimum and maximum prices from the array.
#
# 2. Apply the normalization formula to the entire array in a single line
#    to create a new 'normalized_prices' array.
max=house_prices.max()
min=house_prices.min()
print(f"the max of this array is {max} and the min is {min}")
normalized=(house_prices-min)/(max-min)
print(normalized)

#diagonal extraction
import numpy as np

# Create a sample 3x3 matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Use np.diag() to extract the diagonal elements
diagonal = np.diag(matrix)

print("Original Matrix:\n", matrix)
print("\nDiagonal Elements:", diagonal)

# You can then perform operations on it, like finding the trace
print("Sum of the diagonal (the Trace):", diagonal.sum())