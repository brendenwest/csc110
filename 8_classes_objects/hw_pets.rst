Cats and dogs have much in common - they're both furry mammals that like people and make great pets.

Sadly, they have shorter lifespans than people and we sometimes refer to 'dog years' for this accelerated aging process. Cats and dogs age differently as well, with cats living significantly longer. The general aging rule is:

**Dogs**

    age 1 = 15 dog years
    age 2 = +9 dog years
    age 3+ = +5 dog years for each year over 2

The ages accumulate, so for example 2 human years would be 24 dog years.

**Cats**

    age 1 = 15 cat years
    age 2 = +9 cat years
    age 3+ = +4 cat years for each year over 2

For this assignment, create python module called pets.py, with a **Pet** superclass having common attributes (name, age, breed), where 'age' is in human years. Then create **Cat** and **Dog** subclasses that inherit from **Pet** and implement methods to calculate appropriate 'animal' years and print pet information.

Other programs should be able to import your pets.py module and perform operations like below:

    from pets import *
    d = Dog('fido',6,'great dane')
    c = Cat('sparky',6, 'siamese')
    print(d) # should print something like "fido, great dane, age: 6 (44 dog yrs)"
    print(c) # should print something like "sparky, siamese, age: 6 (40 cat yrs)"
 
**Hints**

- You can use a python data collection to map human years to pet years, or you can use conditional logic. Consider which is easier and what kind of collection might work best,
- See my example of class inheritance here - https://canvas.seattlecentral.edu/files/73429878/ 
- Each of your sub-classes will need a method to calculate non-human age. Ideally, you would name this method the same in each sub-class,
- For simplicity, you may want each subclass to have its own __str__ method 
