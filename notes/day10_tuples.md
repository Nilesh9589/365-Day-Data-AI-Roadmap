Tuples:
      Tuples are used to store multiple items in a single variable.
      Tuple is one of 4 built-in data types in Python used to store collections of data
      A tuple is a collection which is ordered and unchangeable.
      Tuples are written with round brackets.(example01)
Tuple Items:
      Tuple items are ordered, unchangeable, and allow duplicate values.(example2)
      Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Unchangeable:
      Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.      
Allow Duplicates:
      since tuples are  indexed, they can have items with the same value:      
Tuple Length:
      To determine how many items a tuple has, use the len() function:  (example03)    

Create Tuple With One Item:
      To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple. (example 04)
The tuple() Constructor:
      It is also possible to use the tuple() constructor to make a tuple.(example 05)

Access Tuple Items:
      You can access tuple items by referring to the index number, inside square brackets:

Range of Indexes:
      You can specify a range of indexes by specifying where to start and where to end the range.
      When  specifying a range, the return value will be a new tuple with the specified items.(example 06)

Check if Item Exists:
      To determine if a specified item is present in a tuple use the in keyword (example 07)
Unpacking a Tuple:
      When we create a tuple, we normally assign values to it. This is called "packing" a tuple:        
      But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":          (example08)
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect   the remaining values as a list.

Using Asterisk*:
      If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:(example 09)

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.(example 10)

Loop Through a Tuple:
      You can loop through the tuple items by using a for loop.(example 11)

Loop Through the Index Numbers:    (example12 )
      You can also loop through the tuple items by referring to their index number.
      Use the range() and len() functions to create a suitable iterable.

Using a While Loop:  (example 13)
      You can loop through the tuple items by using a while loop.