from Estado import Estado

class Jugador(Estado):
    def __str__(self):
        return self.get_image()