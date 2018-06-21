================
Week 2 - Numbers
================

**Reading**

* Zelle, Chapter 3 - Computing with Numbers
* https://www.tutorialspoint.com//python/python_numbers.htm
* http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter03.pptx

**Summary**

* Numeric data types
* Numeric operators
* Python Math library
* How computers store numbers
* Type conversion & rounding
* Ranges & loops

**Notes**

* Python has two distinct numeric data types:
 - int - whole numbers. Can be positive or negative. Best for representing values that can’t be fractional (e.g. counts)
 - float - numbers with decimal fractions (even 0.0)
* int & float stored differently in computers
* Data type determines valid values and operations that can be performed on an object

type(<value>) shows the datatype of a value:
::

  >>> type(3)
  <class 'int'>
::

  >>> type(3.0)
  <class 'float'>

* Most mathematical calculations are very efficient with integers
* Limits of float accuracy - float is only an approximation of real number value, so not ideal for exact calculations
* Operations on ints produce ints & operations on floats produce floats, except division ( / ):
::

  >>> 3.0+4.0
  7.0
  >>> 3+4
  7
  >>> 3.0*4.0
  12.0
  >>> 3*4
  12
  >>> 10.0/3.0
  3.3333333333333335
  >>> 10/3
  3.3333333333333335

Python has a special operator for integer division:
::

  >>> 10 // 3
  3
  >>> 10.0 // 3.0
  3.0

% operator - returns the remainder from a division operation
::

  10 % 2 = 0
  10 % 3 = 1 # 10 / 3 = 3 remainder 1

* Limitations - how computers store numbers
 - Numbers are stored in bits
 - 32-bit CPU can store ints between -231 to 230 ( to account for 0 )
 - Floating-point numbers are not exact

* Type conversion & rounding
 - In mixed-type expressions, python converts ints to floats, to avoid losing information
 - You can also use explicit type conversion:
::

  >>> float(22//5)
  4.0
  >>> int(4.5)
  4
  >>> int(3.9)
  3
  >>> round(3.9)
  4

Some common Python numeric functions:

- abs(x) - returns absolute value of x
- round(x, n) - returns x rounded to n digits 
- max(x1, x2, ...) - returns the largest of a sequence of numbers
- min(x1, x2, ...) - returns the smallest of a sequence of numbers

**Python Math library** - a special Python module with common math functions

- ceil(x) - returns the smallest integer larger than x
- exp(x) - returns e to the power of x
- floor(x) - returns the largest integer smaller than x
- pi - returns value of pi
- pow(x, y) - x to the power of y
- sqrt(x) - square root of x

Python programs have to import the math library before using these methods:
::

 import math
 # calculate square root
 x = 4
 print(“square root of 4 = “, math.sqrt(x))

**Number Sequences**

In Python, a sequence of numbers can be represented explicitly:
::

 nums = [0, 1, 2, 3, 4, 5]

or logically as a 'range' of numbers in this form - range(<start>, <end>). For example:
::

 nums = range(0,6)  # 0 is start number, 6 is end number
 nums = range(6)

- the 'end' number isn't included in the sequence.
- start number can be omitted if starting from zero

Ranges can increment by some number other than 1 - e.g.
::

  >>> range(0,10,2)
  [0, 2, 4, 6, 8]
  >>> range(6,1,-1)
  [6, 5, 4, 3, 2]

**Loops**

Programs can use loops to perform the same operation on a sequence of numbers:
::

 for <variable> in <sequence>:
   <body>

For example:
::

 import math
 for num in range(10)
     print("Square root of ", num, "=", math.sqrt(num))

- each value in the sequence is assigned to 'num' one at a time,
- <body> can be any number of python commands, executed once for each value in the sequence 

Loops sometimes involve an 'accumulator' variable, defined before starting the loop:
::

 # calculate 6!
 fact = 1
 for factor in [2, 3, 4, 5, 6]:
  fact = fact * factor

 # calculate n!
 fact = 1
 for factor in range(2,n+1):
  fact = fact * factor
::

 # calculate average
 grades = eval(input("Enter grades: "))  # user can enter comma-separated list of grades
 total = 0 
 for grade in grades:
   total = total + grade
 average = total/len(grades) # use 'len()' method to get number of grade entries
 print("Average grade is",round(average,1))

* accumulator value is updated with each pass through the loop
* Loop values can be defined by a list - e.g.  [2, 3, 4, 5, 6]
* Loop values can be defined by a range - e.g. range(2,7)
