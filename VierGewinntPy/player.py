from VierGewinntPy.VierGewinnt import VierGewinnt
import random


class Player():   
    """ In dieseer Klasse wird der Spieler ersetllt """
    
    def __init__(self, icon: str):
        """ In der Klasse Player wird der Manuelle Spieler ersetllt """
        self.icon = icon 
   
    def PlayerMessage(self):
        """ In dieser Methode wird der Spieler über einen String im Terminal angezeigt, der 
            den nächsten Zug angibt. Diese Methode wird in GetTurn aufgerufen. """
        print(f'Spieler {self.icon} ist dran')
        
    def GetTurn(self, board):
        """ In der Methode GetTurn wird die gwünschte Zeile abgefragt. Falls dieser Input kein Int-Wer ist, 
            wird erneut nach einer Spalte gefragt. 
            Board wird erst bei der Vererbung auf AutoPlayer benötigt """
        while True:             
            self.PlayerMessage()       
            try:
                return int(input('Spalte eingeben: ')) # Benutzereingabe in Ganzzahl
            except ValueError:
                continue # versuche es erneut, gehe zum Anfang der Schleife
    


class AutoPlayer(Player):
    """ In dieseer Klasse wird der Automatische Gegner für den Einspielermodus ersetllt """           
    
    def __init__(self, icon: str, col_num):
        super().__init__(icon)
        self.col_num = col_num
    
    def GetTurn(self, board):
        """ In der Methode GetTurn() befinden sich zwei Schleifen. 
        Die erste Schleife kümmert sich darum zu überprüfen, ob der Bot "AutoPlayer" gewinnnen kann.  
        Die zweite Schleife kümmert sich darum, dass das Gewinnen des manuellen Spielers verhindert wird."""
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
        
        # wenn nichts geht, dann random move
        random_move = random.randint(0, self.col_num)
        print(f"Autoplayer {self.icon}: Spalte {random_move}")
        return random_move

    