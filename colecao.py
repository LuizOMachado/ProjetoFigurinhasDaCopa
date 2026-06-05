from modelos import Figurinha
from estruturas import Album

class Colecao:
    """Gerencia o álbum principal e o bolo de figurinhas repetidas do usuário."""
    
    def __init__(self):
        self.album_principal = Album() # Onde ficam as figurinhas coladas
        self.repetidas = Album()       # Onde ficam as repetidas
