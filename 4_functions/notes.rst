====
Functions
====

**Reading**
* Think Python, Chapter 3 - http://greenteapress.com/thinkpython2/html/thinkpython2004.html 
* Think Python, Chapter 6 - http://greenteapress.com/thinkpython2/html/thinkpython2007.html
* https://www.tutorialspoint.com/python/python_functions.htm 


**Summary**

* What are functions
* Function definition
* Usage
* Parameters
* Return values
 

**What are functions?**

* A function is a sub-program inside a program. The sub-program has a name that can be referenced multiple times.
* Benefits:
 - Reduces code duplication - Allows code to be defined/maintained in one place, but called multiple times from different places
 - Can make programs more readable
 
* Common function types in python
 - **main()** function of a program
 - Built-in python functions - e.g. print()
 - Functions in standard libraries - e.g. math.sqrt()
 

**Function definition**

Python functions have this general form:;
::

 def <name>(<formal_parameters>):
  <body>
  return <value>

* Parameters and return statement are optional
* Parameters can be any valid Python data type and are treated as local variables within the function
::

 def printWelcome(name):
    # function doesn't return a value
    print("Welcome",name)
    
 def multiple(x,y):
   # returns a value
   return x * y
  
**Function usage**

Functions are ‘called’ or ‘invoked’ like this - <name>(<actual_parameters>):
::

 printWelcome("dave") # has no return value
 printWelcome("jim")

 val = multiply(3,4) # return value assigned to a variable
 
* Actual params are matched up to formal params by position, unless you use keyword parameters
* When a function is called, the calling program suspends execution and hands control to the function
 

**Function parameters**

* Formal parameters are variables accessible only within the function (local scope) and distinct from variables with same name elsewhere in the program
* Number of actual parameters must match # of expected formal parameters. Extra params are ignored.
* Parameters are passed to a function one of two ways:
 - **By-value** - Simple data-type parameters (int, string, float, bool) are passed as values. Original variables outside the function are unchanged by any code within the function
 - **By-reference** - Changes made to mutable objects (dictionaries, lists, arrays) passed as parameters may be visible to caller outside the function
::

 def capitalizeNames(names):
   # capitalize each name in list
   for i in range(len(names)):
     names[i] = names[i].capitalize()
     
 names = ["jim","sarah"]
 capitalizeNames(names)
 print(names) # prints ["Jim","Sarah"]

 
**Return values**

Functions can ‘return’ values:
::

 def <name>(<formal_parameters>):
  <body>
  return <value>

* Return causes Python to exit the function and return control to where function was invoked. Values in the return statement sent back to the caller.
* Code inside the function but after the return statement is ignored
* Python functions can return multiple values
* Functions w/o a return statement automatically return ‘None’
