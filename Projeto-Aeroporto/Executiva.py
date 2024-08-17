class Executiva:

    def __init__(self,nome,telefone,documento,registro,janta):
        super().__init__(nome,telefone,documento,registro)
        self.janta = janta

    def getJanta(self):
        print(self.janta)

    def setJanta(self, janta):
        self.janta = janta
    