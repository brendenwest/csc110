# Card class
'''
class should have:
 __init method
rank
suite
value
__repr__ method
'''
class Card:
    suites = {'d':'Diamonds', 'c':'Clubs','h':'Hearts','s':'Spades'}
    names = ["Ace","Two", "Three","Four",'Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    
    def __init__(self, rank, suite):
        self.rank = rank
        self._suite = suite
    
    @property
    def suite(self):
        # should return full name - e.g. Diamonds
        return Card.suites[self._suite]
        
    @property
    def value(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10
        
    def __repr__(self):
        return "{0} of {1}".format(Card.names[self.rank-1],Card.suites[self._suite])
        
    
    @staticmethod
    def playBlackJack():
        import random

        '''        
        - prompt user to draw card
        - select a card at random
        - display total BJ value
        - prompt for new card as long as total < 21
        
        '''
        total = 0
        # create deck of cards
        deck = []
        for i in range(len(Card.names)):
            for s in Card.suites.keys():
                deck.append(Card(i+1,s))
                
        # select card at random
        while input("Draw a card? (y/n) ") == 'y':
            # selects a card at random w/o removing from deck            
#            c = random.choice(deck)

            # selects a random card and removes from deck
            # deck length reduced each time a card is drawn
            print(len(deck))
            cardnum = random.randrange(len(deck))
            c = deck.pop(cardnum)
    
            # add card BJ value to total
            total += c.value

            # display total & message
            print("You drew : ",c)
            print("Your hand is now: ",total)
            if total > 21:
                print("you lose!")
                break
        