import os
def create(tiposetreinos, exercises):
    tipo = input("Qual tipo de treino voce deseja adicionar: AMRAP(AM), EMOM(EM), For Time(FT)?\n").upper()
    
    if tipo == "AM":
        nometreino = input("Qual o nome do treino?\n")
        tempo = int(input(f"Qual a duracao, em minutos, do treino de {nometreino}:\n"))
        tiposetreinos["AMRAP"].append(nometreino)
        exercises[nometreino] = tempo
        with open("hora.txt", "w") as app:
            return app.write(f"{nometreino}: {tempo}")
        



def read():
    pass
def update():
    pass
def delete():
    pass
def CRUD(acao):
    while acao != "C" and acao != "R" and acao != "U" and acao != "D":
        acao = input("adicionar um treino (C)\nVisualizar seus treinos atuais (R)\nEditar seus treinos atuais (U)\nExcluir algum de seus treinos(D)\n").upper()
    if acao == "C":
        return create(tiposetreinos,exercises)
    elif acao == "R":
        return read()
    elif acao == "U":
        return update()
    elif acao == "D":
        return delete()
    else:
            print("\nAcao invalida tente novamente\n")
exercises = {}

tipo = ""

nometreino = ""

acao = ""

name = ("Thiago")

tiposetreinos = {}

try:
    app = open ("hora.txt", "x")
    app.close()
    print(f"Ola {name}, esse eh o seu mais novo WOD Tracker\nQual sera sua proxima acao?")
    CRUD(acao)
    
except:
    print(f"Ola {name}, bem vindo de volta...")
    #os.remove("hora.txt")
    
