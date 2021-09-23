# Define classe Pessoa
class Pessoa():
    # Inicia método construtor, cria variável nome iniciando com False para o dado não ser obrigatório
    def __init__(self, cpf, nome=False): 
        # Armanena o valor de nome em um objeto local da classe
        self.nome = nome    
        self.cpf = cpf