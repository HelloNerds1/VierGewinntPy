import random
#from VierGewinntPy.player import *


class Player:
    
    def __init__(self, icon: str):
        self.icon = icon 
   
    def PlayerMessage(self):
        """ Zeig den Spieler im Terminal an, der den nächsten Zug angibt """
        print(f'Spieler {self.icon} ist dran')



class AutoPlayer(Player):           # ergibt automatisch alles?
    
    def __init__(self, board, row_num, icon: str):
        self.board = board
        self.row_num = row_num
        super().__init__(icon)
    
    def GetTurn(self):
        """ beschreiben """
        random_move = random.randint(0, self.row_num)
        #board[][random_move]
        


class VierGewinnt():
    
    def __init__(self, board, row_num, col_num):
        """ beschreiben """
        self.board = board
        self.row_num = row_num
        self.col_num = col_num
        # alles was nicht mit übergeben wird:
        self.counter = 0
        self.col0 = 0
        self.col1 = 0
        self.col2 = 0
        self.col3 = 0
        self.col4 = 0
        self.col5 = 0
        self.col6 = 0
    
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

    def Abfrage(self, spieler):
        """ beschreiben """
        while True:             # SR
            try:
                value = int(input('Spalte eingeben: ')) # Benutzereingabe in Ganzzahl
                global counter 
                counter = counter +1

                if value < self.row_num:   # Hier wird gegengespüft, ob die eingegebene Zahl auch innerhalb des Spielfeldes liegt
                    if value == 0:
                        self.board[self.col0][value] = spieler   # hier wird das gewünschte Spieler-Symbol genutzt
                        self.col0 = self.col0 +1
                        break
                    if value == 1:
                        self.board[self.col1][value] = spieler
                        self.col1 = self.col1 +1
                        break
                    if value == 2:
                        self.board[self.col2][value] = spieler
                        self.col2 = self.col2 +1
                        break         
                    if value == 3:
                        self.board[self.col3][value] = spieler
                        self.col3 = self.col3 +1      
                        break   
                    if value == 4:
                        self.board[self.col4][value] = spieler
                        self.col4 = self.col4 +1    
                        break
                    if value == 5:
                        self.board[self.col5][value] = spieler
                        self.col5 = self.col5 +1    
                        break
                    if value == 6:
                        self.board[self.col6][value] = spieler
                        self.col6 = self.col6 +1    
                        break           
            except:
                continue # versuche es erneut, gehe zum Anfang der Schleife
             

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
    

        
        
# int main()
# {

""" Settings """
board = []
counter = 0
row_num = 8
col_num = 7
win = False



""" Instanzen """
vier_gewinnt = VierGewinnt(board, row_num, col_num)
player1 = Player("x")
player2 = Player("o")


""" Spielschleife """
board = vier_gewinnt.Spielbrett()        # Erstellt die Matrix die als Spielbrett genutzt wird
ausgeben = vier_gewinnt.Ausgabe() 

END = 42     # bessere Lesbarkeit
while True:
    try:
        modi = int(input('Spieleranzahl eingeben: '))
        if modi == 1:
            print("Einspielermodus")
            while win != True:
                if (counter % 2) == 0:
                    player1.PlayerMessage()
                    abfrage = vier_gewinnt.Abfrage(player1.icon)
                    ausgeben = vier_gewinnt.Ausgabe() 
                    win = vier_gewinnt.CheckWin()
                elif (counter % 2) == 1:
                    player2.PlayerMessage()
                    abfrage = vier_gewinnt.Abfrage(player2.icon)
                    ausgeben = vier_gewinnt.Ausgabe() 
                    win = vier_gewinnt.CheckWin()    
            break   
        
        if modi == 2:
            print("Zweispielermodus")
            while win != True:
                if (counter % 2) == 0:
                    player1.PlayerMessage()
                    abfrage = vier_gewinnt.Abfrage(player1.icon)
                    ausgeben = vier_gewinnt.Ausgabe() 
                    win = vier_gewinnt.CheckWin()
                elif (counter % 2) == 1:
                    player2.PlayerMessage()
                    ausgeben = vier_gewinnt.Ausgabe() 
                    win = vier_gewinnt.CheckWin()   
            break
        
        if modi == END:
            print("Spiel beendet")
            break
    except:
        continue


"""Testbereich"""


# return 0; 
# }

# :)


