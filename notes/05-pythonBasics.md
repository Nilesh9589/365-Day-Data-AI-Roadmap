What is a Function?
A function is a named, reusable block of code that performs a specific task. Think of it as a mini-program or a recipe. You write the code once and can then call it by name whenever you need it, which helps you avoid repeating yourself (the DRY principle).

The Two Parts: Definition and Call
Every function has two parts: you must first define it, then you can call it.

1. The Definition (The Blueprint)
This is where you create the function and give it its instructions.

It starts with the def keyword.

Parameters are the placeholders for the ingredients the function needs to work.

Python

# 'name' and 'age' are parameters (placeholders)
def create_greeting(name, age):
    message = f"Hello {name}, you are {age} years old."
    return message
2. The Call (Running the Code)
This is where you execute the function and give it real data.

Arguments are the actual values you pass into the function's parameters.

Python

# "Nilesh" and 30 are arguments (actual values)
greeting = create_greeting("Nilesh", 30)
print(greeting)
The Golden Rules of Functions
These are the most important rules to remember to avoid common mistakes.

The Call Must Match the Definition. The number of arguments in your function call must match the number of parameters in its def line. If the recipe needs two ingredients, you must provide two.

Arguments Must Have the Right Data Type. If a function expects a number (e.g., if age > 18:), you must give it a number. Always remember to convert user input from a string to the correct type (e.g., int() or float()) before passing it to the function.

You Must Use a return Value. If a function returns a value, it sends that value back to your program. Your program then needs to do something with it—either store it in a variable or print() it to the screen. The program won't do anything with a returned value automatically.

print vs. return: The Final Showdown
This is the most critical concept to master.

print is for the USER. It displays information on the screen. Your program cannot use this information for any other steps. It's a "dead end" for data.

return is for the PROGRAM. It gives a value back to your code so it can be used in the next step (like another calculation or function). It's a "building block" for creating more complex programs.

Indefinite Loops
• While loops are called "indefinite loops" because they keep
going until a logical condition becomes False
• The loops we have seen so far are pretty easy to examine to see
if they will terminate or if they will be "infinite loops"
• Sometimes it is a little harder to be sure if a loop will terminate


Definite Loops
• Quite often we have a list of items of the lines in a file -
effectively a finite set of things
• We can write a loop to run the loop once for each of the items in
a set using the Python for construct
• These loops are called "definite loops" because they execute an
exact number of times
• We say that "definite loops iterate through the members of a set"
