====
Dictionaries & Sets
====

**Reading**

* Think Python, Chapter 11 - http://greenteapress.com/thinkpython2/html/thinkpython2012.html 
* http://greenteapress.com/thinkpython2/html/thinkpython2014.html 
* https://www.tutorialspoint.com/python/python_dictionary.htm 
* https://www.tutorialspoint.com/python/python_tuples.htm 
* https://pythonspot.com/en/python-set/

**Practice**

* https://repl.it/community/classrooms/17929  (A.1 - A.8)

**Summary**

* Dictionaries
* Sets
 

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