

class table:
    """
    self.itterate_button = moves the button by adding one, loops with number of players
    self.change_table_BB = changes the big blind
    self.change_table_SB = changes the small blind

    self.set_min_bet = sets the min bet amount in player.py



    """
    def __init__(self, num_players, Big_blind, small_blind):
        self.num_players = num_players
        self.min_bet_amount = 0
        self.big_blind = Big_blind
        self.small_blind = small_blind
        self.button_postion = 0 

    def itterate_button(self):
        self.button_postion = (self.button_postion + 1) % self.num_players
        
    def _set_positive_attr(self, attr_name, value, label):
        if value <= 0:
            raise ValueError(f"{label} must be more than zero")
        setattr(self, attr_name, value)


    def change_table_BB(self, bigBlind):
        self._set_positive_attr('big_blind', bigBlind, 'Big blind')

    def change_table_SB(self, smallBlind):
        self._set_positive_attr('small_blind', smallBlind, 'Small blind')

    def set_min_bet(self, next_min_bet):
        self._set_positive_attr('min_bet_amount', next_min_bet, 'Minimum bet')

