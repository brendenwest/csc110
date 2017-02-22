
This week you learned the basic principles of object-oriented programming, and how classes model real-world objects.

Now you can use this knowledge to simulate playing-cards. 

- Implement a class called Card to represent a playing card. The class should have the following methods:

- __init__(self, rank, suit)  - to create a new card. rank is an int in the range 1-13 indicating the ranks from Ace (1) to King (13). suit is a single character - 'd', 'c', 'h', or 's' indicating the suit (diamonds, clubs, hearts, or spades)

- getRank(self) - returns the card's rank
- getSuit(self) - returns the card's suit
- BJValue(self) - returns the card's Blackjack value (Ace = 1, face cards = 10)
- __str__(self) - returns the card's full name (e.g. "Ace of Spades")

Save your class in a file called card.py

Other programs should be able to import your class and create a card like this:

    from card import Card
    c = Card(1,"s")
    print(c.getRank()) # should print 1
    print(c.getSuit()) # should print 's' or 'Spades'
    print(c.getBJValue()) # should print 10 for face cards & rank for others
    print(c)  # should print 'Ace of Spades'

**Hint**

- Your __str__ method will need some way to match card rank and suit values with longer form values. Consider whether a list or a dictionary is better for each.  

**Extra Credit**

Write a function in card.py, but not part of the Card class, that asks the user whether to draw a card. If the user agrees, the function should create a new card with randomly selected value and suit. The program should display the combined total of Blackjack values after each draw, and prompt the user to draw another card until the total exceeds 21. 