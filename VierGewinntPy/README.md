# Vier Gewinnt

## Struktur

### main.py
In der main.py Datei befindet sich die eigentliche Spielschleife, in der das Spiel läuft sowie die Abfrage darüber, wieviele Spieler das Spiel spielen möchten (Ein- oider Zweispielermodus).


### VierGewinnt.py
In "VierGewinnt.py" steht die eigentliche Logik für das Spiel, die in jedem Fall ausgeführt wird. Dazu gehören die Methoden 
- `__init__(self, row_num, col_num)` \
    initialisierung
- `FromBoard(cls, board: list[list[str]])` \
    für Planung von AutoPlayer
- `Spielbrett(self)` \
    erstellt die Matrix für das Spielbrett
- `Output(self)` \
    gibt das Spielbrett formatiert aus
- `SetMove(self, icon, value)` \
    setzt den input aus der EIngabe von main.py in das Spielfeld ein
- `CheckWin(self)` \
    schaut über das Spielbrett, ob jemand gewonnen hat


### player.py
In player.py befinden sich die Klassen "Player" und "AutoPlayer". Hier werden die menschlichen und manuellen Spieler erstellt.

#### Player()
- `__init__(self, icon: str)` \
    initialisieren
- `PlayerMessage(self)` \
    gibt eine Nachricht aus, wer gerade am Zug ist
- `GetTurn(self, board)` \
    "PlayerMessage()" wird hier aufgerufen, außerdem wird die gewünschte Spalte vom Spieler angefordert

#### AutoPlayer(Player) 
    erbt von Player
- `_init__(self, icon: str, col_num)` \
    initialisieren
- `GetTurn(self, board)` \
    überschreibt die geerbte Methode von Player -> überprüft zusätzlich, ob der Automatische Gegner gewinnen kann oder das Gewinnen des menschlichen Spielers verhindern kann. Ansonsten wird ein willkürlicher Zug gesetzt


## Anleitung
Bei beginn des Spieles wird zuerst nach den Zahlen ”1” für Einspielermodus oder ”2” für
Zweispielermodus gefragt. Nach der Auswahl des Modus wird das Spiel über die Eingabe
der gewünschten Spalte über die Tastatur gesteuert.