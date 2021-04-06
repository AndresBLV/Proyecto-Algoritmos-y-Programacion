from objeto import Objeto

class Room(Objeto):
    def __init__(self, name, objeto):
        super().__init__(name)
        self.objeto = objeto




