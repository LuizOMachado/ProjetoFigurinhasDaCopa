from modelos import NodoLista, Figurinha

class Album:
    """Implementação do Álbum usando Lista Encadeada Simples."""
    
    def __init__(self):
        self._cabeca = None  
        self._tamanho = 0
        
def adicionar(self, figurinha: Figurinha):
        """Adiciona uma nova figurinha ao final do álbum"""
        novo_nodo = NodoLista(figurinha)
        
        # Se o álbum estiver vazio, a nova figurinha vira a cabeça
        if self._cabeca is None:
            self._cabeca = novo_nodo
        else:
            # Percorre a lista até achar o último nó (cujo 'proximo' é None)
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            # Faz o último nó apontar para o novo nó criado
            atual.proximo = novo_nodo
            
        self._tamanho += 1


