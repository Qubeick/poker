import random
class deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['h', 'c', 'd', 's']  # hearts, diamonds, clubs, spades
        self.players = [[] for _ in range(num_players)]
        self.deck_of_cards = [rank + suit for suit in suits for rank in ranks]

    #shuffled deck
    def shuffle(self):
        random.shuffle(self.deck)
    
    #deals
    def deal(self, players_holecards, players_stack,cards_each):
        if players_holecards !=[]:
            raise ValueError('players still have hands')
        if any(stack == 0 for stack in players_stack):
            raise ValueError('At least one player has no chips.')
        else:
            for _ in range(cards_each):
                for player_hand in self.players:
                    card = deck.deal_card()
                    if card:
                        player_hand.append(card)