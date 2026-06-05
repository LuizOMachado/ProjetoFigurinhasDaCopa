import os 
from modelos import Figurinha
from estruturas import Album

class Colecao:
    """Gerencia o álbum principal e o bolo de figurinhas repetidas do usuário."""
    
    def __init__(self):
        self.album_principal = Album() 
        self.repetidas = Album()       

    def receber_pacotinho(self, figurinha: Figurinha):
        ja_possui = self.album_principal.buscar(figurinha.id)
        if ja_possui is not None:
            print(f"Ops! A figurinha [{figurinha.id}] {figurinha.nome} é repetida.")
            self.repetidas.adicionar(figurinha) 
        else:
            print(f"Inédita! Colando [{figurinha.id}] {figurinha.nome} no álbum oficial.")
            self.album_principal.adicionar(figurinha)

    def exibir_status_repetidas(self):
        print(f"\n--- Suas Repetidas (Quantidade: {self.repetidas._tamanho}) ---")
        self.repetidas.exibir_album()

    def buscar_por_jogador(self, nome_jogador: str):
        print(f"\nBuscando jogador: '{nome_jogador}'...")
        atual = self.album_principal._cabeca
        encontrou = False
        while atual is not None:
            if atual.figurinha.nome.lower() == nome_jogador.lower():
                print(atual.figurinha)
                encontrou = True
            atual = atual.proximo
        if not encontrou:
            print("Jogador não encontrado no álbum principal.")

    def buscar_por_selecao(self, pais: str):
        print(f"\nBuscando seleção: '{pais}'...")
        atual = self.album_principal._cabeca
        encontrou = False
        while atual is not None:
            if atual.figurinha.pais.lower() == pais.lower():
                print(atual.figurinha)
                encontrou = True
            atual = atual.proximo
        if not encontrou:
            print("Nenhuma figurinha dessa seleção foi encontrada.")

# CLASSE DE PERSISTÊNCIA

class Persistencia:
    """Responsável por salvar e carregar os dados da coleção em formato CSV."""
    
    @staticmethod
    def salvar_csv(colecao: Colecao, nome_arquivo: str = "dados_copa.csv"):
        """Salva o álbum principal e as repetidas em um arquivo CSV."""
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write("id,nome,pais,posicao,raridade,tipo\n")
                
                # Salva Álbum Principal
                atual = colecao.album_principal._cabeca
                while atual is not None:
                    fig = atual.figurinha
                    arquivo.write(f"{fig.id},{fig.nome},{fig.pais},{fig.posicao},{fig.raridade},oficial\n")
                    atual = atual.proximo
                    
                # Salva Repetidas
                atual = colecao.repetidas._cabeca
                while atual is not None:
                    fig = atual.figurinha
                    arquivo.write(f"{fig.id},{fig.nome},{fig.pais},{fig.posicao},{fig.raridade},repetida\n")
                    atual = atual.proximo
                    
            print(f"Sucesso! Dados salvos com segurança em '{nome_arquivo}'.")
        except Exception as e:
            print(f"Erro ao tentar salvar o arquivo: {e}")

    @staticmethod
    def carregar_csv(colecao: Colecao, nome_arquivo: str = "dados_copa.csv"):
        """Lê o arquivo CSV e reconstrói as listas encadeadas (álbum e repetidas)."""
        if not os.path.exists(nome_arquivo):
            print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando um álbum vazio.")
            return

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            for linha in linhas[1:]:
                linha = linha.strip()
                if not linha:
                    continue 
                    
                dados = linha.split(',')
                
                # Tratamento de entradas inválidas
                try:
                    id_fig = int(dados[0])
                    if id_fig < 0:
                        raise ValueError("O ID da figurinha não pode ser negativo.")
                        
                    fig = Figurinha(id_fig, dados[1], dados[2], dados[3], dados[4])
                    
                    if dados[5] == "oficial":
                        colecao.album_principal.adicionar(fig)
                    elif dados[5] == "repetida":
                        colecao.repetidas.adicionar(fig)
                        
                except ValueError as e:
                    print(f"Entrada inválida ignorada na linha '{linha}': {e}")
                except IndexError:
                    print(f"Entrada inválida ignorada (faltando dados): '{linha}'")
                    
        print(f"Dados carregados com sucesso! O álbum está pronto para uso.")
