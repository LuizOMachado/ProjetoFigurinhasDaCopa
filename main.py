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

def main():
    # Instanciando o sistema
    minha_colecao = Colecao()
    amigo_colecao = Colecao() # Criamos um "usuário 2" fantasma para podermos testar as trocas
    hist_trocas = Historico()
    
    # Carregando dados salvos do CSV (se existirem)
    print("Carregando seus dados da nuvem...")
    Persistencia.carregar_csv(minha_colecao, "meu_album.csv")
    Persistencia.carregar_csv(amigo_colecao, "amigo_album.csv") # O amigo também tem um save
    
    # Loop infinito do menu interativo
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try:
                print("\n--- NOVA FIGURINHA ---")
                id_fig = int(input("Número (ID): "))
                nome = input("Nome do Jogador: ")
                pais = input("Seleção (País): ")
                posicao = input("Posição: ")
                raridade = input("Raridade (Comum, Extra, Lenda): ")
                
                nova_fig = Figurinha(id_fig, nome, pais, posicao, raridade)
                minha_colecao.receber_pacotinho(nova_fig)
            except ValueError:
                print("Erro: O ID deve ser um número inteiro!")
                
        elif opcao == '2':
            print("\n--- MEU ÁLBUM OFICIAL ---")
            minha_colecao.album_principal.exibir_album()
            print(f"Total coladas: {minha_colecao.album_principal._tamanho}")
            
        elif opcao == '3':
            minha_colecao.exibir_status_repetidas()
            
        elif opcao == '4':
            tipo = input("Buscar por (1) Jogador ou (2) Seleção? ")
            if tipo == '1':
                nome = input("Digite o nome do jogador: ")
                minha_colecao.buscar_por_jogador(nome)
            elif tipo == '2':
                pais = input("Digite o nome da seleção: ")
                minha_colecao.buscar_por_selecao(pais)
            else:
                print("Opção inválida.")
                
        elif opcao == '5':
            print("\n--- SISTEMA DE TROCAS ---")
            try:
                meu_id = int(input("ID da SUA figurinha repetida que deseja dar: "))
                amigo_id = int(input("ID da figurinha repetida do AMIGO que você quer: "))
                
                # Para testar isso, você precisa primeiro adicionar a figurinha no amigo_colecao no código ou no CSV
                hist_trocas.processar_troca(minha_colecao, meu_id, amigo_colecao, amigo_id)
            except ValueError:
                print("Erro: Digite apenas números para os IDs.")
                
        elif opcao == '6':
            hist_trocas.exibir_historico()
            
        elif opcao == '7':
            print("\nSalvando o seu progresso...")
            Persistencia.salvar_csv(minha_colecao, "meu_album.csv")
            Persistencia.salvar_csv(amigo_colecao, "amigo_album.csv")
            print("Arquivos CSV atualizados. Até a próxima!")
            break # Quebra o loop e encerra o programa
            
        else:
            print("Opção inválida. Digite um número de 1 a 7.")

# Ponto de entrada padrão do Python
if __name__ == "__main__":
    main()
