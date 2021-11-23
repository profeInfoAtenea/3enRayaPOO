from Celda import Celda
from Vacio import Vacio

class Tablero:

    def __init__(self, total_filas, total_columnas):
        self.__total_filas = total_filas
        self.__total_columnas = total_columnas
        self.__celdas = {}
        
        for i in range(0,total_filas):
            fila = i 
            for j in range(total_columnas):
                columna = self.__numero_a_letra(j)
                clave = columna+str(fila)
                v_celda = Celda(i,j, Vacio("_"))
                self.__celdas[clave] = v_celda
    
    def __str__(self):
        ret = ""
        for i in range(0,self.__total_filas):
            fila = i 
            ret += "\n"
            for j in range(0,self.__total_columnas):
                columna = self.__numero_a_letra(j)
                clave = columna+str(fila)
                v_celda = self.__celdas[clave]

                ret += " "+ str(v_celda.get_estado()) + ""
        return ret

    def __numero_a_letra(self,numero):
        letra = ['a','b','c','d','e','f','g', 'h']
        try:
            return letra[numero]
        except ValueError:
            print("Error")
    
    def colocar_pieza(self, pieza, coordenada):
        if(coordenada in self.coordenadas_vacias()):
            celda = self.__celdas[coordenada]
            celda.set_estado(pieza)
            self.__celdas[coordenada] = celda

    def celdas(self):
        return self.__celdas
    
    def coordenadas_vacias(self):
        coordenadasvacias = []
        for coordenada in self.__celdas:
            celda = self.__celdas[coordenada]
            if(type(celda.get_estado()) == Vacio):
                coordenadasvacias.append(coordenada)
        return coordenadasvacias

    def es_coordenada_vacia(self, coordenada):
        return coordenada in self.coordenadas_vacias()

