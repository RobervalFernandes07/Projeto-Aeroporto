import mysql.connector


class Pessoa:

    def __init__(self, nome, telefone, documento, registro):
        self.nome = nome
        self.telefone = telefone
        self.documento = documento
        self.registro = registro

    def getNome(self):
        print(self.nome)

    def setNome(self,nome):
        self.nome = nome
        
    def getTelefone(self):
        print(self.telefone)

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getDocumento(self):
        print(self.documento)

    def setDocumento(self,documento):
        self.documento = documento

    def getRegistro(self):
        print(self.registro)
    
    def setRegistro(self,registro):
        self.registro = registro

    def insert(self, conexao):
        cursor = conexao.conexao.cursor()
        query = "INSERT INTO Pessoa (nome, telefone, documento, registro ) VALUES (%s, %s, %s, %s)"
        dados = (self.nome, self.telefone, self.documento, self.registro)
        try:
            cursor.execute(query, dados)
            conexao.conexao.commit()
            print("Inserido com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao inserir: {e}")
        finally:
            cursor.close()

    def select(self, conexao):
        cursor = conexao.conexao.cursor()
        query = "SELECT * FROM Pessoa"
        try:
            cursor.execute(query)
            
            clientes = cursor.fetchall()
            for cliente in clientes:
                print(cliente)
                
        except mysql.connector.Error as e:
            print(f"Erro ao selecionar: {e}")
        finally:
            cursor.close()
        