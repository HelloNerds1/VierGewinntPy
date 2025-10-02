


class Spieler:
    
    def __init__(self, icon = str):
        self.icon = icon 
        
    def GetTurn(self, Field):
        # Feld printen
        value = int(input('Spalte eingeben: '))
        return value



class AutoSpieler:
    
    def __init__(self):
        pass
    
    def GetTurn(self, Field):
        # wo denkt der Computer, dass es hingehört?
        pass
        



def Spielbrett(zeile, spalte):
    """ Diese Funktion erstellt das Spielbrett. Hierbei werden mehrere Listen in eine Liste 
    zusammengefügt, um eine Matrix zu erstellen. """
    for m in range(row_num):
        zeile = []
        for n in range(col_num):
            zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen      # av, vllt. Leerzeichen in ASCII?
        spielbrett.append(zeile)
    

def Ausgabe(row_num, col_num):
    """ In dieser Funktion wird das Spielbrett für die Konsole formatiert ausgegeben. 
    Dazu wird die Spielbrett Matrix durchgegenagen, wobei für jeden Eintrag ein leeres Feld eingefügt wird. """
    print("0     1     2     3")    # av
    for i in range(row_num):
        for j in range(col_num):
            print(spielbrett[i][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
        print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch


def Abfrage(zeile, spieler):
    """ beschreiben """
    while True:             # SR
        try:
            value = int(input('Spalte eingeben: ')) # Benutzereingabe in Ganzzahl
            global counter 
            global col0
            global col1
            global col2
            global col3
            counter = counter +1
            
            """ Gedächtinis über die Züge: """
            if value < zeile:   # Hier wird gegengespüft, ob die eingegebene Zahl auch innerhalb des Spielfeldes liegt
                if value == 0:
                    spielbrett[col0][value] = spieler   # hier wird das gewünschte Spieler-Symbol genutzt
                    col0 = col0 +1
                if value == 1:
                    spielbrett[col1][value] = spieler
                    col1 = col1 +1
                if value == 2:
                    spielbrett[col2][value] = spieler
                    col2 = col2 +1            
                if value == 3:
                    spielbrett[col3][value] = spieler
                    col3 = col3 +1         
 
        except:
            continue # versuche es erneut, gehe zum Anfang der Schleife
        break # verlässt die while-Schleife, Wert definitiv eine Ganzzahl
    
    
    


def checkWin():
    
    """ horizontal """
    for col in range(col_num-3):        # -3 aufgrund der range   SR
        for row in range(row_num):
            if(spielbrett[row][col] == spielbrett[row][col+1] == spielbrett[row][col+2] == spielbrett[row][col+3] != " "):
                print("Gewonnen")
    
    """ vertikal """
    for col in range(col_num):        
        for row in range(row_num -3):
            if(spielbrett[row][col] == spielbrett[row+1][col] == spielbrett[row+2][col] == spielbrett[row+3][col] != " "):
                print("Gewonnen")
 
    """ diagonal hochzu """
    for col in range(col_num):       
        for row in range(row_num -3):
            if(spielbrett[row][col] == spielbrett[row+1][col+1] == spielbrett[row+2][col+2] == spielbrett[row+3][col+3] != " "):
                print("Gewonnen")  
                
    """ diagonal herunter """
    for col in range(col_num):        # SR
        for row in range(row_num -3):
            if(spielbrett[row][col] == spielbrett[row+1][col-1] == spielbrett[row+2][col-2] == spielbrett[row+3][col]-3 != " "):
                print("Gewonnen") 
    

        
        
# int main()
# {

""" Settings für Matrix etc. """
spielbrett = []
row_num = 4
col_num = 4

counter = 0
col0 = 0
col1 = 0
col2 = 0
col3 = 0

""" Funktionen aufrufen """
board = Spielbrett(row_num, col_num)   #ab hier ist Spielbrett befüllt

""" Spieler """
player1 = Spieler("x")
player2 = Spieler("o")

0
""" Spielschleife """
ausgeben = Ausgabe(row_num, col_num) 
while counter < 8:
    if (counter % 2) == 0:
        abfrage = Abfrage(row_num, player1.icon)
        ausgeben = Ausgabe(row_num, col_num) 
        win = checkWin()
    elif (counter % 2) == 1:
        print("I am odd")
        abfrage = Abfrage(row_num, player2.icon)
        ausgeben = Ausgabe(row_num, col_num) 

"""Testbereich"""

print(col2)


# return 0; 
# }

# :)


