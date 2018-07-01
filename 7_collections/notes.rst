====
Data Collections
====

**Reading**

* Zelle, Chapter 11 - Data Collections
* https://www.tutorialspoint.com/python/python_lists.htm 
* https://www.tutorialspoint.com/python/python_dictionary.htm 
* https://www.tutorialspoint.com/python/python_tuples.htm 
* https://pythonspot.com/en/python-set/

** Slides** 
* http://mcsp.wartburg.edu/zelle/python/ppics2/slides/Chapter11.ppt 

**Summary**

* List basics
* List methods
* Tuples
* Dictionaries
* Sorting
* Sets
 
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

**Dictionaries**

* Similar to hashes or associative arrays in other languages
* Data are stored as key-value pairs - values are ‘mapped’ to unique keys:
::
    <dictionary> = { <key> : <value>, <key> : <value> }

    >>> student = { ‘name’ : ‘sara’, ‘age’: 23 }
    >>> student[‘name’]
    ‘sara’

* Keys must be unique strings
* Values can be any valid Python data type
* Key-value pairs not stored in any order
* New keys can be added by assignment
::
    >>> student[‘major’] = ‘CS’
    >>> student
    { ‘name’ : ‘sara’, ‘age’: 23, ‘major’: ‘CS }

**Dictionary methods**

* <key> in <dict> - returns True if <dict> contains <key>
* <dict>.keys() - return a sequence of keys in <dict>
* <dict>.values() - return a sequence of values in <dict>
* <dict>.items() - return a sequence of tuples representing key-value pairs in in <dict>
* <dict>.get(<key>, <default>) - return the value for a specified key or a default value
* del <dict>[<key>] - delete the specified key
* for <var> in <dict> - iterate over the keys in <dict>
* <dict>.clear() - delete all dictionary items

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


**Sets**

A Python set is a collection of 'unique' items, similar to a list but with no duplicates. Multiple items added to a set are removed.
::
    >>> names = set(['ann','bob','chris','ann'])
    >>> names
    {'bob', 'chris', 'ann'}

Set elements can be added or removed:
::
    >>> names.add('james')
    >>> names
    {'james', 'bob', 'chris', 'ann'}
    >>> names.remove('bob')
    >>> names
    {'james', 'chris', 'ann'}
  
Python sets are modeled after sets in mathematics and support efficient comparison operations:
- test if a set is a subset of another set
- test if a set is a super-set of another set
- difference between two sets
- intersection of two sets