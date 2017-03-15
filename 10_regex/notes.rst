**Reading**

- https://www.tutorialspoint.com/python3/python_reg_expressions.htm
- https://docs.python.org/3/library/re.html 
- https://regex101.com/ (online regex tester)

**Summary**

- Intro to regular expressions
- Character patterns
- Quantifiers
- Modifiers


A regular expression uses specialized language-independent syntax for describing character patterns. Regular expressions are very useful for finding/replacing text, but can easily become complex and difficult to read.

In Python, regular expressions depend on the 're' module and have this basic syntax:

    import re
    re.<command>(r'pattern', string, flags)
    
where:
    - pattern is the regular expression to be matched
    - string is the text to be searched
    - flags are expression modifiers (separated by |)
    
**note** the pattern is wrapped as a 'raw' string because some characters have special meaning as a regular expression.

Patterns are combinations of: 

Literal characters - Any letters, numbers, symbols or control characters (e.g. tab, line break, etc.). Characters with special meaning in regular expressions, such as ( and \ must be ‘escaped’ with a \ symbol. 


**Character classes** - define specific characters to match. E.g. 

[abc] - match any of the characters within brackets

[a-m] - match any lowercase character between a & m

[^abc] - negated set. matches any characters NOT among those in brackets

[0-9] - match any number between 0 & 9

(a | b) - match either pattern a or pattern b, separated by | symbol 

 
**Metacharacters** - match certain kinds of characters

\d - match any digit

\D - match any character NOT a digit

\s - match a whitespace character

\w - matches any word character

\W - matches any non-word character

.  - matches any one character

\b - matches the boundary between a word & a non-word

^  - matches the start of the string

$  - matches the end of the string


**Quantifiers** - define how many times to match the preceding pattern

pattern* - match 0 or more repetitions of 'pattern'

pattern+ - match one or more instance of 'pattern'

pattern? - match any string with zero or one occurrences of 'pattern'

pattern$ - match any string with 'pattern' at the end

^pattern - match any string with 'pattern' at the beginning

pattern{n} - match strings that repeat 'pattern' n times

pattern{n, m} - match strings that repeat 'pattern' n or m times


**Flags** - modify how the pattern will be executed

    re.a - Makes escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
    re.i - perform case-insensitive matching
    re.m - perform multi-line match

Regex patterns can be composed into more complex patterns. For example the below pattern uses an optional group to match 5-digit or 9-digit US zip codes:

    r'\d{5}(?:-\d{4})?'

**Python Operations**

Python has several basic regex methods you can use for text searching & replacing:

- match - checks for a match only at the beginning of the string
- search - checks for a match anywhere in the string
- findall - returns any matches as a list of strings

Both match & search return a match object for any sub-strings that match the regex pattern, and none on failure. The match object contains information about where the match was found in the input string, as well as sub-groups found.

We use group(num) or groups() function of match object to get the matched expression.

    import re
    matchObj = re.search(r'\d{5}?', 'my zip code is 98104', flags=0)
    if matches: 
      print ("matchObj.group() : ", matchObj.group()) 
    else: 
      print ("Nothing found!!")

findall() will return a collection of matched strings. If your regex pattern uses parentheses for grouping, matched groups will be returned as tuples.

    import re
    matches = re.findall(r'\d{5}(?:-\d{4})?', '98104, 98124-4033')
    print(matches)

sub - replaces the matched string with a different string

    # replace cat w/ dog
    print(re.sub(r'cat\b', 'dog', 'my cat is in a category by herself', flags=re.I))
    >>>'my dog is in a category by herself'