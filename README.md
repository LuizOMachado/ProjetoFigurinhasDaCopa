# ProjetoFigurinhasDaCopa

# Sistema de Álbum de Figurinhas - Copa 2026

Projeto desenvolvido para a disciplina de Estrutura de Dados da Fatec de Rio Claro-SP. Este sistema permite que usuários colecionem, troquem e organizem figurinhas de jogadores e seleções da Copa do Mundo de 2026. 

O grande diferencial técnico deste projeto é a construção e manipulação de gerenciamento de memória do zero, através do uso de Listas Encadeadas e Filas FIFO criadas manualmente com base em nós, obedecendo ao requisito estrito de não utilizar estruturas prontas da linguagem Python (como `list` ou `deque`).

## Funcionalidades Principais

* **Gerenciamento do Álbum:** Inserção, remoção e visualização de figurinhas do álbum oficial.
* **Controle de Repetidas:** Separação automática, armazenamento e contagem de figurinhas repetidas.
* **Buscas Específicas:** Pesquisa de figurinhas por número (ID), por nome do jogador e por seleção.
* **Sistema de Trocas (FIFO):** Registro de propostas de trocas entre usuários. O sistema verifica automaticamente as regras de negócio (se os usuários possuem as repetidas e se já não as têm no álbum oficial) antes de efetuar a troca e registrar a transação em uma Fila separada.
* **Persistência de Dados:** Salvamento e carregamento automático das coleções utilizando arquivos no formato CSV.

## Estrutura do Projeto

A arquitetura do código foi separada em classes e arquivos distintos para manter a organização e a responsabilidade única:

* `modelos.py`: Contém a entidade de negócio (Figurinha) e os nós base (NodoLista e NodoFila).
* `estruturas.py`: Implementação da lógica de ponteiros para a Lista Encadeada (Album) e para a Fila FIFO (Fila).
* `colecao.py`: Gerencia a Coleção do usuário (Álbum principal e Repetidas) e a Persistência de Dados (salvar/carregar CSV).
* `historico.py`: Contém a classe de Histórico, responsável por gerenciar e validar as trocas utilizando a fila FIFO.
* `main.py`: Ponto de entrada do programa, contendo o menu interativo para uso no terminal.



## Como executar o projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Abra o seu terminal na pasta raiz do projeto.
4. Execute o arquivo principal com o comando:

    python main.py
