"""
Um sistema com duas classes
Entrevistador e compromisso
Aí pode ser só um módulo mesmo
Onde depois de criar o entrevistador, você vai adicionando os compromissos
O compromisso tem data e hora de início e tempo de duração em minutos
Não pode haver compromissos que conflitar entre si
Gera uma exception neste caso
Cobre de teste com pytest
Não precisa de banco
São 2 modulos: models, test
"""

# Importa a classe Pessoa do arquivo pessoa.py
from entrevistador import Entrevistador
import json, datetime, os

def criarEntrevistador(nome):
    entrevistador_object = Entrevistador()
    entrevistador_object.setNome(nome)
    return entrevistador_object
    
def criarCompromisso(entrevistador_object, compromisso,data):
    entrevistador_object.setCompromisso(compromisso,data)

def imprimirCompromissos(entrevistador_object):
    entrevistador_object.getCompromissos()

################# DEBUG
os.system("clear")

print("\n--------------\n")

pessoa = criarEntrevistador("João Neto")
criarCompromisso(pessoa, "Lavar casa",str(datetime.datetime.now()))
imprimirCompromissos(pessoa)

print("\n--------------\n")

pessoa = criarEntrevistador("Sarah B")
criarCompromisso(pessoa, "Lavar roupa",str(datetime.datetime.now()))
criarCompromisso(pessoa, "Lavar louças",str(datetime.datetime.now()))
criarCompromisso(pessoa, "Cuidar do Arthur",str(datetime.datetime.now()))

imprimirCompromissos(pessoa)

print("\n--------------\n") 


"""
objs = list()

while True:
    option = input("\n\n[1] Novo entrevistador\n[2] Add compromisso\n[3] Listar Entrevistador\n[4] Listar Compromissos\n[0] Sair\n>>>>>> ")

    if int(option) == 1:
        nome = input("\n\nNome do entrevistador: ")
        objs.append(criarEntrevistador(nome))

    if int(option) == 2:
        nome = input("\n\nNome do entrevistador: ")
        for entrevistador in objs:
            if entrevistador.nome == nome:
                criarCompromisso(entrevistador, "Lavar casa",str(datetime.datetime.now()))

    if int(option) == 3:
        if len(objs) == 0:
            print("\n\nNenhum entrevistador cadastrado!")
        else:
            print("\n\n### Lista Entrevistadores ###")
            for entrevistador in objs:
                print(entrevistador.nome)
            print("### Fim da Lista ###")

    if int(option) == 4:
        nome = input("\n\nNome do entrevistador: ")
        for entrevistador in objs:
            if entrevistador.nome == nome:
                imprimirCompromissos(entrevistador)
        

    if int(option) == 0:
        break
"""