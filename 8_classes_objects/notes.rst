====
Objects & Classes
====

**Reading**

* Think Python, Chapter 15 - http://greenteapress.com/thinkpython2/html/thinkpython2016.html 
* Think Python, Chapter 17 - http://greenteapress.com/thinkpython2/html/thinkpython2018.html  
* Think Python, Chapter 18 - http://greenteapress.com/thinkpython2/html/thinkpython2019.html 
* https://www.tutorialspoint.com/python/python_classes_objects.htm 
 
**Summary**

* What are objects & classes?
* Python class definition
* Class methods
* Getter & Setter methods
* Class variables
* Class inheritance

**What are objects?**

* Key concept in object-oriented programming
* A data type that has attributes (properties and methods)
* Objects are instances of a ‘class’ with;
  - Properties - set of related information
  - Methods - functions that perform object-specific operations
* Each instance can have different valuies for properties (instance variables)
* Objects allow encapsulation of all information about an individual item into a single variable

**What are classes?**

* Abstract model of a real-world object
* Defines the attributes object instances will have
* Can be defined in a python module with other classes, or in a standalone module
* Names usually begin with an upper-case letter
* May define 'class variables' shared between instances of the class
* In Python, names for special class methods are delimited with __
::
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

**Note**
- Python class methods automatically receive 'self' as a parameter
- 'self' allows methods to access attributes of the current object instance

**Constructor method**

Classes may have a 'constructor' method to to initialize an object instance with default values. 

* Python constructor methods are called __init__ 
* In Python, the first parameter - ‘self’ - refers to the object being created
* Python invokes the class constructor to create a new object instance:
::
  student1 = Student('James','math')
  print(student1.major) # prints 'math'
  
  student2 = Student('Sara','cs')
  print(student2.major) # prints 'cs' 


**Class methods**

  Methods belonging to a class.

**Class variables**

  Variables shared between instances of the class

**Getter & Setter methods**

* Methods that mediate access to instance variables.
* Allow external programs to access methods as properties,
* Can be used to ensure changes to object properties are logically correct,
* Not required in Python, but useful for computed values:
::
  class Student:
    def __init__(self, name):
      # private instance variable prefaced with _
      self._name = name

  @property
  def name(self):
    # ensure name is returned in capitalized form
    return self._name.capitalize() 
  
  @name.setter
  def name(self, value):
    # ensure name is not empty
    if len(value) > 0:
      self._name = value

**Class description**

Python recognizes several default methods for returning information about a class. The default method __repr__ is invoked by the print() command must return a string value:
::
  def __repr__(self):
    return "Student: {0} major: {1}".format(self._name, self._major)
  
  >>> student1 = Student('Sanjay','CS')
  >>> print(student1)
  'Student: Sanjay major: CS'
 

**Importing Classes**

Python programs often import classes defined in other Python modules.

A program can import all module classes like so, with module name prefixed to any class methods or attributes: 
::
  import math
  print(math.pi)

Alternatively, a program can import specific module classes. In this case, module prefix is not required on usage:  
::
  from math import pi, fabs
  print(pi)
  print(fabs(-1))
  
**Inheritance**

* Avoids duplication of code
* A class (subclass) can inherit attributes from another class (superclass)
* Subclasses can share attributes inherited from the superclass
* Subclasses can have unique attributes not shared with other subclasses
* Subclasses can ‘override’ attributes or methods inherited from the superclass
::
  class Person:
  
      def __init__(self, first, last):
          self.firstname = first
          self.lastname = last
  
      def __repr__(self):
          return "{0} {1}".format(self.firstname, self.lastname)
  
  class Employee(Person):
  
      def __init__(self, first, last, staffId):
          super().__init__(first, last)
          self.staffId = staffId
  
      def __repr__(self):
          return "{0}, staffId={1}".format(super().__repr__(), self.staffId)
  
  class Student(Person):
  
      def __init__(self, first, last, studentId):
          super().__init__(first, last)
          self.studentId = studentId
  
      def __repr__(self):
          return "{0}, studentId={1}".format(super().__repr__(), self.studentId)


person1 = Person("Marge", "Simpson") 
employee1 = Employee("Homer", "Simpson", 1007)
student1 = Student("Lisa", "Simpson", 123)

print(person1) # prints "Marge Simpson"
print(employee1) # prints "Homer Simpson, staffId=1007"
print(student1) # prints "Lisa Simpson, studentId=123"