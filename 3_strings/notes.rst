========================
Week 3 - Strings & Files
========================

**Reading**

* Zelle, Chapter 5 - Sequences, Strings, Lists & Files
* https://www.tutorialspoint.com/python/python_strings.htm 

**Slides**

* Slides - http://mcsp.wartburg.edu/zelle/python/ppics3/slides/Chapter05.pptx

**Summary**

* String variables
* Strings as sequences
* String operations
* Character encoding
* String methods
* String formatting
* File processing

**String variables**

* Text is represented by the String data type
* Strings are delimited by quotes or apostrophes - e.g. ‘This is text’
* Quotes in text are escaped with \ - e.g. ‘We\re excited’
* Strings are case sensitive
* Python input() command returns a string by default::

    phrase = input("enter a phrase: ")

**Strings as sequences**

* Strings are sequences of characters. Individual characters can be accessed by zero-based index #:
::

    >>> name = 'james'
    >>> name[0]
    'j'

* The last character of a string is at index of length-1
* len(<string>) returns the number of characters in the string
::
    >>> len(name)
    5

 
**Substrings**
 
* Substrings can be accessed by ‘slicing’ - <string>[<start>:<end>]
::

    >>>name[1:3]
    'am'

* the substring contains characters up to, but NOT including 'end' number
* If either expression is omitted, the start or end of the string is used
::

    >>>name[:3]
    'jam'
    >>>name[2:]
    'mes'
 

**Concatenation** - Strings can be combined with +
::

    >>>'spam' + 'eggs'
    'spameggs'

**Repetition** - Strings can be repeated with *
::

    >>>3*'spam'
    'spamspamspam'

**String methods** - Python provides many string-specific methods:

* s.upper()
::

    >>> name = 'Bart'
    >>> name.upper()
    BART

* s.lower()
::

    >>> name.lower()
    bart

* s.replace(<sub1>,<sub2>) - replace occurrences of <sub1> with <sub2>
::

    >>> bart.replace(‘t,’b’)
    Barb

* s.count(<sub>) - count occurrences of <sub> in string s
* s.find(<sub>) - return the first position of <sub> in string s
* s.join([<sub>, <sub>]) - join a list of substrings, using s as separator
* s.split(<sub>) - split s into a list of substrings based on <sub>
::

    sentence = 'the quick brown fox'
    sentence.split() # splits on spaces by default
    print(words) # prints [‘the’, ‘quick’, ‘brown’, ‘fox’]

    for w in words:
      print(w) # prints each word in list

**Iteration** - You can iterate through the characters in a string with a loop: 
::

    for ch in 'class':
       print(ch, end=" ") # prints each character followed by a space


**Character encoding**

* ASCII - most common latin characters & symbols
* UTF-8 - support for nearly all characters in all languages
* Control characters - special characters that control computer behavior (e.g. tabs, spaces, carriage returns, etc.)
* chr(<int>) - returns character associated with the number
::

    >>> chr(65)
    'A'

* ord(<str>) - returns number associated with the character
::

    >>> ord('A')
    65

**String Formatting**

Strings can be formatted with a ‘template’ string that has placeholders into which values are inserted:

    <template-string>.format(<values>)
::

    "Hi. My name is {0} and I like {1}".format('Dave', 'baseball')

* Placeholders have an index number that tells which value to insert,
* Placeholders can include a format specifier for how the value should be displayed.
* Format specifier has the form:

    <width>.<precision><type>

    - Width tells how may spaces to occupy and precision indicates # of decimal places. For example, the below statement formats ‘total’ value to 2 decimal places:
::

    print("Total price is {0:0.2f}".format(total))


**File processing**
 
* Files are large strings
* Lines in files are separated by newline ( \n ) characters
* Files must be opened before programs can read from or write to them:

    <filevar> = open(<filename>, <mode>)
::

    myFile = open('myfile.txt', 'r')

* Reading: after opening a file, you can read file contents with several different commands:
    - file.read() - reads entire file into a string
    - file.readlines() - returns the entire file into a list of lines
    - file.readline() - reads the next line as a string. Moves ‘pointer’ so subsequent commands operate only on remaining lines.
    
Programs can iterate through all lines in a file:
::

    inFile = open(‘myfile.txt’, ‘r’)
    for line in inFile.readlines():
        print(line)
    inFile.close()


After completing read/write operations, the file must be closed:

* Writing
    - Opening a file for writing prepares it to receive data. It creates a file if one doesn’t exist, and overwrites any existing file contents:
::

    outfile = open('myfile.txt', 'w')
    print(<expression>, file=outfile)
