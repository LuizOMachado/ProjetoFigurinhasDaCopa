from modelos import Figurinha
from estruturas import Fila
from colecao import Colecao

class Historico:
    """Gerencia o registro de trocas utilizando a Fila FIFO."""
    
    def __init__(self):
        # Instância separada de Fila para registrar o histórico de trocas
        self.fila_trocas = Fila() 
        
    def processar_troca(self, u1: Colecao, id_u1: int, u2: Colecao, id_u2: int):
        """Registra a proposta, verifica as regras e efetua a troca automática."""
        print(f"\n--- Processando Proposta de Troca ---")
        print(f"Usuário 1 oferece a figurinha [{id_u1}]")
        print(f"Usuário 2 oferece a figurinha [{id_u2}]")
        
        #  Verifica se ambos possuem as figurinhas repetidas
        fig_u1 = u1.repetidas.buscar(id_u1)
        fig_u2 = u2.repetidas.buscar(id_u2)
        
        if fig_u1 is None or fig_u2 is None:
            print("Troca RECUSADA: Um dos usuários não possui a figurinha oferecida nas repetidas.")
            return
            
        #  Verifica se o U1 já tem a figurinha que o U2 está oferecendo no álbum principal
        if u1.album_principal.buscar(id_u2) is not None:
             print(f"Troca RECUSADA: O Usuário 1 já tem a figurinha [{id_u2}] no álbum oficial.")
             return
             
        # Verifica se o U2 já tem a figurinha que o U1 está oferecendo no álbum principal
        if u2.album_principal.buscar(id_u1) is not None:
             print(f"Troca RECUSADA: O Usuário 2 já tem a figurinha [{id_u1}] no álbum oficial.")
             return

        # EFETUAR A TROCA AUTOMÁTICA
        print(f"Troca APROVADA: Trocando [{fig_u1.nome}] por [{fig_u2.nome}]")
        
        # Remove das repetidas de ambos
        u1.repetidas.remover(id_u1)
        u2.repetidas.remover(id_u2)
        
        # Adiciona no álbum principal do novo dono
        u1.album_principal.adicionar(fig_u2)
        u2.album_principal.adicionar(fig_u1)
        
        # Registrar no histórico (Fila FIFO)
        # Como o NodoFila exige um objeto Figurinha, criamos uma figurinha "adaptada" para servir de registro textual
        resumo_troca = f"Troca Concluida: U1 recebeu [{fig_u2.id}] / U2 recebeu [{fig_u1.id}]"
        registro = Figurinha(0, resumo_troca, "Sistema", "Troca", "Concluída")
        
        self.fila_trocas.enqueue(registro)
        print("Registro salvo no histórico de transações.")
        
    def exibir_historico(self):
        """Mostra as trocas registradas na fila FIFO percorrendo os nós."""
        print("\n--- Histórico de Trocas (FIFO) ---")
        atual = self.fila_trocas._inicio
        if atual is None:
            print("Nenhuma troca registrada ainda.")
            return
            
        while atual is not None:
            print(atual.figurinha.nome) # Imprime o resumo textual que guardamos no campo 'nome'
            atual = atual.proximo
