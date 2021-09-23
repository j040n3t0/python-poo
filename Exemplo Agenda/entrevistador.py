from compromisso import Compromisso

class Entrevistador():
    def __init__(self) -> None:
        self.compromisso_lista = list()
        self.compromisso = Compromisso(self)

    def setNome(self, nome):
        self.nome = nome

    def setCompromisso(self, compromisso_nome, compromisso_data):
        self.compromisso.compromissoNome(compromisso_nome,compromisso_data)

    def getCompromissos(self):
        for item in self.compromisso_lista:
            print(self.nome, item)
