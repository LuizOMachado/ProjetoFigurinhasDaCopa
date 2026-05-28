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

     def buscar(self, id_figurinha: int) -> Figurinha:
        """Busca uma figurinha pelo ID. Retorna a Figurinha ou None se não achar"""
        atual = self._cabeca
        
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                return atual.figurinha
            # Pula para o próximo nó
            atual = atual.proximo
            
        return None
    def remover(self, id_figurinha: int) -> bool:
        """Remove uma figurinha pelo ID manipulando os ponteiros"""
        atual = self._cabeca
        anterior = None
        
        while atual is not None:
            if atual.figurinha.id == id_figurinha:
                # Caso 1: A figurinha a ser removida é a primeira da lista (cabeça)
                if anterior is None:
                    self._cabeca = atual.proximo
                # Caso 2: A figurinha está no meio ou no final da lista
                else:
                    # A "seta" do nó anterior pula o nó atual e aponta para o próximo
                    anterior.proximo = atual.proximo
                    
                self._tamanho -= 1
                return True # Retorna True indicando que foi removido com sucesso
                
            # Se não achou ainda, avança os dois ponteiros
            anterior = atual
            atual = atual.proximo
            
        return False # Retorna False se percorreu tudo e não achou a figurinha

   def exibir_album(self):
        """Método extra para imprimir o álbum completo no terminal"""
        atual = self._cabeca
        if atual is None:
            print("O álbum está vazio.")
            return
            
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo


