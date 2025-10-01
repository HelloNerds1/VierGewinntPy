
    

def Spielbrett(zeile, spalte):
    """ Diese Funktion erstellt das Spielbrett. Hierbei werden mehrere Listen in eine Liste 
    zusammengefügt, um eine Matrix zu erstellen. """
    for m in range(zeile):
        zeile = []
        for n in range(spalte):
            zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen      # av, vllt. Leerzeichen in ASCII?
        spielbrett.append(zeile)
    

def Ausgabe(zeile, spalte):
    """ In dieser Funktion wird das Spielbrett für die Konsole formatiert ausgegeben. 
    Dazu wird die Spielbrett Matrix durchgegenagen, wobei für jeden Eintrag ein leeres Feld eingefügt wird. """
    print("0     1     2     3")    # av
    for i in range(zeile):
        for j in range(spalte):
            print(spielbrett[i][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
        print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch
        


class Spieler(object):
    
    def __init__(self, icon = str):
        self.icon = icon            
        



def Abfrage(zeile, spieler):
    """ beschreiben """
    while True:
        try:
            value = int(input('Spalte eingeben: ')) # versuche, die Benutzereingabe in eine Ganzzahl umzuwandeln, könnte fehlschlagen
            global counter 
            global col0
            global col1
            global col2
            global col3
            counter = counter+1
            if value == 0:
                if spielbrett_logik[col0][counter] == True:
                    col0 = col0 +1
            elif value == 1:
                col1 = col1 +1
            elif value == 2:
                col2 = col2 +1            
            elif value == 3:
                col3 = col3 +1 
            else:
                return          # ergibt das Sinn? av        wichtig          
            
            
            if value < zeile:
                spielbrett[0][value] = spieler
                
                
            if spielbrett_logik[col0][value] == True:
                spielbrett[col0][value] = spieler
            else:
                print("passt nicht")
        except:
            continue # versuche es erneut, gehe zum Anfang der Schleife
        break # verlässt die while-Schleife, Wert definitiv eine Ganzzahl
    
    

def SpielbrettLogik(zeile, spalte):
    """beschreiben"""
    for m in range(zeile):
        zeile = []
        for n in range(spalte):
            zeile.append(False)             # Spielbrett mit False Einträgen füllen
        spielbrett_logik.append(zeile)
    
def AbfrageLogik():
    if spielbrett[col0][counter] == "x":
        spielbrett_logik[col0][counter] == True
    if spielbrett[col1][counter] == "x":
        spielbrett_logik[col1][counter] == True
    if spielbrett[col2][counter] == "x":
        spielbrett_logik[col2][counter] == True
    if spielbrett[col3][counter] == "x":
        spielbrett_logik[col3][counter] == True


        
        
# int main()
# {

""" Settings für Matrix etc. """
spielbrett = []
spielbrett_logik = []
zeile = 4
spalte = 4

counter = 0
col0 = 0
col1 = 0
col2 = 0
col3 = 0

""" Funktionen aufrufen """
board = Spielbrett(zeile, spalte)   #ab hier ist Spielbrett befüllt
logic_board = SpielbrettLogik(zeile, spalte)

""" Spieler """
player1 = Spieler("x")
player2 = Spieler("o")

""" Spielschleife """
ausgeben = Ausgabe(zeile, spalte) 
while counter < 4:
    if (counter % 2) == 0:
        abfrage = Abfrage(zeile, player1.icon)
        ausgeben = Ausgabe(zeile, spalte) 
    elif (counter % 2) == 1:
        print("ich bin ungerade")
        abfrage = Abfrage(zeile, player2.icon)
        ausgeben = Ausgabe(zeile, spalte) 

"""Testbereich"""



# return 0; 
# }

# :)


