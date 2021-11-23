class Celda:
    def __init__(self, fila, columna, estado):
        self.__fila = fila
        self.__columna = columna
        self.__estado = estado
    
    def __str__(self):  
        return  self.__columna,  self.__fila
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_coordenada(self):
        return self.__columna,  self.__fila