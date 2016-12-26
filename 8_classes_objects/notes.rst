====
Objects & Classes
====

**Reading**

* Zelle, Chapter 10 - Objects & Classes
* http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter10.ppt (Links to an external site.) 
* https://www.tutorialspoint.com/python/python_classes_objects.htm (Links to an external site.) (Links to an external site.)
 
**Summary**

* What are classes?
* What are objects?
* Python class definition
* Class methods
* Getter & Setter methods
* Class variables
* Class inheritance

**What are classes?**

* A software 'class' models a real-world object
* Defines the attributes (including default values) object instances will have
* Can be defined in a python module with other classes, or in a standalone module
* Names usually begin with an upper-case letter

**What are objects?**

* Key concept in object-oriented programming
* A data type that has attributes (properties and methods)
* Objects have;
  - Properties - set of related information
  - Methods - functions that perform object-specific operations
* Objects are instances of a ‘class’
* Each instance can have different valuies for properties (instance variables)
* Objects allow encapsulation of all information about an individual item into a single variable
* Python invokes the class constructor to create a new object instance:

  student = Student('James','math')


**Python class definition**

Python classes are defined with a 'class' statement. Class names usually begin with an upper case character.

Classes may have a 'constructor' method to set initial values for class variables. 

  class Person:

  id = 0  # class variable

  # constructor method to create new class instance
  def __init__(self,name,role):
    self.name = name
    self.role = role
    
    Person.id += 1 # increment class variable
    self.id = personId

  # print person name 
  def displayName(self):
    print("Name:",self.name)

**Constructor method**

* Special class method to initialize an object instance with default values,
* Python constructor methods are called __init__ 
* In Python, the first parameter - ‘self’ - refers to the object being created
* Defines initial properties of the object instance being created

**Class methods**

Methods belonging to a class.

**Class variables**

Variables shared between instances of the class

**Getter & Setter methods**

* Methods that mediate access to instance variables.
* Can be used to ensure changes to object properties are logically correct,
* Not required in Python, but is good practice to use them

  def getName(self):
    return self.name
  
  def setName(self, newName):
    self.name = newName

**Class inheritance**
