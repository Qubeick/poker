from abc import ABC, abstractmethod

class ChipsOnTable:
    def __init__(self, max_buy_in, players_stacks):
        #self.max = max_buy_in
        #need to get this working

        #Keeps track of every players stacks
        self.players_stacks = players_stacks
        self.pot = 0 
        
    
    def add_to_pot(self, amount):
        if amount  > 0:
            self.pot += amount  

    def subtract_from_player_stack(self, amount, player_index):
            if 0 <= player_index < len(self.players_stacks) and amount > 0:
                if self.players_stacks[player_index] >= amount:
                    self.players_stacks[player_index] -= amount
                else:
                    print("Not enough chips to subtract.")
            else:
                print("Invalid player index or amount.")
            


class Player:


    def __init__(self, Player_index, ChipsOnTable, hole_cards):
        self.chip_stack = ChipsOnTable.players_stacks[Player_index]
        self.seat = 0
        self.hole_cards = hole_cards
        #player in hand
        self.pin = False



    def __str__(self):
        return f'Player {self.seat} | Chips: {self.stack}'
    
    def grab_hand(self, players_hands):
        self.hole_cards = players_hands[self.seat]
        self.pin = True

    def muck_hand(self):
        self.pin = False
        self.hole_cards = []

#possible player actions
class Ppa:
    @abstractmethod
    def betting():
        pass
    
    @abstractmethod
    def raising():
        pass

    @abstractmethod
    def check():
        pass

    @abstractmethod
    def fold():
        pass

class TerminalHumanPlayer(Player, Ppa):

    def __init__(self, ChipsOnTable, hole_cards):
        super().__init__(ChipsOnTable, hole_cards)

    
    def betting(self):

        
        while True:
            try:
                print(f'total chips:{self.chip_stack}')
                betting_ammount = input('how much would you like to bet')
                if betting_ammount > self.chip_stack:
                    print('not enough chips')
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
                    
        print(f'the pot is equal to {ChipsOnTable.pot}')
                    