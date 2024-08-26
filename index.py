import random

# Create a dictionary of basic Python questions and answers
pythonDict = {
    # variables
    ("what is variable", "tell me about variable", "what is variable in python", "variable", "variables"): ["In Python, a variable is essentially a name that refers to a value stored in the computer's memory", "variable is a reserved memory location to store values.", "variable is like a container where we store data or values","A variable in Python is a named location used to store data in the memory."],
    # data types
    ("data types","how many data types in python", "tell me about data types","what is data types in python","what is data types in python"):["These are basic data types in python: integers, floats, Boolean, and strings.","Python has five standard Data Types: Numbers,String,List,Tuple,Dictionary."],
    # int
    ("what is an int", "explain int data type", "integer type", "int data type", "what is integer"): [
        "An 'int' in Python represents an integer, which is a whole number without a decimal point.",
        "The 'int' data type in Python is used to represent integer values, such as 1, 2, or -3.",
        "An integer (int) is a numeric data type used for whole numbers in Python."
    ],
    # float
    ("what is a float", "explain float data type", "floating-point type", "float data type", "what is float"): [
        "A 'float' in Python represents a floating-point number, which is a number that has a decimal point.",
        "The 'float' data type in Python is used to represent real numbers, such as 3.14, 2.0, or -7.25.",
        "A floating-point number (float) is a numeric data type used for numbers with decimal points."
    ],
    # string
    ("what is a string", "explain str data type", "string type", "str data type", "what is string"): [
        "A 'str' in Python represents a sequence of characters, typically used to store text.",
        "The 'str' data type in Python is used for strings, which are sequences of characters, such as 'hello' or 'Python'.",
        "A string (str) is a data type in Python used for storing text data."
    ],
    # lists
    ("what is a list", "explain list data type", "list type", "list data type", "what is a list in python"): [
        "A 'list' in Python is an ordered collection of items, which can be of different data types. Lists are defined using square brackets, e.g., [1, 2, 3].",
        "The 'list' data type in Python is used to store multiple items in a single variable, like [10, 'Python', True].",
        "A list is a data type in Python that allows you to store multiple values in an ordered sequence."
    ],
    # tuple
    ("what is a tuple", "explain tuple data type", "tuple type", "tuple data type", "what is a tuple in python"): [
        "A 'tuple' in Python is similar to a list, but it is immutable, meaning it cannot be changed after creation. Tuples are defined using parentheses, e.g., (1, 2, 3).",
        "The 'tuple' data type in Python is used to store multiple items in a single variable, but unlike lists, tuples cannot be modified.",
        "A tuple is a data type in Python used for storing a sequence of values that cannot be changed."
    ],
    # dictinary
    ("what is a dictionary", "explain dict data type", "dictionary type", "dict data type", "what is a dictionary in python"): [
        "A 'dict' in Python is a collection of key-value pairs, where each key is unique. Dictionaries are defined using curly braces, e.g., {'key': 'value'}.",
        "The 'dict' data type in Python is used for storing data in key-value pairs, such as {'name': 'Alice', 'age': 25}.",
        "A dictionary (dict) is a data type in Python used for storing data that is indexed by unique keys."
    ],
    # boolean
    ("what is a boolean", "explain bool data type", "boolean type", "bool data type", "what is a bool in python"): [
        "A 'bool' in Python represents a Boolean value, which can be either True or False.",
        "The 'bool' data type in Python is used to represent truth values, typically used in conditional statements.",
        "A boolean (bool) is a data type in Python that has only two possible values: True or False."
    ],
    # Functions
    ("what is a function", "explain function", "function in python", "what is a function in python"): [
        "A function in Python is a block of code that only runs when it is called. Functions are defined using the 'def' keyword.",
        "In Python, a function is used to encapsulate code that performs a specific task. It can be called multiple times with different arguments.",
        "Functions in Python help in organizing code into reusable blocks, defined with the 'def' keyword followed by the function name and parentheses."
    ],
    # define function
    ("how to define a function", "defining a function", "create a function", "how to create a function in python"): [
        "You define a function in Python using the 'def' keyword, followed by the function name and parentheses. For example: def my_function():",
        "To create a function in Python, use the 'def' keyword, followed by the function name and parentheses. Inside the function, you write the code that performs the task.",
        "A function is defined with the 'def' keyword, followed by the function name and a block of code that performs the desired task."
    ],
    # return
    ("what is a return statement", "return statement in python", "function return", "what does return do"): [
        "The 'return' statement is used to exit a function and return a value to the caller. It can be used to send back a result from a function.",
        "In Python, 'return' is used to pass back a result from a function to the code that called the function.",
        "The 'return' statement ends the function execution and optionally passes back a value to the caller."
    ],

    # Loops
    ("what is a loop", "types of loops", "loop in python", "what are loops"): [
        "A loop in Python is a control structure used to repeat a block of code multiple times. The two main types of loops are 'for' and 'while'.",
        "Loops in Python allow you to execute a block of code repeatedly. The 'for' loop is used for iterating over a sequence, while the 'while' loop repeats as long as a condition is true.",
        "Python has two main types of loops: 'for' loops and 'while' loops. They are used to execute code multiple times based on conditions."
    ],
    # for loop
    ("how to use a for loop", "for loop syntax", "example of for loop", "how does for loop work"): [
        "A 'for' loop in Python is used to iterate over a sequence (like a list or a range). Syntax: for item in sequence: # code block",
        "To use a 'for' loop in Python, write 'for' followed by a variable name and 'in' keyword, then the sequence to iterate over.",
        "The 'for' loop allows you to execute a block of code for each item in a sequence, such as a list or a range of numbers."
    ],
    # while loop
    ("how to use a while loop", "while loop syntax", "example of while loop", "how does while loop work"): [
        "A 'while' loop in Python repeats a block of code as long as a condition is true. Syntax: while condition: # code block",
        "To use a 'while' loop, write 'while' followed by a condition and a block of code to execute while the condition is true.",
        "The 'while' loop continues to execute as long as its condition evaluates to true. Be careful to ensure the condition eventually becomes false to avoid infinite loops."
    ],

    # Conditionals
    ("what is an if statement", "if statement in python", "conditional statements", "how to use if statements"): [
        "An 'if' statement in Python is used to execute a block of code if a specified condition is true. Syntax: if condition: # code block",
        "The 'if' statement allows you to run code conditionally based on whether a given condition is true or false.",
        "In Python, 'if' statements are used to make decisions in your code, running specific code blocks based on certain conditions."
    ],
    # elif
    ("what is an elif statement", "elif in python", "elif keyword", "how to use elif"): ["The 'elif' statement in Python stands for 'else if' and allows you to check multiple conditions. It follows an 'if' statement","The “elif” keyword in Python, stands for “else if”. It can be used in conditional statements to check for multiple conditions. For example, if the first condition is false, it moves on to the next “elif” statement to check if that condition is true."],

     # Operators
    ("what is an operator", "explain operators in python", "operators in python", "what are operators"): [
        "An operator in Python is a symbol that performs a specific operation on one or more operands. Common operators include arithmetic, comparison, logical, and assignment operators.",
        "Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.",
        "Python operators are used to perform operations on variables and values. They include arithmetic operators like +, -, *, / and logical operators like and, or, not."
    ],
    # Arithmetic
    ("what is an arithmetic operator", "arithmetic operators", "explain arithmetic operators", "what are arithmetic operators in python"): [
        "Arithmetic operators in Python are used to perform mathematical operations like addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).",
        "Python provides arithmetic operators for performing common mathematical calculations. Examples include + for addition, - for subtraction, * for multiplication, and / for division.",
        "The arithmetic operators in Python include +, -, *, / for basic math operations, as well as % for modulus, ** for exponentiation, and // for floor division."
    ],
    # Comparison
    ("what is a comparison operator", "comparison operators", "explain comparison operators", "what are comparison operators in python"): [
        "Comparison operators in Python are used to compare two values. Common comparison operators include == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).",
        "Python comparison operators allow you to compare two values and return a Boolean result (True or False). Examples include == for equality, != for inequality, and >, < for greater or less than comparisons.",
        "Comparison operators are used in Python to compare two values. These operators return True or False based on the comparison result."
    ],
    # Logical
    ("what is a logical operator", "logical operators", "explain logical operators", "what are logical operators in python"): [
        "Logical operators in Python are used to combine conditional statements. The common logical operators are 'and', 'or', and 'not'.",
        "Python's logical operators include 'and', 'or', and 'not'. They are used to perform logical operations, combining multiple conditions into a single condition.",
        "The logical operators in Python allow you to combine multiple conditions. 'and' returns True if both conditions are true, 'or' returns True if at least one condition is true, and 'not' inverts the Boolean value."
    ],
    # Assignment
    ("what is an assignment operator", "assignment operators", "explain assignment operators", "what are assignment operators in python"): [
        "Assignment operators in Python are used to assign values to variables. The basic assignment operator is =, but there are compound operators like +=, -=, *=, /= that combine assignment with an arithmetic operation.",
        "The assignment operator = in Python is used to assign values to variables. There are also compound assignment operators like +=, -= which perform an operation and assign the result to the variable.",
        "Python uses assignment operators to assign values to variables. Besides the basic = operator, there are others like +=, -= which combine assignment with an arithmetic operation."
    ],
    # bitwise
    ("what is a bitwise operator", "bitwise operators", "explain bitwise operators", "what are bitwise operators in python"): [
        "Bitwise operators in Python are used to perform operations on binary representations of integers. Examples include &, |, ^, ~, <<, and >>.",
        "Python's bitwise operators operate on bits and include &, |, ^ for bitwise AND, OR, and XOR operations, as well as ~ for bitwise NOT, and <<, >> for bitwise shifts.",
        "Bitwise operators perform operations on binary numbers. They include AND (&), OR (|), XOR (^), NOT (~), and shift operators (<<, >>)."
    ],
    # Membership
    ("what is a membership operator", "membership operators", "explain membership operators", "what are membership operators in python"): [
        "Membership operators in Python are used to test whether a value or variable is found in a sequence such as a list, tuple, or string. The operators are 'in' and 'not in'.",
        "Python membership operators include 'in' and 'not in'. They check whether a value is present in a sequence like a list or string.",
        "The 'in' and 'not in' operators in Python are membership operators that test for the presence of a value in a sequence, such as a list, tuple, or string."
    ],
    # Identity
    ("what is an identity operator", "identity operators", "explain identity operators", "what are identity operators in python"): [
        "Identity operators in Python are used to compare the memory locations of two objects. The operators are 'is' and 'is not'.",
        "Python's identity operators include 'is' and 'is not'. They are used to check whether two variables refer to the same object in memory.",
        "The identity operators 'is' and 'is not' are used in Python to check if two variables point to the same object in memory."
    ],
    # Object-Oriented Programming (OOP) in Python
    ("what is oops", "explain oops in python", "object-oriented programming in python", "what is object-oriented programming"): [
        "Object-Oriented Programming (OOP) in Python is a programming paradigm that uses objects and classes to structure code. It allows for creating reusable code by modeling real-world entities as objects.",
        "OOP in Python focuses on using classes and objects to organize code. It supports principles like inheritance, polymorphism, encapsulation, and abstraction.",
        "Object-Oriented Programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. Python supports OOP through the use of classes."
    ],
    # class
    ("what is a class", "explain class in python", "what is a class in python", "how to define a class in python"): [
        "A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have.",
        "In Python, a class is a user-defined blueprint or prototype from which objects are created. Classes encapsulate data and the functions that operate on that data.",
        "A class is a construct in Python that defines the structure and behavior (methods) that its objects will have. It acts as a template for creating multiple instances."
    ],
    # object
    ("what is an object", "explain object in python", "what is an object in oops", "how to create an object in python"): [
        "An object in Python is an instance of a class. Objects are created using the class and can have attributes and behaviors defined by the class.",
        "In OOP, an object is a specific instance of a class, with its own attributes and methods. Objects are the building blocks of Python programs.",
        "An object is a tangible entity based on a class. It is created by calling the class and can have state and behavior as defined by the class."
    ],
    # Inheritance
    ("what is inheritance", "explain inheritance in python", "how does inheritance work in python", "what is class inheritance"): [
        "Inheritance in Python allows a class to inherit attributes and methods from another class. It promotes code reuse and establishes relationships between classes.",
        "In Python, inheritance is a mechanism where a new class (child class) inherits the properties and behaviors of an existing class (parent class). This allows for extending or modifying the parent class's functionality.",
        "Inheritance is a fundamental concept in OOP that enables one class to inherit characteristics (attributes and methods) from another, promoting code reuse and efficiency."
    ],
    # Polymorphism
    ("what is polymorphism", "explain polymorphism in python", "how does polymorphism work in python", "what is polymorphism in oops"): [
        "Polymorphism in Python refers to the ability of different classes to be treated as instances of the same class through inheritance. It allows for using a single interface to interact with different data types.",
        "In Python, polymorphism allows objects of different classes to respond to the same function call. It is achieved through method overriding and interfaces.",
        "Polymorphism is a concept where different classes can be accessed through the same interface. Each class can provide its own implementation of the interface, enabling code flexibility and reuse."
    ],
    # Encapsulation
    ("what is encapsulation", "explain encapsulation in python", "how does encapsulation work in python", "what is encapsulation in oops"): [
        "Encapsulation in Python is the concept of bundling data and methods that operate on that data within a single unit, such as a class. It helps in data hiding and abstraction.",
        "Encapsulation in OOP restricts direct access to some of an object's components, which can prevent the accidental modification of data. In Python, this is typically achieved using private or protected variables.",
        "Encapsulation is the process of wrapping code and data together into a single unit. In Python, encapsulation is used to protect the internal state of an object from being modified directly."
    ],
    # Abstraction
    ("what is abstraction", "explain abstraction in python", "how does abstraction work in python", "what is abstraction in oops"): [
        "Abstraction in Python is the concept of hiding the complex implementation details and showing only the essential features of an object. It helps in reducing complexity and improving code readability.",
        "In Python, abstraction is achieved through abstract classes and interfaces. It allows programmers to focus on what an object does rather than how it does it.",
        "Abstraction is an OOP principle that involves hiding the implementation details of an object and exposing only the necessary parts. It simplifies the interaction with complex systems."
    ],
    # __init__ method
    ("what is __init__", "explain __init__ in python", "what does __init__ do", "what is the __init__ method"): [
        "__init__ is a special method in Python, known as a constructor, that is automatically called when a new object of a class is created. It is used to initialize the object's attributes.",
        "In Python, __init__ is a constructor method that initializes an object's state. It runs as soon as an object of a class is instantiated and allows setting initial values for object attributes.",
        "__init__ is a method that gets called when a new object is created from a class. It’s used to set the initial state of the object by assigning values to its properties."
    ],

    # self keyword
    ("what is self", "explain self in python", "what does self mean", "why use self in python"): [
        "In Python, self is a reference to the current instance of the class. It is used to access variables that belong to the class and is the first parameter of methods in the class.",
        "The self parameter in Python is used in instance methods to access the attributes and other methods of the class. It allows each object to keep track of its own data.",
        "self refers to the instance calling the method. It is used to bind the instance with the method so that the method can access or modify the object’s attributes."
    ],

    # decorators
    ("what is a decorator", "explain decorators in python", "how to use decorators in python", "what do decorators do"): [
        "A decorator in Python is a function that modifies the behavior of another function or method. Decorators are often used to add functionality to existing functions in a clean and reusable way.",
        "Decorators in Python are a powerful tool that allows you to wrap a function or method to extend or alter its behavior without modifying its code. They are often used for logging, access control, and memoization.",
        "In Python, a decorator is a design pattern that allows you to add new functionality to an existing object without modifying its structure. Decorators are applied using the '@' symbol above a function definition."
    ]
}

# create a main function to take user's name
def toRunChatbot():
    userName = input("What is your good name...? ")

    # create a program to give answers of user's choice 
    def chatbot():
        print("Hello!",userName.upper(),"I'm your Python programming chatbot. Ask me about Python fundamentals.")
        print("Type 'exit' OR press 'enter' to end the chat.\n")

        while True:
            # to get user input
            user_input = input(f"{userName.upper()}: ").lower()
            
            # Check if the user wants to exit
            if not user_input or user_input == "exit":
                print("Chatbot: Goodbye! Happy coding!")
                break
            
            # Check if the user's input is in any of the keys in the dictionary
            questionFound = False
            for keyInTuple, answers in pythonDict.items():
                if user_input in keyInTuple:
                    print("Chatbot: ", random.choice(answers))
                    questionFound = True
                    break
            
            # If no matching question is found
            if not questionFound:
                print("Chatbot: Sorry, I don't understand that question. Can you try asking differently?")
    # if get username then invoke the function
    if userName:
        chatbot()
    else:
        print("Sorry I can't reply to any nameless")
# Run the chatbot
toRunChatbot()


