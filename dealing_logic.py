from deck import Deck

class DealingLogic(Deck):

    def __init__(self, num_players):
        super().__init__()
        self.players_hands = []
        self.community_cards = []
        self.num_players = num_players
        #dealing state
        self.ds = 0


    def deal_cards(self, count):
        return [self.deck.pop() for _ in range(count)]

    def dealing_hole_cards(self):
        hole_cards = self.deal_cards(int(self.num_players * 2))
        self.players_hands = []  # Reset hands

        for p in range(self.num_players):
            hand = [hole_cards[p], hole_cards[p + self.num_players]]
            self.players_hands.append(hand)
            
        self.ds += 1 
    def dealing_community_cards(self):
        
        if self.ds == 0:
            print('need to deal hole cards first')
        elif self.ds == 1:
            self.deal_cards(1)
            flop = (self.deal_cards(3))
            self.community_cards.append(flop)
            self.ds += 1 
        elif self.ds == 2:
            self.deal_cards(1)
            turn = (self.deal_cards(1))
            self.community_cards.append(turn)
            self.ds += 1 
        elif self.ds == 3:
            self.deal_cards(1)
            river = (self.deal_cards(1))
            self.community_cards.append(river)
            self.ds = 0 


