 (## Day 2: Data Types and Input).
 constants; Fixed values such as numbers, letters, and strings, are called
"constants" because their value does not change
Numeric constants are as you expect
String constants use single quotes (*)
or double quotes (")

Variable; their value are choosed by programmer, temporary store value can be changed later in the statment.
example; a=1;

Python Variable Name Rules
Must start with a letter or underscore _
Must consist of letters, numbers, and underscores
Case Sensitive
Good:spam  eggs  spam23
Bad:23spam  #sign  var.12
Different:spam  Spam  SpAm

Operator Precedence Rules
Highest precedence rule to lowest precedence rule:
• Parentheses are always respected
• Exponentiation (raise to a power)
• Multiplication, Division, and Remainder
• Addition and Subtraction
• Left to right

 Parenthesis
Power
Multiplication
Addition
Left to Right


Types of data
• In Python variables, literals, and
constants have a "type"
• Python knows the difference between
an integer number and a string
• For example "+" means "addition" if
something is a number and
"concatenate" if something is a string

type() is indeed a built-in function in Python. It’s used to determine the data type of a value or variable.

In Python, a function is a reusable block of code designed to perform a specific task. Think of it like a mini-program within your program—it helps you organize your logic, avoid repetition, and make your code cleaner and easier to understand.


 input() function always gives you a string (text)


The * operator multiplies two integer or floating-point values. But when the * operator is used on one string value and one integer value, it becomes the string replication operator. Enter a string multiplied by a number into the interactive shell to see this in action:

>>> 'Alice' * 5
'AliceAliceAliceAliceAlice'

The len() Function
You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string:

print('The length of your name is:')
print(len(my_name))
Enter the following into the interactive shell to try this:

>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.')
46
>>> len('')
0


The str() function can be passed an integer value and will return a string value version of the integer, as follows:

>>> str(29)
'29'
>>> print('I am ' + str(29) + ' years old.')
I am 29 years old.


The round() function accepts a float value and returns the nearest integer. Enter the following into the interactive shell:

>>> round(3.14)
3
>>> round(7.7)
8
>>> round(-2.2)
-2

The round() function also accepts an optional second argument specifying how many decimal places it should round. Enter the following into the interactive shell:

>>> round(3.14, 1)
3.1
>>> round(7.7777, 3)
7.778
The behavior for rounding half numbers is a bit odd. The function call round(3.5) rounds up to 4, while round(2.5) rounds down to 2. For halfway numbers that end with .5, the number is rounded to the nearest even integer. This is called banker’s rounding.

The abs() function returns the absolute value of the number argument. In mathematics, this is defined as the distance from 0, but I find it easier to think of it as the positive form of the number. Enter the following into the interactive shell:

>>> abs(25)
25
>>> abs(-25)
25
>>> abs(-3.14)
3.14
>>> abs(0)
0

So, while expressions are like math problems that give you an answer, statements are like instructions that tell Python what to do.

