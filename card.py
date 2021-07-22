"""
Design a class to represent a playing card. Now design a class to represent a deck of
cards. Using these two classes, implement a favorite card game.
"""

class Card:

	

	def __init__(self,value,cardclass):
		self.value = value
		self.cardclass = cardclass

	def __str__(self):
		return "This card is "+ self.value + " of " + self.cardclass


class Deck:

	values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
	cardclasses = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

	


	def __init__(self):
		self.cardDeck = []
		self.construct_deck()


	def construct_deck(self):
		for v in self.values:
			for c in self.cardclasses:
				self.cardDeck.append(Card(v,c))

	def __str__(self):
		s = ""
		for i in range(len(self.cardDeck)):
			s += " " * i + str(self.cardDeck[i]) + "\n"
		return s


	
				
	
card1 = Card('King','Spades')
deck = Deck()


print (card1)
print (deck)




