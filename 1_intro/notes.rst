=====
Week 1 - Intro to programming
=====

**Reading**

* Zelle, Chapter 1 - Computers & Programming
* Zelle, Chapter 2 - Writing Simple Programs
* https://www.tutorialspoint.com/python/python_basic_syntax.htm  

**Slides**

* http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter01.pptx 
* http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter02.pptx 

**Summary**

* Class overview
* What is computer science?
* Computer programming overview
* Programming languages overview
* Running Python 
 
**What is computer science?**

* Design, Analysis, Experimentation
* **Design** is the process of creating an algorithm - a step-by-step process for solving a problem with computation
* **Analysis** is the process of examining algorithms & problems mathematically
* **Experimentation** is the process of testing a system for possible solutions or verifying that a solution works
 
**What are programs?**

* Programs (software) are step-by-step instructions telling a computer what to do
* Programs are ‘executed’ by the computer
* Programming is the art of writing programs, and a fundamental part of computer science
* Also a form of expression. Programming can be fun.
 
**Computer hardware terms**

* CPU - central processing unit carries out all basic data operations
* GPU - graphics processing unit. Similar to CPU, but optimized for operations typical for graphics
* Memory - stores programs and data
* Main memory (RAM) is fast, but volatile
* Secondary memory - persistent but slower than RAM
* Input - How information is passed to the computer. E.g. keyboard, mouse, etc
* Output - How information is presented to the user - e.g. monitor, printer

**Programming languages**

* Unambiguous way of providing instructions to a computer
* High level -v- low level
  - High-level languages are designed to be understood by humans. E.g. Python, Java, C++
  - Low-level languages optimized for machines - Machine code, Assembly
* Compilers convert code from a high-level language to machine code (binary). Compiled languages include Java, C++, C#
* Interpreters allow a computer to execute high-level code without advance compilation. Interpret languages include Python, JavaScript
* Compiled programs generally runs faster than interpreted code
* Interpreted code can be developed and run interactively

**Why Python**

* human readable,
* easy to set up and run interactively,
* class-based & object oriented
* Open-source w/ large ecosystem of specialized libraries
 
**Running Python**

* local -v- cloud : Python can be installed and run on a local PC, or via a cloud-hosted service such as Cloud9 or PythonAnywhere
* Idle - integrated command-line and file-editing interface installed with Python
* Python shell - allows running python commands one line at a time:
::

    $ python
    >>> print("testing")
    testing
    >>> age = 32
    >>> age
    32

**Python programs**

Python programs are composed of one or more commands contained in a plain text file saved with a .py extension.

We'll cover more advanced commands throughout the course, but some basic commands you'll use:

* print - prints text to the screen or log file. Can combine multiple values into a single text message:
::

    print("Welcome")
    print("My name is:", name) 

Note - by default, each *print* command prints a new line of text. You can override this behavior by setting a custom *end* character:
::

    print("My name is:", name, end=" ")
    
* assignment - assign value to a variable for later use:
::

    age = 32
    name = "Dave"
    isActive = True

* comments are not executed by the code interpreter and can take several forms:
::

    # this is a single-line comment
    
    """
    This is a multi-line comment
    that spans two lines
    """

* Basic data types
Python supports several primitive data types for storing values:

    - int - whole integer numbers
    - float - floating point numbers w/ decimals
    - bool - True or False values
    - character - alpha-numeric characters

* Python scripts or modules are saved as text files with .py extension

* Python uses indents to define program structure. Number of tabs or spaces at the start of a command line are very important.

**Programming steps**

* Analyze the problem
* Specify what program will do (not how it will be done)
* Design program structure
    - Pseudocode - step-by-step description of program operations using plain english
    - Allows focus on program logic (algorithm) instead of language syntax
* Implement the design (actual code)
* Test & debug

**Meta-language** - method for showing generic syntax of a statement. E.g.:
::

    print(<expr>, <expr>)
    <variable> = <expr>

**Program elements**

* Names - identifiers for variables, functions, modules, etc.
    - must begin with letter or _
    - Cannot contain spaces or control characters
    - Case sensitive
    - Cannot use reserved words - words that have meaning in Python
* Literals - represent a specific value (e.g. number or string)
* Expressions
    - Fragments of code that produce new values
    - Can be combined with operators
    - Can be string concatenation (combining strings)
 