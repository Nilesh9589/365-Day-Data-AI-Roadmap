String Data Type
• A string is a sequence of characters
• A string literal uses quotes
"Hello' or "Hello"
• For strings, + means "concatenate"
• When a string contains numbers, it is
still a string
• We can convert numbers in a string
into a number using int()
• We can get at any single character in a
string using an index specified in
square brackets
• The index value must be an integer
and starts at zero
• The index value can be an expression
that is computed

Looping Through Strings

Using a while statement
and an iteration variable,
and the len function, we
can construct a loop to
look at each of the letters
in a string individually


Looping Through Strings
• A definite loop using a
for statement is much
more elegant
• The iteration variable is
completely taken care of
by the for loop

Slicing Strings
• We can also look at any
continuous section of a string
using a colon operator
• The second number is one
beyond the end of the slice -
"up to but not including"
• If the second number is
beyond the end of the string,
it stops at the end

If we leave off the first number or
the last number of the slice, it is
assumed to be the beginning or
end of the string respectively


• The in keyword can also be
used to check to see if one
string is "in" another string
• The in expression is a
logical expression that
returns True or False and
can be used in an if
statement

• Python has a number of string
functions which are in the
string library
• These functions are already
built into every string - we
invoke them by appending the
function to the string variable
• These functions do not modify
the original string, instead the
return a new string that has
been altered