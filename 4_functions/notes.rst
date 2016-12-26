====
Functions
====

**Reading**

* Zelle, Chapter 6 - Functions
* https://www.tutorialspoint.com/python/python_functions.htm 
* Slides - http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter06.ppt 

**Summary**

* What are functions
* Definition
* Usage
* Parameters
* Return values
 

**What are functions?**

* A function is a sub-program inside a program. The sub-program has a name that can be referenced multiple times.
* Benefits:

 - Reduces code duplication - Allows code to be defined/maintained in one place, but called multiple times from different places
 - Can make programs more readable
 
* Common function types in python
 - main() function of a program
 - Built-in python functions - e.g. print()
 - Functions in standard libraries - e.g. math.sqrt()
 

**Function definition**

code that creates a function;

 def <name>(<formal_parameters>):
  <body>
  return <value>

* Parameters and return statement are optional
* Parameters are function inputs and can be any valid Python data type
 
**Function usage**

Functions are ‘called’ or ‘invoked’;

 <name>(<actual_parameters>)

* Actual params are matched up to formal params by position, unless you use keyword parameters
* When a function is called, the calling program suspends execution and hands control to the function
 

**Function parameters**

* Formal parameters are variables accessible only within the function (local scope) and distinct from variables with same name elsewhere in the program
* Number of actual parameters must match # of expected formal parameters. Extra params are ignored.
* Parameters are passed to a function one of two ways:
 - By-value - Simple data-type parameters (int, string, float, bool) are passed as values. Original variables outside the function are unchanged by any code within the function
 - By-reference - Changes made to mutable objects (dictionaries, lists, arrays) passed as parameters may be visible to caller outside the function
 
**Return values**

Functions can ‘return’ values:

 def <name>(<formal_parameters>):
  <body>
  return <value>

* Return causes Python to exit the function and return control to where function was invoked. Values in the return statement sent back to the caller.
* Python functions can return multiple values
* Functions w/o a return statement automatically return ‘None’
