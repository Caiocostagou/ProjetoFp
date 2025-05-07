import os
def create():
    pass
def read():
    pass
def update():
    pass
def delete():
    pass
def CRUD(acao):
    while acao != "C" or acao != "C" or acao != "C" or acao != "C":
        acao = input("adicionar um treino (C)\nVisualizar seus treinos atuais (R)\nEditar seus treinos atuais (U)\nExcluir algum de seus treinos(D)\n").upper()
        if acao == "C":
            return create()
        elif acao == "R":
            return read()
        elif acao == "U":
            return update()
        elif acao == "D":
            return delete()
        else:
            print("\nAcao invalida tente novamente\n")
exercises = {}

acao = ""

name = ("Thiago")

tiposetreinos = {"AMRAP": "", "EMOM": "", "For Time": ""}

try:
    app = open ("hora.txt", "x")
    app.close()
    print(f"Ola {name}, esse eh o seu mais novo WOD Tracker\nQual sera sua proxima acao?")
    CRUD(acao)
        
except:
    print(f"Ola {name}, bem vindo de volta...")
    os.remove("hora.txt")
