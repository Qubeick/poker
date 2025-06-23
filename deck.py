import random

class Deck:

    def __init__(self):
        self.deck = []
        for i in range(52):
            self.deck.append(i)
        random.shuffle(self.deck)

    @staticmethod
    def translate_cards(cards):
        suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        def translate(card):
            return ranks[card % 13] + suits[card // 13]

        if isinstance(cards, int):
            return translate(cards)

        if isinstance(cards, list):
            if all(isinstance(c, list) for c in cards):  # list of lists
                return [[translate(c) for c in sublist] for sublist in cards]
            else:  # flat list
                return [translate(c) for c in cards]

        raise TypeError("Input must be an int, list, or list of lists")

