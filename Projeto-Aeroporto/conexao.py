import mysql.connector

class ConexaoMySQL:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            print("Conexão ao MySQL estabelecida com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão ao MySQL fechada.")