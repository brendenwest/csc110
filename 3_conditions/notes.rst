====
Conditional Logic
====

**Reading**

* http://greenteapress.com/thinkpython2/html/thinkpython2006.html 
* https://www.tutorialspoint.com/python/python_decision_making.htm 
* https://www.tutorialspoint.com/python/python_exceptions.htm 

**Practice**

* https://repl.it/community/classrooms/17929 (section 3)

**Summary**

* Boolean expressions
* If statements
* Two-way & multi-way if statements
* Nested decisions
* Exception handling

**Boolean Expressions**

Conditional statements allow a program to execute different instructions for different conditions. Conditions use boolean expressions that evaluate to True or False. For example:
::
    1 < 3 # evaluates to True
    1 > 3 # evaluates to False
    'Dave' == 'dave' # False because upper & lower-case strings are different

Conditional expressions can use these **comparison operators**:

* <, <=, ==, >=, >, !=
* remember to use '==' for comparison
* The ! operator negates the expression. For example:
::
    'Dave' != 'dave' # True

**Compound expressions** can be formed with and, or, not. For example:
::
    age < 18 and gender == 'female' # True if both expressions are true
    age < 18 or gender == 'female' # True if either of the expressions is true 

* not - returns the opposite of a subsequent boolean expression. For example:
::
    not 1 == 1 # returns False because 1 == 1 returns True
    not 1 == 2 # returns True because 1 == 2 returns False


**Conditional statements**
Allow a program to execute different sequences of instructions for different cases. 

* Basic conditional statements have this structure:
::

    if <condition>:
        <body>

    if age < 18:
        print("sorry, you can't vote")


**Two-way** - handle two mutually exclusive conditions:
::
    if <condition>:
        <statements>
    else:
        <statements>

**Multi-way** - Decision structures can have any number of conditions:
::
    if <condition>:
        <statements>
    elif <condition>:
        <statements>
    else:
        <statements>

 
**Nesting** - conditional statements can be nested:
::
    if <condition1>:
        if <condition2>:
            <statements> # executed if condition1 & condition2 are true

