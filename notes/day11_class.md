What is OOP?:
     OOP stands for Object-Oriented Programming.
     Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP:
    Provides a clear structure to programs
    Makes code easier to maintain, reuse, and debug
    Helps keep your code DRY (Don't Repeat Yourself)
    Allows you to build reusable applications with less code

What are Classes and Objects?
    Classes and objects are the two core concepts in object-oriented programming.
    A class defines what an object should look like, and an object is created based on that class. For example:  
Classes vs Instances
    Classes allow you to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.  3
    While the class is the blueprint, an instance is an object that’s built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.
    you can create many instances from a single class.

Class Definition:
    You start all class definitions with the class keyword, then add the name of the class and a colon. Python will consider any code that you indent below the class definition as part of the class’s body.

the built-in __init__() method: (example01)
    All classes have a method called __init__(), which is always executed when the class is being initiated.
    Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:
    You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. When you create a new class instance, then Python automatically passes the instance to the self parameter in .__init__() so that Python can define the new attributes on the object

Attributes created in .__init__() are called instance attributes.:
     An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.

 class attributes :
     are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().

Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.

How Do You Instantiate a Class in Python?:
   Creating a new object from a class is called instantiating a class. You can create a new object by typing the name of the class, followed by opening and closing parentheses:

