# hier ein neues Pythonspiel uwu
# diesmal 4 Gewinnt
# Objektorientiert

# coole Darstellung über Zeilenumbruch?


#Herzstück oder so
AusgesuchteSpalte = int(input("wohin? "))       # wichtig
    # ist ein Literal und somit seltsam




# Logik Spielbrett
def LogikSpielbrett(zeile, spalte):
    """ hier wird geschaut, ob der Eintrag im Feld schon getätigt wurde bzw. wird das Eingegebene verarbeitet """
    
            # counter um zu wissen, welche Spalten für die Zeile schon besetzt sind
    counter_0 = 0
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    zeile1 = zeile
    spalte1 = spalte
    
        
    spielbrett_logik = []
    for m in range(zeile1):
        zeile = []
        for n in range(spalte1):
            zeile.append(0)             # Spielbrett mit 0 füllen 
        spielbrett_logik.append(zeile)
            
    while counter_2 < 3:
            
        if AusgesuchteSpalte == 0:
            counter_0 += 1
            spielbrett_logik[counter_0][AusgesuchteSpalte] == 1
        if AusgesuchteSpalte == 1:
            counter_1 += 1
            spielbrett_logik[counter_1][AusgesuchteSpalte] == 1
        if AusgesuchteSpalte == 2:
            counter_2 += 1
            spielbrett_logik[counter_2][AusgesuchteSpalte] == 1
        if AusgesuchteSpalte == 3:
            counter_3 += 1    
            spielbrett_logik[counter_3][AusgesuchteSpalte] == 1
            
        print("ausgewähltes: ")
        print("0: ", counter_0)
        print("1: ", counter_1)
        print("2: ", counter_2)
        print("3: ", counter_3)
        
    
        #LogikSpielbrett(zeile_test, spalte_test)
        # Endlosschleife
    



# Spielbrett für die Ausgabe
spielbrett = []
zeile = 4
spalte = 4
for m in range(zeile):
    zeile = []
    for n in range(spalte):
        zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen      # av, vllt. Leerzeichen in ASCII?
    spielbrett.append(zeile)
    




# Eingabe in Spielbrett einarbeiten
        # --> Logik Spielbrett reyclen?
if AusgesuchteSpalte < len(spielbrett[0]):      # av, später muss sich die Zeile variable mit ändern
    spielbrett[0][AusgesuchteSpalte] = "x"      # av, später ausählbar
else:
    print("so viele Spalten gibt es heute nicht")
    


    

def Ausgabe(zeile, spalte):
    """ Spielbrett "hübsch" ausgeben lassen """     #av
    print("0     1     2     3")    # av
    for i in range(zeile):
        for j in range(spalte):
            print(spielbrett[i][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
        print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch
        

        
        
# sowas wie meine main()
zeile = 4
spalte = 4
logik = LogikSpielbrett(zeile, spalte)
ausgeben = Ausgabe(zeile, spalte)   

#input("mach mal noch was: ")

# return 0;         :P