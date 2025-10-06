from VierGewinntPy.player import Player, AutoPlayer
from VierGewinntPy.VierGewinnt import VierGewinnt
    

        
if __name__ == "__main__":      
    # int main()
    # {

    """ Settings """
    counter = 0
    row_num = 8
    col_num = 7
    win = False
    last_player = None


    """ Auswahl des Modus"""
    modi = None
    while modi == None:
        try:
            modi = int(input('Spieleranzahl eingeben: '))
        except ValueError:      
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
    ausgeben = vier_gewinnt.Output()    # um das Spielbrett schonmal sehen zu können

    while win != True:
        if (counter % 2) == 0:
            last_player = player1
            is_valid = False
            while not is_valid:
                value = player1.GetTurn(vier_gewinnt.board)
                is_valid = vier_gewinnt.SetMove(player1.icon, value)
            vier_gewinnt.Output() 
            win = vier_gewinnt.CheckWin()
            
        elif (counter % 2) == 1:
            last_player = player2
            is_valid = False
            while not is_valid:
                value = player2.GetTurn(vier_gewinnt.board)
                is_valid = vier_gewinnt.SetMove(player2.icon, value)
            vier_gewinnt.Output() 
            win = vier_gewinnt.CheckWin()    
        counter = counter + 1
    print(f"GEWONNEN: Player {last_player.icon}")


    # return 0; 
    # }

    # :)