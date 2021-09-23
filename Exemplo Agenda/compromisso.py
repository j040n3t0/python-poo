class Compromisso(object):
    def __init__(self, entrevistador) -> None:
       self.entrevistador = entrevistador

    def compromissoNome(self, compromisso_nome=None, data_compromisso=None):
        self.compromisso_nome = compromisso_nome
        self.data = data_compromisso
        self.message = " - " + self.compromisso_nome + " - " + self.data
        self.entrevistador.compromisso_lista.append(self.message)
