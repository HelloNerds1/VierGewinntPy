# testen

class Spieler:
    
    def __init__(self, icon = str):
        self.icon = icon 
   
    def PlayerMessage(self):
        print(f'Spieler {self.icon} ist dran')



class AutoSpieler:
    
    def __init__(self, icon = str):
        self.icon = icon 
   
    def PlayerMessage(self):
        print(f'Spieler {self.icon} ist dran')
    
    def GetTurn(self, Field):
        # wo denkt der Computer, dass es hingehört?
        pass