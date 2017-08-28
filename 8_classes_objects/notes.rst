====
Objects & Classes
====

**Reading**

* Zelle, Chapter 10 - Objects & Classes
* http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter10.ppt  
* https://www.tutorialspoint.com/python/python_classes_objects.htm 
 
**Summary**

* What are objects?
* What are classes?
* Python class definition
* Class methods
* Getter & Setter methods
* Class variables
* Class inheritance

**What are objects?**

* Key concept in object-oriented programming
* A data type that has attributes (properties and methods)
* Objects have;
  - Properties - set of related information
  - Methods - functions that perform object-specific operations
* Objects are instances of a ‘class’
* Each instance can have different valuies for properties (instance variables)
* Objects allow encapsulation of all information about an individual item into a single variable
* In Python, objects are defined by a 'class'

**What are classes?**

* A software 'class' models a real-world object
* Defines the attributes (including default values) object instances will have
* Can be defined in a python module with other classes, or in a standalone module
* Names usually begin with an upper-case letter
* Can have 'class variables' shared between instances of the class
* In Python, names for special class methods are delimited with __

  class Student:
  
    id = 0  # class variable
  
    # constructor method to create new class instance
    def __init__(self,name,major):
      self.name = name
      self.major = major
      Student.id += 1 # increment class variable
      self.id = Student.id
    
    # print student name 
    def displayName(self):
      print("Name:",self.name)


* Python invokes the class constructor to create a new object instance:

  student = Student('James','math')

**Constructor method**

Classes may have a 'constructor' method to set initial values for class variables. 

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
