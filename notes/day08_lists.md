• Algorithms
 A set of rules or steps used to solve a problem
• Data Structures
•A particular way of organizing data in a computer

• List constants are surrounded by
square brackets and the elements
in the list are separated by
commas
• A list element can be any Python
object - even another list
• A list can be empty

• Strings are "immutable" - we
cannot change the contents of a
string - we must make a new string
to make any change
• Lists are "mutable' - we can
change an element of a list using
the index operator

• The range function returns
a list of numbers that range
from zero to one less than
the parameter
• We can construct an index
loop using for and an
integer iterator

The range() function is a powerful tool in Python used to generate a sequence of numbers.

Its main use is to control for loops, allowing you to repeat a block of code a specific number of times.

How range() Works
range() can be used in three ways:

1. range(stop)
This generates numbers starting from 0 up to, but not including, the stop number.
2.2. range(start, stop)
This generates numbers from the start number up to, but not including, the stop number.
3. range(start, stop, step)
This generates numbers from start to stop, incrementing by the step value each time.

Main Uses of range()
Repeating an action a set number of times.
If you need to do something exactly 10 times, range(10) is the perfect tool.

Accessing list elements by index.
You can combine range() with len() to get the index for each element in a list.

Key takeaway: range() doesn't actually store all the numbers in memory. It's a "lazy" generator that produces each number as you need it, which makes it very efficient for working with large sequences.

 We can create an empty list
and then add elements using
the append method
• The list stays in order and
new elements are added at
the end of the list

• Python provides two operators
that let you check if an item is
in a list
• These are logical operators
that return True or False
• They do not modify the list

A list can hold many
items and keeps those
items in the order until we
do something to change
the order
• A list can be sorted
(i.e., change its order)
• The sort method (unlike in
strings) means "sort
yourself"

Split breaks a string into parts and produces a list of strings. We think of these
as words. We can access a particular word or loop through all the words.

