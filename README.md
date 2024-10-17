# Sistema de Cadastro de Passagens Aéreas

Este projeto é uma aplicação em Python que permite o cadastro e gerenciamento de passagens aéreas, pilotos e passageiros. Utiliza um banco de dados MySQL para armazenar informações e realizar operações de inserção e seleção.

## Funcionalidades

- Cadastrar passageiros e pilotos com informações pessoais.
- Cadastrar passagens com origem, destino, valor e horário.
- Conexão com um banco de dados MySQL para armazenamento persistente de dados.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

/src ├── Passagem.py # Classe que representa uma passagem aérea ├── Pessoa.py # Classe base para pessoas (passageiros e pilotos) ├── Piloto.py # Classe que herda de Pessoa e representa um piloto ├── Comum.py # Classe que representa uma passagem comum ├── Executiva.py # Classe que representa uma passagem executiva ├── ConexaoMySQL.py # Classe para gerenciar a conexão com o banco de dados MySQL └── main.py # Ponto de entrada do programa


## Requisitos

- Python 3.x
- Biblioteca `mysql-connector-python`

## Instalação

1. **Clone o repositório** (se aplicável):
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
2. **Instale as dependências:
   pip install mysql-connector-python
3. **Configurar o Banco de Dados:

  1.Certifique-se de que o MySQL está instalado e em execução.
  2.Crie um banco de dados chamado bancoempresaaerea.
  3.Crie as tabelas necessárias (Pessoa, Piloto, etc.) conforme sua estrutura.

## Como usar 
1. Execute o programa :
   python main.py
2. Siga as instruções na tela para cadastrar pilotos, passageiros e passagens.

## Exemplo de uso 
piloto = Piloto("Vinicius", "18999", "123456789", "12345", 1921.2)
piloto.insert(conexao)  # Insere o piloto no banco de dados
piloto.select(conexao)  # Lista todos os pilotos cadastrados



