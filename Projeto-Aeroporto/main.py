from conexao import ConexaoMySQL
from Pessoa import Pessoa
from Passagem import Passagem
from Piloto import Piloto


conexao = ConexaoMySQL(host="localhost",usuario="root",senha="etec",banco="bancoempresaaerea")
conexao.conectar()

piloto = Piloto("vinicius","18999",192,12332,1921.2)

# piloto.getNome()
# piloto.getTelefone()
# piloto.getDocumento()
# piloto.getRegistro()
# piloto.getSalario()

# piloto.setNome("Vinicius")

# piloto.getNome()

# piloto.insert(conexao)

piloto.select(conexao)