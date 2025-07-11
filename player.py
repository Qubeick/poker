class player:
    """
    def reset_hole_cards = this resets the hole cards to a empty list
    def set_hole_cards(new_hole_cards) = this takes a input from the deck.dealer[player_seat]


    def subtract_from_chip_stack(num) = self explanitory
    def add_to_chip_stack(num) = adds to chip stack
    """


    def __init__(self, buy_in:int, player_seat):

        self.chip_stack = buy_in
        self.player_hole_card = []
        self.in_hand = False
        self.player_seat = player_seat


    # hole card logic
    def reset_hole_Cards(self):
        self.player_hole_card = []
        self.in_hand = False

    def set_hole_cards(self, new_hole_cards):
        self.player_hole_card = new_hole_cards
        self.in_hand = True

    #  math of chip stack
    
    def subtract_from_chip_stack(self, subtracting):
        self.chip_stack -= subtracting

    def add_to_chip_stack(self, add):
        self.chip_stack += add 


    # when betting you remove the chips from your stack, set the new min bet amount

    def betting(self, betting_amount: int, min_betting_amount: int, pot: int) -> int:
        if betting_amount <= 0:
            raise ValueError('Bet must be above zero')
        if betting_amount < min_betting_amount:
            raise ValueError(f'Must bet at least {min_betting_amount}')
        if betting_amount > self.chip_stack:
            raise ValueError('Bet cannot exceed chip stack')
        
        self.chip_stack -= betting_amount
        pot += betting_amount
        
        min_betting_amount = betting_amount
        return pot, self.chip_stack, min_betting_amount





if __name__ == '__main__':
    player0 = player(500,player_seat=0)

    pot,chip_stack,min_betting_amount = player0.betting(10,10,0)

print(pot,chip_stack,min_betting_amount)

        
