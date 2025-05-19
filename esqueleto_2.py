

import random

def linhadata(line):
    partesdata = line.split('/')
    if len(partesdata) != 3:
        return False
    day, month, year = partesdata 
    return (
        day.isdigit() and len(day) == 2 and  
        month.isdigit() and len(month) == 2 and 
        year.isdigit() and len(year) == 4   
    )


def linhaatelinha(tipo, datatreino):
    printdata = []
    state = False 

    with open(f"{tipo}.txt", 'r') as app:
        for line in app:
            line = line.strip()

            if linhadata(line):
                if line == datatreino:
                    state = True 
                    continue 
                elif state:
                    break  

            elif state: 
                printdata.append(line)

    return printdata 
def check(tipo):
    state = 0
    with open(f"{tipo}.txt", "r") as app:   
        perg = input("voce deseja vizualizar treinos de uma data especifica? S/N\n").upper()
        if perg == "S":
            datatreino = input("Qual data o treino que voce deseja visualizar aconteceu?\n")
            for line in app:
                if datatreino in line:
                    state = 1
                    return state, datatreino
        elif perg == "N":
            state = 2
            return state, "0"
        else:
            print("Resposta invalida")
            return state, "0"

def create(tiposetreinos, exercises):
    tipo = input("Qual tipo de treino voce deseja adicionar: AMRAP(AM), EMOM(EM), For Time(FT)?\n").upper()
    
    if tipo == "AM":
        nometreino = input("Qual o nome do treino?\n")
        tempo = int(input(f"Qual a duracao, em minutos, do treino de {nometreino}:\n"))
        tiposetreinos.setdefault("AMRAP", []).append(nometreino)
        exercises[nometreino] = tempo
        with open("AM.txt", "a") as app:
            app.write(f"{nometreino}:{tempo} minutos\n")
        return CRUD(acao)
            
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
            app.write(nometreino + "(" + str(qnt) + "):" + str(tempo) + "minutos\n")
            for ex, rep in treinoem.items():
                app.write(f"        {ex}:{rep} reps\n")
        return CRUD(acao)
            

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
            app.write(nometreino + "(" + str(qnt) + ")\n")
            for ex, rep in treinoft.items():
                app.write(f"        {ex}:{rep} reps\n")
        return CRUD(acao)
    else:
        print("Tipo inválido.")

def read():
    tipo = input("Qual tipo de treino voce deseja visualizar?\n").upper()
    try:
        state, datatreino = check(tipo)
        if tipo in ["AM", "EM", "FT"]:
            if state == 2:
                with open(f"{tipo}.txt", "r") as app:
                    print(app.read())
            elif state == 0:
                print("data nao encontrada")

            else:
                with open(f"{tipo}.txt", "r") as app:
                    printdata = linhaatelinha(tipo, datatreino)
                    for i in printdata:
                        print(i)
                    print()
        else:
            print("tipo de treino nao reconhecido.")
        return CRUD(acao)
    except FileNotFoundError:
        print("voce ainda nao tem treinos criados")
        return CRUD(acao)
def update():
    pass
def delete():
    pass

def CRUD(acao):
    while acao not in ["C", "R", "U", "D","S","E"]:
        acao = input("Adicionar um treino (C)\nVisualizar seus treinos atuais (R)\nEditar seus treinos atuais (U)\nExcluir algum de seus treinos (D)\nReceber sugestão de WOD aleatório (S)\nSair (E)\n").upper()
    if acao == "C":
        return create(tiposetreinos, exercises)
    elif acao == "R":
        return read()
    elif acao == "U":
        return update()
    elif acao == "D":
        return delete()
    elif acao=="S":
        return sugerir_wod()
    elif acao == "E":
        pass
    else:
        print("\nAcao invalida tente novamente\n")

def sugerir_wod():
    sugestoes = []

    
    try:
        with open("AM.txt", "r") as file:
            linhas = file.readlines()
            treinos_amrap = []
            for linha in linhas:
                if ":" in linha:
                    treino = linha.strip()
                    treinos_amrap.append(treino)
            if treinos_amrap:
                sugestao = random.choice(treinos_amrap)
                sugestoes.append(("AMRAP", sugestao))
    except FileNotFoundError:
        pass

    
    try:
        with open("EM.txt", "r") as file:
            linhas = file.readlines()
            treinos_emom = []
            for linha in linhas:
                if ":" in linha and not linha.strip().startswith("EMOM"):
                    treino = linha.strip()
                    treinos_emom.append(treino)
            if treinos_emom:
                sugestao = random.choice(treinos_emom)
                sugestoes.append(("EMOM", sugestao))
    except FileNotFoundError:
        pass

   
    try:
        with open("FT.txt", "r") as file:
            linhas = file.readlines()
            treinos_ft = []
            for linha in linhas:
                if ":" in linha and not linha.strip().startswith("For Time"):
                    treino = linha.strip()
                    treinos_ft.append(treino)
            if treinos_ft:
                sugestao = random.choice(treinos_ft)
                sugestoes.append(("For Time", sugestao))
    except FileNotFoundError:
        pass

    if sugestoes:
        print("\nSugestões de WODs Aleatórios:")
        for tipo, sugestao in sugestoes:
            print(f"- {tipo}: {sugestao}")
    else:
        print("Nenhum treino encontrado para sugerir. Crie alguns treinos primeiro!")

exercises = {}
tiposetreinos = {}
acao = ""
name = "Thiago"

try:
    data = input("Qual a data de hoje?(formato dd/mm/aaaa)\n")
    while True:
        if not linhadata(data):
            print("Data invalida tente novamente\n")
            data = input("Qual a data de hoje?(formato dd/mm/aaaa)\n")
        else:
            break


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

    print(f"Ola {name}, esse eh o seu mais novo WOD Tracker.\nQual sera sua proxima acao?")
    CRUD(acao)
except FileExistsError:
    print(f"Ola {name}, bem-vindo de volta...")
    with open("AM.txt", "a") as app:
        app.write(f"{data} \n")
    with open("EM.txt", "a") as app:
        app.write(f"{data} \n")
    with open("FT.txt", "a") as app:
        app.write(f"{data} \n")
    CRUD(acao)
