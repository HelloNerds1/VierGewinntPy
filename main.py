from VierGewinntPy.player import Player, AutoPlayer
from VierGewinntPy.VierGewinnt import VierGewinnt
    

        
if __name__ == "__main__":      # SR
    # int main()
    # {

    """ Settings """
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
    vier_gewinnt = VierGewinnt(row_num, col_num)
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
    print("GEWONNEN")


    """Testbereich"""

    # return 0; 
    # }

    # :)


