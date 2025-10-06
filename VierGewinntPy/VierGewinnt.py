class VierGewinnt():
    
    def __init__(self, row_num, col_num):
        """ Init Funktion der VierGewinnt Klasse -
        - VierGewinnt() verarbeitet die interne Spiellogik, also alles, was nicht vom Spieler/Autospieler 
          übernommen wird. """
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
        self.board = []
        self.Spielbrett()       # Methode zur Matrixerstellung aufrufen
        self.icons = {"x", "o"} # ein Set
    
    @classmethod
    def FromBoard(cls, board: list[list[str]]):
        """ Diese Methode ist für den AutoSpieler in player.py notwendig.
        Dabei wird ein neues Vier Gewinnt Objekt von einem Board generiert. """
        row_num = len(board)
        col_num = len(board[0])
        vier_gewinnt = VierGewinnt(row_num, col_num)    # Aufruf zu __init__
        for i in range(row_num):
            for j in range(col_num):
                vier_gewinnt.board[i][j] = board[i][j]
                if board[i][j] != " ":
                    if j == 0:
                        vier_gewinnt.col0 = i+1
                    if j == 1:
                        vier_gewinnt.col1 = i+1
                    if j == 2:
                        vier_gewinnt.col2 = i+1
                    if j == 3:
                        vier_gewinnt.col3 = i+1
                    if j == 4:
                        vier_gewinnt.col4 = i+1
                    if j == 5:
                        vier_gewinnt.col5 = i+1
                    if j == 6:
                        vier_gewinnt.col6 = i+1
                    
        return vier_gewinnt
        
    
    def Spielbrett(self):
        """ Diese Funktion erstellt das Spielbrett. Hierbei werden mehrere Listen in eine Liste 
        zusammengefügt, um eine Matrix zu erstellen. Die einzelnen Einträge werden mit Leerzeichen gefüllt """
        for m in range(self.row_num):
            zeile = []
            for n in range(self.col_num):
                zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen
            self.board.append(zeile)           

    def Output(self):
        """ In dieser Funktion wird das Spielbrett für die Konsole formatiert ausgegeben. 
        Dazu wird die Spielbrett-Matrix durchgegenagen, wobei am Ende jedes Eintrages ein 
        Separierunsstrich eingefügt wird. Ebenso entstehn hier die Zeilenumbrüche der einzelnen Zeilen """
        print("0     1     2     3     4     5     6")    
        for i in range(self.row_num):
            for j in range(self.col_num):
                print(self.board[self.row_num-i-1][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
            print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch
            
            
    def SetMove(self, icon, value):
        """ In der Methode SetMove wird der Input des Spielers verarbietet. 
        Dabei wird zuerst abgefragt, ob die ausgewählte Spalte auch innerhalb des Spielfeldes liegt. 
        Daraufhin wird überprüft, ob die gewünschte Spalte schon voll ist. Falls dies nicht der Fall ist, wird
        der Zähler für die Spalten um eins erweitert, um zu signalisieren, in welche Zeile der nächste Zug gehört.
        Jede Spalte hat dabei ihren eigenen Zähler. """
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
                    return True

        """ vertikal """
        for col in range(self.col_num -3):        
            for row in range(self.row_num -3):
                if(self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != " "):
                    return True
    
        """ diagonal hochzu """
        for col in range(self.col_num -3):       
            for row in range(self.row_num -3):
                if(self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != " "):
                    return True

        """ diagonal herunter """
        for col in range(self.col_num):        
            for row in range(self.row_num -3):
                if(self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] != " "):
                    return True
        return False