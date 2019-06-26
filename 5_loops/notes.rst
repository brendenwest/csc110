====
Loops
====

**Reading**

* Think Python, Chapter 7 - http://greenteapress.com/thinkpython2/html/thinkpython2008.html
* https://www.tutorialspoint.com/python/python_loops.htm 

**Practice**

* https://repl.it/community/classrooms/17929 (sections 4 & 6) 

**Summary**

* Basic loops
* Counted loops
* Indefinite loops
* Sentinel loops
* Nested loops
 
**Basic loop**
::
  for <var> in <sequence>:
    <body>

* Statements in body executed once for each item in <sequence>
* <sequence> can be any valid Python sequence (range, list, string, etc.)
* With each loop iteration, <var> is assigned the value of the next item in the sequence
* Can use an ‘accumulator’ variable initialized outside the loop
 
**Counted loop**
::
  for <var> in range(n):
    <body>

  for num in range(5):
    print(num,' - ', num**2)
    
* <var> will have an integer value

::
  names = ['dave','james','susan']
  for name in names:
    print(name)

**Indefinite (while) loop**
::
  while <condition>:
    <body>
    
  count = 1
  while count < 5:
    print(count,' - ',count * 2)
    count += 1

* <body> statements executed as long as <condition> is True
* <condition> can be one or more logical expressions
* No guarantee how many times loop will execute
* Can result in infinite loop if condition is never met
 
**Sentinel loop**

Loop continues until reaching a special value (sentinel)
::
  stop = 5
  for i in range(10):
    print(i)
    if i == stop:
      break
    
**Nested loops**
::
  for <var> in <sequence>:
    for <var2> in <sequence2>:
      <body>
 

**Break statement**

terminates loop and transfers to command after the loop
::
  for <var> in <sequence>:
    if <expr>:
      break
    else:
     <body>
     
  names = ['dave','james','susan']
  for name in names:
    print(name)
    if name == 'james':
      print('- break')
      break

