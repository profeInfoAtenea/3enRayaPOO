from Tablero import Tablero
from Jugador import Jugador
import os


class Juego:
    def __init__(self):
        self.__movimientos = []
        self.__tablero = Tablero(3,3)
        self.__jugador1 = Jugador('★')
        self.__jugador2 = Jugador('✪')

    def __imprime_tablero(self):
        os.system ("clear")
        print("Selecciona una coordenada correcta: ")
        print( self.__tablero.coordenadas_vacias())
        print(str( self.__tablero ))
        print( str(self.__jugador1)+": ", self.__coordenada_jugador(self.__jugador1))
        print(str(self.__jugador2)+": ", self.__coordenada_jugador(self.__jugador2))


    def empezar(self):
        while(True):
            self.__imprime_tablero()

            if(self.__turno()):
                jugador = self.__jugador1
            else:
                jugador = self.__jugador2
            
            coordenada = input("Jugador "+ str(jugador) + " dime coordenada: ")
            while(self.__tablero.es_coordenada_vacia(coordenada)):
                self.__tablero.colocar_pieza(jugador, coordenada)
                self.__movimientos.append(coordenada)
            
            if self.__es_ganador(jugador):
                self.__imprime_tablero()
                print("HA GANADO EL JUGADOR " +  str(jugador)  )
                return True
            if self.__es_empate():
                 self.__imprime_tablero()
                 print("EMPATE" )
                 return False


    def __turno(self):
        return len(self.__movimientos) % 2 == 0

    def __coordenada_jugador(self, jugador):
        coordenadas = []
        celdas = self.__tablero.celdas()
        for coordenada in celdas.keys():
           if(type(celdas[coordenada].get_estado())==Jugador) and (celdas[coordenada].get_estado()==jugador):
                   coordenadas.append(coordenada)
        return coordenadas
    
    def __es_ganador(self, jugador):

        coordenadasjugador = self.__coordenada_jugador(jugador)

        #columnas
        columna1 = ['a0','a1','a2']
        columna2=['b0','b1','b2']
        columna3=['c0','c1','c2']
        #filas
        fila1 = ['a0', 'b0', 'c0']
        fila2 = ['a1', 'b1', 'c1']
        fila3 = ['a2', 'b2', 'c2']
        #diagonales
        diag1 = ['a0','b1','c2']
        diag2 = ['a2','b1','c0']
        
        c1 = set(columna1).issubset(set(coordenadasjugador))
        c2 = set(columna2).issubset(set(coordenadasjugador))
        c3 = set(columna3).issubset(set(coordenadasjugador))

        f1 = set(fila1).issubset(set(coordenadasjugador))
        f2 = set(fila2).issubset(set(coordenadasjugador))
        f3 = set(fila3).issubset(set(coordenadasjugador))

        d1 = set(diag1).issubset(set(coordenadasjugador))
        d2 = set(diag2).issubset(set(coordenadasjugador))

        return c1 or c2 or c3 or f1 or f2 or f3 or d1 or d2

    def __es_empate(self):
        return (len(self.__movimientos) >= 8)
       


