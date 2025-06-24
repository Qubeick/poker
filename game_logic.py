from dealing_logic import DealingLogic



class GameLogic(DealingLogic,):
    def __init__(self, num_players):
        super().__init__(num_players)
        