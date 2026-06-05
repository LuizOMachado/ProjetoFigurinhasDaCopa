from modelos import Figurinha
from colecao import Colecao, Persistencia
from historico import Historico

def exibir_menu():
    print("\n" + "="*40)
    print(" ÁLBUM DA COPA DO MUNDO 2026 ")
    print("="*40)
    print("1. Abrir pacotinho (Adicionar Figurinha)")
    print("2. Ver Álbum Oficial")
    print("3. Ver Figurinhas Repetidas")
    print("4. Buscar Figurinha (Por Jogador ou Seleção)")
    print("5. Realizar Troca com um Amigo")
    print("6. Ver Histórico de Trocas (Fila FIFO)")
    print("7. Salvar e Sair")
    print("="*40)
