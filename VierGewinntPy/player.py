from abc import ABC, abstractmethod
from VierGewinntPy.VierGewinnt import VierGewinnt
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
        # kann Bot gewinnen?
        for i in range(self.col_num):
            vier_gewinnt = VierGewinnt.FromBoard(board)
            is_valid = vier_gewinnt.SetMove(self.icon, i)  # i aus Schleife
            if is_valid:
                win = vier_gewinnt.CheckWin()
                if win:
                    print(f"Autoplayer {self.icon}: gewinnende Spalte {i}")
                    return i
        
        # verhindere gewinnenn des Spielers
        for i in range(self.col_num):
            vier_gewinnt = VierGewinnt.FromBoard(board)
            enemy_icon = list(vier_gewinnt.icons-{self.icon})[0]        # Differenz der Menge -> daraus Liste für 0. Element
            is_valid = vier_gewinnt.SetMove(enemy_icon, i)  # i aus Schleife
            if is_valid:
                win = vier_gewinnt.CheckWin()
                if win:
                    print(f"Autoplayer {self.icon}: verhindernde Spalte {i}")
                    return i
        
        # wenn ncihts geht, dann random move
        random_move = random.randint(0, self.col_num)
        print(f"Autoplayer {self.icon}: Spalte {random_move}")
        return random_move

    