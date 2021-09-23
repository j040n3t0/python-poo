# Importa a classe Pessoa do arquivo pessoa.py
from pessoa import Pessoa

try:
    # Cria instância da classe pessoa
    pessoa1 = Pessoa("123")
    # Seta o valor de nome que contém no classe Pessoa
    pessoa1.nome = "João Neto"
    # Adiciona um campo que não contém na classe (característica do objeto pessoa1)
    pessoa1.idade = 29
except:
    pass

try:
    # Cria instância da classe pessoa
    pessoa2 = Pessoa()
except Exception as e:
    if "required positional argument" in str(e):
        print("Erro ao criar o objeto")
    else:
        print("Outro erro ocorreu!")

# Imprime na tela dos valores dos atributos de cada objeto.
#print(pessoa1.__dict__)
#print(pessoa2.__dict__)
