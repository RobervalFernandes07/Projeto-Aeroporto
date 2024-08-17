class Passagem:

    def __init__(self, origem, destino, valor, horario):
        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.horario = horario
    
    def getOrigem(self):
        print(self.origem)

    def setorigem(self,origem):
        self.origem = origem

    def getDestino(self):
        print(self.destino)

    def setDesitno(self,destino):
        self.destino = destino
    def getValor(self):
        print(self.valor)
    
    def setValor(self, valor):
        self.valor = valor

    def getHorario(self):
        print(self.horario)

    def setHorario(self, horario):
        self.horario = horario

    
        