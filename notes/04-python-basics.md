What Is a Function?
A function is a reusable block of code that performs a specific task. It helps organize your program, avoid repetition, and improve readability.
Python uses the def keyword to define a function—short for “define.”
def function_name(parameters):
    """Optional docstring describing the function."""
    # Code block (body)
    return result  # Optional
def: Starts the function definition.
function_name: A valid identifier (no spaces, starts with a letter).
parameters: Optional inputs (can be zero or more).
return: Optional keyword to send back a result.

def greet():
    print("Hello, Nilesh!")
greet()  # Output: Hello, Nilesh!

Function with Parameters
python

def add(a, b):
    return a + b
result = add(3, 5)  # result = 8

Why Use Functions?
✅ Modularity: Break your code into logical chunks.

✅ Reusability: Call the same logic multiple times.

✅ Maintainability: Easier to debug and update.

✅ Abstraction: Hide complexity behind a simple interface.

🔹 Pro Tip from PY4E
The course emphasizes functions as a way to implement the "store and use later" pattern—write once, use many times. It’s a core concept for building scalable, readable code.

min() → Returns the smallest item.

max() → Returns the largest item.

Works with numbers, strings, lists, tuples, and other iterables.

🔹 Syntax
python
min(arg1, arg2, ...)
max(arg1, arg2, ...)

min(iterable)
max(iterable)
🔹 Examples
python
min(3, 7, 2)               # → 2
max([10, 25, 5])           # → 25
min("nilesh", "mukati")    # → "mukati" (alphabetical order)
🔹 Rules to Remember
Rule	Explanation
✅ Type Consistency	All arguments must be of comparable types (e.g., all numbers or all strings).
✅ Lexicographic for Strings	Strings are compared alphabetically ("apple" < "banana").
✅ Use key for Custom Logic	Example: max(names, key=len) returns longest name.
✅ Use default for Empty Iterables	Prevents errors: min([], default=0) returns 0.
❌ Don’t Print the Function Object	print(min) shows the function, not the result. Use print(min(...)).
🔹 Bonus: With key Argument
python
names = ["Nilesh", "Amit", "Zoya"]
max(names, key=len)   # → "Nilesh"
🔹 Common Mistake
python
min("nilesh", "mukati")
print(min)  # ❌ Prints function object

# ✅ Correct:
print(min("nilesh", "mukati"))  

A parameter is a variable which
we use in the function
definition. It is a "handle" that
allows the code in the function
to access the arguments for a
particular function invocation.


Return Values
Often a function will take its arguments, do some computation, and
return a value to be used as the value of the function call in the
calling expression. The return keyword is used for this.

boolean Values
While the integer, floating-point, and string data types have an unlimited number of possible values, the Boolean data type has only two values: True and False
you can use Boolean values in expressions and store them in variables

Comparison Operators
Comparison operators, also called relational operators, compare two values and evaluate down to a single Boolean value. Table 2-1 lists the comparison operators.

Table 2-1: Comparison Operators

Operator
Meaning
Examples
==
Equal to
5 == 5 evaluates to True. 4 == 2 + 2 evaluates to True.
!=
Not equal to
1 != 2 evaluates to True. 'Hello' != 'Hello' evaluates to False.
<
Less than
10 < 5 evaluates to False. 1.999 < 5 evaluates to True.
>
Greater than
1 + 1 > 4 + 8 evaluates to False. 99 > 4 + 8 evaluates to True.
<=
Less than or equal to
4 <= 5 evaluates to True. 5 <= 5 evaluates to True.
>=
Greater than or equal to
5 >= 4 evaluates to True. 5 >= 5 evaluates to True.
Boolean Operators
The three Boolean operators (and, or, and not) are used to compare Boolean values. Like comparison operators, they evaluate these expressions down to a Boolean value. Let’s explore these operators in detail, starting with the and operator.

The and operator always takes two Boolean values (or expressions), so it’s considered to be a binary Boolean operator. The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False. Enter some expressions using and into the interactive shell to see it in action:

>>> True and True
True
>>> True and False
False

Like the and operator, the or operator also always takes two Boolean values (or expressions), and therefore is considered to be a binary Boolean operator. However, the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False:

>>> False or True
True
>>> False or False
False
Like the and operator, the or operator also always takes two Boolean values (or expressions), and therefore is considered to be a binary Boolean operator. However, the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False:

>>> False or True
True
>>> False or False
False

Unlike and and or, the not operator operates on only one Boolean value (or expression). This makes it a unary operator. The not operator simply evaluates to the opposite Boolean value:

>>> not True
False
❶ >>> not not not not True
True

Mixing Boolean and Comparison Operators
Since the comparison operators evaluate to Boolean values, you can use them in expressions with the Boolean operators.

Recall that the and, or, and not operators are called Boolean operators because they always operate on the Boolean values True and False. While expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values. Try entering some Boolean expressions that use comparison operators into the interactive shell:

>>> (4 < 5) and (5 < 6)
True
>>> (4 < 5) and (9 < 6)
False
>>> (1 == 2) or (2 == 2)
True
The computer will evaluate the left expression first, and then it will evaluate the right expression. When it knows the Boolean value for each, it will evaluate the whole expression down to one Boolean value. 

Python evaluates the not operators first, then the and operators, and then the or operators.