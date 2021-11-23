''''
from Tablero import Tablero
from Guerrero import Guerrero

tab = Tablero(4,4)

superman = Guerrero('Superman', 100, 50, 60, 30, 20, '⚔')
goku = Guerrero('Gokua', 100, 75, 50, 95, 85,'☭')

tab.colocarGuerrero(superman, "a0")


print(str(tab))
'''

from Juego import Juego
j = Juego()
j.empezar()

