from modelos import Figurinha
from estruturas import Album

class Colecao:
    """Gerencia o álbum principal e o bolo de figurinhas repetidas do usuário."""
    
    def __init__(self):
        self.album_principal = Album() # Onde ficam as figurinhas coladas
        self.repetidas = Album()       # Onde ficam as repetidas

    def receber_pacotinho(self, figurinha: Figurinha):
        """Verifica se já tem no álbum. Se tiver, manda para as repetidas."""
        ja_possui = self.album_principal.buscar(figurinha.id)
        
        if ja_possui is not None:
            print(f"Ops! A figurinha [{figurinha.id}] {figurinha.nome} é repetida.")
            self.repetidas.adicionar(figurinha) # Vai para a lista de repetidas
        else:
            print(f"Inédita! Colando [{figurinha.id}] {figurinha.nome} no álbum oficial.")
            self.album_principal.adicionar(figurinha)

    def exibir_status_repetidas(self):
        """Mostra a lista de repetidas e conta a quantidade."""
        print(f"\n--- Suas Repetidas (Quantidade: {self.repetidas._tamanho}) ---")
        self.repetidas.exibir_album()

    def buscar_por_jogador(self, nome_jogador: str):
        """Percorre a lista encadeada buscando por nome do jogador."""
        print(f"\nBuscando jogador: '{nome_jogador}'...")
        atual = self.album_principal._cabeca
        encontrou = False
        
        # Viaja nó por nó verificando o nome
        while atual is not None:
            if atual.figurinha.nome.lower() == nome_jogador.lower():
                print(atual.figurinha)
                encontrou = True
            atual = atual.proximo
            
        if not encontrou:
            print("Jogador não encontrado no álbum principal.")

    def buscar_por_selecao(self, pais: str):
        """Percorre a lista encadeada buscando por seleção."""
        print(f"\nBuscando seleção: '{pais}'...")
        atual = self.album_principal._cabeca
        encontrou = False
        
        # Viaja nó por nó verificando o país
        while atual is not None:
            if atual.figurinha.pais.lower() == pais.lower():
                print(atual.figurinha)
                encontrou = True
            atual = atual.proximo
            
        if not encontrou:
            print("Nenhuma figurinha dessa seleção foi encontrada.")
