import os  # noqa: F401


def create(tiposetreinos, exercises):
    tipo = input("Qual tipo de treino voce deseja adicionar: AMRAP(AM), EMOM(EM), For Time(FT)?\n").upper()
    
    if tipo == "AM":
        nometreino = input("Qual o nome do treino?\n")
        tempo = int(input(f"Qual a duracao, em minutos, do treino de {nometreino}:\n"))
        tiposetreinos.setdefault("AMRAP", []).append(nometreino)
        exercises[nometreino] = tempo
        with open("AM.txt", "a") as app:
            app.write(f"{nometreino}:{tempo} minutos\n")
            
    elif tipo == "EM":
        nometreino = input("Qual o nome desse conjunto EMOM?\n")
        qnt = int(input(f"Quantos exercicios serao feitos no conjunto {nometreino}?:\n"))
        tiposetreinos.setdefault("EMOM", []).append(nometreino)
        treinoem = {}
        for i in range(qnt):
            nome = input(f"Qual o nome do exercicio {i+1}? ")
            reps = input(f"Quantas repeticoes terao o exercicio {i+1}? ")
            treinoem[nome] = reps
        tempo = int(input(f"Qual o tempo total de duracao, em minutos, do conjunto {nometreino}? "))
        exercises[nometreino] = tempo
        with open("EM.txt", "a") as app:
            app.write("\nEMOM (" + str(qnt) + ")\n")
            app.write(f"    {nometreino}: {tempo} minutos\n")
            for ex, rep in treinoem.items():
                app.write(f"        {ex}:{rep} reps\n")
            

    elif tipo == "FT":
        nometreino = input("Qual o nome desse conjunto For Time?\n")
        qnt = int(input(f"Quantos exercicios o conjunto {nometreino} tera?:\n"))
        tiposetreinos.setdefault("For Time", []).append(nometreino)
        treinoft = {}
        for i in range(qnt):
            nome = input(f"Qual o nome do exercicio {i+1}? ")
            reps = input(f"Quantas repeticoes terao o exercicio {i+1}? ")
            treinoft[nome] = reps
        exercises[nometreino] = ""
        with open("FT.txt", "a") as app:
            app.write("For Time(" + str(qnt) + ")\n")
            app.write(f"    {nometreino}\n")
            for ex, rep in treinoft.items():
                app.write(f"        {ex}:{rep} reps\n")
    else:
        print("Tipo inválido.")

def read():
    tipo = input("Qual tipo de treino voce deseja visualizar?\n").upper()
    try:
        if tipo == "AM":
            with open("AM.txt", "r") as app:
                print(app.read())
        elif tipo == "EM":
            with open("EM.txt", "r") as app:
                print(app.read())
        elif tipo == "FT":
            with open("FT.txt", "r") as app:
                print(app.read())
        else:
            print("tipo de treino nao reconhecido.")
    except:
        print("voce ainda nao tem treinos criados")
def update():
    pass
def delete():
    pass

def CRUD(acao):
    while acao not in ["C", "R", "U", "D"]:
        acao = input("Adicionar um treino (C)\nVisualizar seus treinos atuais (R)\nEditar seus treinos atuais (U)\nExcluir algum de seus treinos (D)\n").upper()
    if acao == "C":
        return create(tiposetreinos, exercises)
    elif acao == "R":
        return read()
    elif acao == "U":
        return update()
    elif acao == "D":
        return delete()
    else:
        print("\nAcao invalida tente novamente\n")

exercises = {}
tiposetreinos = {}
acao = ""
name = "Thiago"

try:
    data = input("Qual a data de hoje?(formato dd/mm/aa)\n")
    print(f"Ola {name}, esse eh o seu mais novo WOD Tracker.\nQual sera sua proxima acao?")
    with open("AM.txt", "x") as app:
        pass
    with open("AM.txt", "w") as app:
        app.write("AMRAP \n")
        app.write(f"{data} \n")
    with open("EM.txt", "x") as app:
        pass
    with open("EM.txt", "w") as app:
        app.write("EMOM \n")
        app.write(f"{data} \n")
    with open("FT.txt", "x") as app:
        pass
    with open("FT.txt", "w") as app:
        app.write("ForTime \n")
        app.write(f"{data} \n")

    
    CRUD(acao)
except FileExistsError:
    print(f"Ola {name}, bem-vindo de volta...")
    data = input("Qual a data de hoje?(formato dd/mm/aa)\n")
    with open("AM.txt", "a") as app:
        app.write(f"{data} \n")
    with open("EM.txt", "a") as app:
        app.write(f"{data} \n")
    with open("FT.txt", "a") as app:
        app.write(f"{data} \n")
    CRUD(acao)
