from abc import ABC, abstractmethod
import random



class PlayerInterface(ABC): # AbstractBaseClass
    @abstractmethod
    def GetTurn(self, board):
        pass    
        # mehr macht es nicht


class Player(PlayerInterface):
    
    def __init__(self, icon: str):
        self.icon = icon 
   
    def PlayerMessage(self):
        """ Zeig den Spieler im Terminal an, der den nächsten Zug angibt """
        print(f'Spieler {self.icon} ist dran')
        
    def GetTurn(self, board):
        """ beschreiben """
        while True:             # SR
            self.PlayerMessage()        # SR
            try:
                return int(input('Spalte eingeben: ')) # Benutzereingabe in Ganzzahl
            except ValueError:
                continue # versuche es erneut, gehe zum Anfang der Schleife


class AutoPlayer(Player):           # ergibt automatisch alles?
    
    def __init__(self, icon: str, col_num):
        super().__init__(icon)
        self.col_num = col_num
    
    def GetTurn(self, board):
        """ beschreiben """
        random_move = random.randint(0, self.col_num)
        return random_move