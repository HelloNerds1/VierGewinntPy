from abc import ABC, abstractmethod
import random
#from VierGewinntPy.player import *

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



class VierGewinnt():
    
    def __init__(self, board, row_num, col_num):
        """ beschreiben """
        self.board = board
        self.row_num = row_num
        self.col_num = col_num
        # alles was nicht mit übergeben wird:
        self.col0 = 0
        self.col1 = 0
        self.col2 = 0
        self.col3 = 0
        self.col4 = 0
        self.col5 = 0
        self.col6 = 0
        self.value = None
        self.Spielbrett()
    
    def Spielbrett(self):
        """ Diese Funktion erstellt das Spielbrett. Hierbei werden mehrere Listen in eine Liste 
        zusammengefügt, um eine Matrix zu erstellen. """
        for m in range(self.row_num):
            zeile = []
            for n in range(self.col_num):
                zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen      # av, vllt. Leerzeichen in ASCII?
            self.board.append(zeile)            # SR

    def Ausgabe(self):
        """ In dieser Funktion wird das Spielbrett für die Konsole formatiert ausgegeben. 
        Dazu wird die Spielbrett Matrix durchgegenagen, wobei für jeden Eintrag ein leeres Feld eingefügt wird. """
        print("0     1     2     3     4     5     6")    
        for i in range(self.row_num):
            for j in range(self.col_num):
                print(self.board[self.row_num-i-1][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
            print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch
            
            
    def SetMove(self, icon, value):
        if value < self.col_num:   # Hier wird gegengespüft, ob die eingegebene Zahl auch innerhalb des Spielfeldes liegt
            if value == 0:
                if self.col0 >= self.row_num:
                    return False
                self.board[self.col0][value] = icon   # hier wird das gewünschte Spieler-Symbol genutzt
                self.col0 = self.col0 +1  
                return True 
                
            if value == 1:
                if self.col1 >= self.row_num:
                    return False
                self.board[self.col1][value] = icon
                self.col1 = self.col1 +1 
                return True 
                 
            if value == 2:
                if self.col2 >= self.row_num:
                    return False
                self.board[self.col2][value] = icon
                self.col2 = self.col2 +1   
                return True 
                     
            if value == 3:
                if self.col3 >= self.row_num:
                    return False
                self.board[self.col3][value] = icon
                self.col3 = self.col3 +1   
                return True 
                       
            if value == 4:
                if self.col4 >= self.row_num:
                    return False
                self.board[self.col4][value] = icon
                self.col4 = self.col4 +1  
                return True 
                  
            if value == 5:
                if self.col5 >= self.row_num:
                    return False
                self.board[self.col5][value] = icon
                self.col5 = self.col5 +1  
                return True  
                
            if value == 6:
                if self.col6 >= self.row_num:
                    return False
                self.board[self.col6][value] = icon
                self.col6 = self.col6 +1  
                return True   
        return False                
             

    def CheckWin(self) -> bool:
        """ In dieser Methode wird überprüft, ob vier Steine einer Art aneinander liegen. 
        Falls vier Steine beeinander liegen, gibt die Methode den boolschen Wert True zurück, woraufhin 
        die Spielschleife beendet wird. """

        """ horizontal """
        for col in range(self.col_num-3):        # -3 aufgrund der range
            for row in range(self.row_num):
                if(self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] != " "):
                    print("Gewonnen")
                    return True

        """ vertikal """
        for col in range(self.col_num -3):        
            for row in range(self.row_num -3):
                if(self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != " "):
                    print("Gewonnen")
                    return True
    
        """ diagonal hochzu """
        for col in range(self.col_num -3):       
            for row in range(self.row_num -3):
                if(self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != " "):
                    print("Gewonnen")  
                    return True

        """ diagonal herunter """
        for col in range(self.col_num):        # SR
            for row in range(self.row_num -3):
                if(self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] != " "):
                    print("Gewonnen") 
                    return True
        return False
    

        
if __name__ == "__main__":      # SR
    # int main()
    # {

    """ Settings """
    board = []
    counter = 0
    row_num = 8
    col_num = 7
    win = False
    END = 42     # bessere Lesbarkeit

    """ Auswahl des Modus"""
    modi = None
    while modi == None:
        try:
            modi = int(input('Spieleranzahl eingeben: '))
        except ValueError:      # SR
            continue
        if modi == 1:
            print("Einspielermodus")
        elif modi == 2:
            print("Zweispielermodus")
        else:
            modi = None

            

    """ Instanzen """
    vier_gewinnt = VierGewinnt(board, row_num, col_num)
    player1 = Player("x")
    player2 = Player("o")
    if modi == 1:
        player2 = AutoPlayer("o", col_num)


    """ Spielschleife """
    ausgeben = vier_gewinnt.Ausgabe() 

    while win != True:
        if (counter % 2) == 0:
            is_valid = False
            while not is_valid:
                value = player1.GetTurn(vier_gewinnt.board)
                is_valid = vier_gewinnt.SetMove(player1.icon, value)
            vier_gewinnt.Ausgabe() 
            win = vier_gewinnt.CheckWin()
            
        elif (counter % 2) == 1:
            is_valid = False
            while not is_valid:
                value = player2.GetTurn(vier_gewinnt.board)
                is_valid = vier_gewinnt.SetMove(player2.icon, value)
            vier_gewinnt.Ausgabe() 
            win = vier_gewinnt.CheckWin()    
        counter = counter + 1


    """Testbereich"""

    # return 0; 
    # }

    # :)


