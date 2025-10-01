mat = [[0,0],[0,0]]
mat [1][1] = 1

print(mat)


#print("sag was: ")
#input = input()                # nicht int input führt zu Fehlern
#if (input == ("0" or "1" or "2" or "3")):
#    #spielbrett[0][1] = x
#    input = int(input)
#    print("passt")
#else:
#    print("passt nicht")
    
    
    
class Spieler(object):
    
    def __init__(self, icon = str):
        self.icon = icon            # zweites icon bezieht sich auf Attribut der Methode
        
p1 = Spieler("x")
p2 = Spieler("o")

print(p1.icon)