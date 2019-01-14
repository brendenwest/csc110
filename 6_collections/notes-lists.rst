====
Lists & Tuples
====

**Reading**

* Think Python, Chapter 10 - http://greenteapress.com/thinkpython2/html/thinkpython2011.html
* Think Python, Chapter 12 -  http://greenteapress.com/thinkpython2/html/thinkpython2013.html
* https://www.tutorialspoint.com/python/python_lists.htm 
* https://www.tutorialspoint.com/python/python_tuples.htm 

**Practice**

* https://repl.it/community/classrooms/17929  (section 7)

**Summary**

* List basics
* List methods
* Tuples
* Sorting

**Python List Basics**

* Python lists are sequences
* Python lists are similar to ‘Arrays’ in other languages
* Lists are defined with data inside brackets:
::
    >>> mylist = [1,2,3,4]
    >>> emptylist = []

* A Python list can contain different data types
::
    >>> mylist = [‘dog’,2,True]

* Indexing - List items can be accessed by index. Indices start at zero
::
    >>> mylist[0]
    ‘dog’
    >>> mylist[0] = ‘cat’
    >>> mylist[0]
    'cat'

* Slicing - List items can be accessed by slicing
::
    >>> mylist[1:2]
    2, True

* Deletion - List items can be removed with the built-in Python del method:
::
    >>> mylist = [1,2,3,4,5]
    >>> del list1[1]
    >>> mylist
    [1,3,4,5]
    >>> del mylist[1:2]
    >>> mylist
    [1,5]

* Deletion - List items can be removed with the built-in Python del method: 
::
    >>> mylist = [1,2,3,4,5]
    >>> del list1[1]
    >>> list1
    [1,3,4,5]
    >>> del list1[1:2]
    >>> list1
    [1,5]

* Contatenation - Lists can be added
::
    >>> list1 = [‘a’,’b’,’c’]
    >>> list2 = [‘x’,’y’,’z’]
    >>> list3 = list1 + list2
    [‘a’,’b’,’c’,‘x’,’y’,’z’]

* Length - lists have length
::
    >>> list1 = [‘a’,’b’,’c’]
    >>> len(list1)
    3
 
* Iteration - programs can operate on each item in a list, one at a time:
::
    >>> for letter in list1:
    >>>   print(letter) # prints each item in 'list1'
    
    >>> for i, item in enumerate(list):
    >>>   print(i, item)

* Membership check - test if a list contains a particular item
::
    >>> list1 = [‘a’,’b’,’c’]
    >>> ‘a’ in list1
    True

    >>> 'x' in list1
    False

* Other built-in Python methods
    - max(<list>)
    - min(<list>)
    - cmp(<list1>, <list2>)
    - list<tuple>) - converts a tuple to a list

**List Methods**

Python has a number of methods specific to lists, such as:

* <list>.append() - add element to END of list
* <list>.sort(<function>) - sort the list
* <list>.reverse() - reverse the list
* <list>.index(x) - return the index of the first occurrence of x
* <list>.insert(i, x) - insert x into the list at index i
* <list.count(x) - returns the number of occurrences of x in the list
* <list>.remove(x) - delete the first occurrence of x in the list
* <list>.pop(i) - deletes the ith element from the list and returns its value

**Tuples** 

* read-only sequences
* defined with parens instead of brackets
* similar behavior as lists
::
    >>> mytuple = ('a,'b','c)
    >>> len(mytuple)
    3
    >>> mytuple[1]
    'b'


**Sorting**

Lists are sorted by ASCII value by default:
::
    >>> mylist = ['a', 'B', 'b', 'c']
    >>> mylist.sort()
    >>> mylist
    ['B', 'a', 'b', 'c']

You can override the default with a custom sort function:

    <list>.sort(key=<function>, reverse=True)
::
    def byAlpha(ch):
     return ch.lower()

    >>> mylist.sort(key=byAlpha)
    >>> mylist
    ['a', 'B', 'b', 'c']
