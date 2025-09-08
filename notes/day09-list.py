#list[start:stop:step]
nums = [10,20,30,40,50,60]

nums[1:4]   # → [20, 30, 40]  (start=1 inclusive, stop=4 exclusive)
nums[:3]    # → [10, 20, 30]  (start defaults to 0)
nums[3:]    # → [40, 50, 60]  (stop defaults to end)
nums[::3]   # → [10, 30, 50]  (every 2nd item, step=2)
nums[::-1]  # → [60, 50, 40, 30, 20, 10] (reverse)

#Lists are mutable — you can change their contents without creating a new list.

a = [1, 2, 3]
b = a         # b references the same list object as a
b[0] = 99
print(a)      # → [99, 2, 3]  (a changed because b and a are the same object)
#Function example (mutability in functions):
def add_item(x):
    x.append(100)

lst = [1,2]
add_item(lst)
print(lst)   # → [1, 2, 100]  (function modified original list)

#Nested lists — lists inside lists (like a 2D grid) 
# Imagine a bookshelf where each slot contains another small shelf.

matrix = [
  [1,2,3],   # row 0
  [4,5,6],   # row 1
  [7,8,9]    # row 2
]

print(matrix[1][2])  # → 6  (row 1, column 2)


##Beware: inner lists are full Python objects. If multiple references point to the same inner list, changing it via one reference affects all.

squares = [x*x for x in range(6)]

print(squares)


#even  with if condition
evens = [x for x in range(10) if x % 2 == 0]
print (evens)
# step-by-step:
# for x in 0..9:
#   if x%2==0 -> append x

#if else conditiom
labels = ["even" if x%2==0 else "odd" for x in range(5)]

#Nested comprehension (flatten a matrix):

matrix = [[1,2],[3,4]]
print(matrix)
flat = [v for row in matrix for v in row]   # [1,2,3,4]
# equivalent to nested loops:
# for row in matrix:
#   for v in row:
#       flat.append(v)

FRIENDS=[['AISH','BHUSHAN'],[1,2]]

COMLIST=[c for name in FRIENDS for c in name] #[ The Final Action for The First Loop for The Second Loop ]
print(COMLIST)

"""#grade_matrix = [
    [85, 92, 88],
    [78, 81, 86],
    [90, 94, 89]
]"""
#Can you write a comprehension that collects only the grades above 90 into a flat list?
grade_matrix = [
    [85, 92, 88],
    [78, 81, 86],
    [90, 94, 89]]
for grade in grade_matrix:
    for check in grade:
    
     if check>90 :
        
      print(check)

newscore=[check for grade in grade_matrix for check in grade if check>90  ]
print(newscore)
#pratice 
sentencelist = ["python", "java", "c", "golang", "r", "rust"]

updatedlist=[word.upper()    if len(word)>3 and 'o' in word   else word.lower()  for word in sentencelist ]

print(updatedlist)
# practice

numbers = [5, 12, 7, 20, 33, 40]
for key in numbers:
   if key%2==0:
    print (key)

dictionarys=[key if key%2==0  else (key*key*key) for key in numbers ]    
print(dictionarys)

#practice


"""If the number is divisible by both 2 and 3 → return "FIZZBUZZ"

If only divisible by 2 → return "FIZZ"

If only divisible by 3 → return "BUZZ"

Otherwise → return the number itself"""

numbers = [10, 15, 21, 28, 33, 42, 55, 60]
aftermath=["FIZZBUZZ" if check %3==0 and check %2==0 else 'FIZZ' if check%2==0 else "BUZZ" if check%3==0 else check for check in numbers]
aftermath.reverse()
print(aftermath)
