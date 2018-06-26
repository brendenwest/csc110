====
Conditional Logic
====

**Reading**

* Zelle, Chapter 7 - Decision Structures
* Slides http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter07.ppt 
* https://www.tutorialspoint.com/python/python_decision_making.htm 
* https://www.tutorialspoint.com/python/python_exceptions.htm 

**Summary**

* If statements
* Boolean statements
* Two-way & multi-way if statements
* Nested decisions
* Exception handling

**Decision structures**
- allow a program to execute different sequences of instructions for different cases.

* basic if statements have this structure:
::

    if <condition>:
        <body>

**Conditional statements** - evaluate to **True** or **False**

    <expr> <relational_operator> <expr>

for example:
::
    name = "dave"
    len(name) < 3   # evaluates to False
    name == 'dave'  # evaluates to True

**Comparison Operators**

* <, <=, ==, >=, >, !=
* remember that python uses '==' for comparison 
* 'not' returns the opposite of a subsequent boolean expression. For example:
    - not 1 == 1 # returns False because 1 == 1 returns True
    - not 1 == 2 # returns True because 1 == 2 returns False

**Compound expressions** can be formed with **and**, **or**, **not**. For example:
::
    if age < 18 and gender == 'female': # both expressions must be true

    if age < 18 or gender == 'female': # either of the expressions must be true 

**Two-way** - mutually exclusive decisions
::
    if <condition>:
        <statements>
    else:
        <statements>

 
**Nesting** - conditional statements can be nested:
::
    if <condition1>:
        if <condition2>:
            <statements> # executed if condition1 & condition2 are true

**Multi-way** - Decision blocks can have any number of conditional statements:
::
    if <condition>:
        <statements>
    elif <condition>:
        <statements>
    else:
        <statements>

**Exception handling** - used to gracefully catch & handle possible program errors.
::
    try:
        <body>
    except <ErrorType>:
        <handler>

* Body can have multiple statements
* Can have multiple exception handlers for different errors
* Can assign error to an object for use in handler
