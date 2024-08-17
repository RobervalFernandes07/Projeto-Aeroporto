from Pessoa import Pessoa

class Piloto(Pessoa):

    def __init__(self,nome,telefone,documento,registro,salario):
        super().__init__(nome,telefone,documento,registro)
        self.salario = salario

    def getSalario(self):
        print(self.salario)

    def setSalario(self, salario):
        self.salario = salario
    
    def insert(self, conexao):
        cursor = conexao.conexao.cursor()
        query = "INSERT INTO piloto (nome, telefone, documento, registro, salario) VALUES (%s, %s, %s, %s, %s)"
        dados = (self.nome, self.telefone, self.documento, self.registro, self.salario)
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
        query = "SELECT * FROM Piloto"
        try:
            cursor.execute(query)
            
            clientes = cursor.fetchall()
            for cliente in clientes:
                print(cliente)
                
        except mysql.connector.Error as e:
            print(f"Erro ao selecionar: {e}")
        finally:
            cursor.close()