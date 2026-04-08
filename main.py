
def ler_arquivo(nome):
    try:
        with open(nome, "r") as arq:
            return [linha.strip() for linha in arq]
    except FileNotFoundError:
        return []

def escrever_arquivo(nome, dados):
    with open(nome, "w") as arq:
        for linha in dados:
            arq.write(linha + "\n")

def adicionar_linha(nome, linha):
    with open(nome, "a") as arq:
        arq.write(linha + "\n")

def criar_aluno():
    nome = input("Nome: ")
    idade = input("Idade: ")
    adicionar_linha("alunos.txt", f"{nome},{idade}")


def listar_alunos():
    alunos = ler_arquivo("alunos.txt")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n=== ALUNOS ===")
    for i, linha in enumerate(alunos):
        nome, idade = linha.split(",")
        print(f"{i} - {nome} | {idade}")


def atualizar_aluno():
    alunos = ler_arquivo("alunos.txt")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n=== LISTA DE ALUNOS ===")
    for i, linha in enumerate(alunos):
        nome, idade = linha.split(",")
        print(f"{i} - {nome} | {idade}")

    try:
        escolha = int(input("Escolha o número do aluno: "))
        if escolha < 0 or escolha >= len(alunos):
            print("Escolha inválida!")
            return
    except:
        print("Entrada inválida!")
        return

    nome, idade = alunos[escolha].split(",")

    novo_nome = input(f"Novo nome ({nome}): ") or nome
    nova_idade = input(f"Nova idade ({idade}): ") or idade

    alunos[escolha] = f"{novo_nome},{nova_idade}"

    escrever_arquivo("alunos.txt", alunos)
    print("Aluno atualizado!")


def deletar_aluno():
    alunos = ler_arquivo("alunos.txt")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n=== LISTA DE ALUNOS ===")
    for i, linha in enumerate(alunos):
        nome, idade = linha.split(",")
        print(f"{i} - {nome} | {idade}")

    try:
        escolha = int(input("Escolha o número para deletar: "))
        if escolha < 0 or escolha >= len(alunos):
            print("Inválido!")
            return
    except:
        print("Erro!")
        return

    alunos.pop(escolha)
    escrever_arquivo("alunos.txt", alunos)
    print("Aluno removido!")



def criar_turma():
    nome = input("Nome da turma: ")
    adicionar_linha("turmas.txt", nome)


def listar_turmas():
    turmas = ler_arquivo("turmas.txt")

    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("\n=== TURMAS ===")
    for i, linha in enumerate(turmas):
        print(f"{i} - {linha}")


def atualizar_turma():
    turmas = ler_arquivo("turmas.txt")

    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("\n=== LISTA DE TURMAS ===")
    for i, linha in enumerate(turmas):
        print(f"{i} - {linha}")

    try:
        escolha = int(input("Escolha a turma: "))
        if escolha < 0 or escolha >= len(turmas):
            print("Inválido!")
            return
    except:
        print("Erro!")
        return

    nome = turmas[escolha]
    novo_nome = input(f"Novo nome ({nome}): ") or nome

    turmas[escolha] = novo_nome

    escrever_arquivo("turmas.txt", turmas)
    print("Turma atualizada!")


def deletar_turma():
    turmas = ler_arquivo("turmas.txt")

    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("\n=== TURMAS ===")
    for i, linha in enumerate(turmas):
        print(f"{i} - {linha}")

    try:
        escolha = int(input("Escolha a turma para deletar: "))
        if escolha < 0 or escolha >= len(turmas):
            print("Inválido!")
            return
    except:
        print("Erro!")
        return

    turmas.pop(escolha)
    escrever_arquivo("turmas.txt", turmas)
    print("Turma removida!")


def criar_disciplina():
    nome = input("Nome da disciplina: ")
    adicionar_linha("disciplinas.txt", nome)


def listar_disciplinas():
    disciplinas = ler_arquivo("disciplinas.txt")

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("\n=== DISCIPLINAS ===")
    for i, linha in enumerate(disciplinas):
        print(f"{i} - {linha}")


def atualizar_disciplina():
    disciplinas = ler_arquivo("disciplinas.txt")

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("\n=== LISTA DE DISCIPLINAS ===")
    for i, linha in enumerate(disciplinas):
        print(f"{i} - {linha}")

    try:
        escolha = int(input("Escolha a disciplina: "))
        if escolha < 0 or escolha >= len(disciplinas):
            print("Inválido!")
            return
    except:
        print("Erro!")
        return

    nome = disciplinas[escolha]
    novo_nome = input(f"Novo nome ({nome}): ") or nome

    disciplinas[escolha] = novo_nome

    escrever_arquivo("disciplinas.txt", disciplinas)
    print("Disciplina atualizada!")


def deletar_disciplina():
    disciplinas = ler_arquivo("disciplinas.txt")

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("\n=== DISCIPLINAS ===")
    for i, linha in enumerate(disciplinas):
        print(f"{i} - {linha}")

    try:
        escolha = int(input("Escolha a disciplina para deletar: "))
        if escolha < 0 or escolha >= len(disciplinas):
            print("Inválido!")
            return
    except:
        print("Erro!")
        return

    disciplinas.pop(escolha)
    escrever_arquivo("disciplinas.txt", disciplinas)
    print("Disciplina removida!")


def menu():
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Criar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Deletar aluno")
        print("5 - Criar turma")
        print("6 - Listar turmas")
        print("7 - Atualizar turma")
        print("8 - Deletar turma")
        print("9 - Criar disciplina")
        print("10 - Listar disciplinas")
        print("11 - Atualizar disciplina")
        print("12 - Deletar disciplina")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1": criar_aluno()
        elif op == "2": listar_alunos()
        elif op == "3": atualizar_aluno()
        elif op == "4": deletar_aluno()
        elif op == "5": criar_turma()
        elif op == "6": listar_turmas()
        elif op == "7": atualizar_turma()
        elif op == "8": deletar_turma()
        elif op == "9": criar_disciplina()
        elif op == "10": listar_disciplinas()
        elif op == "11": atualizar_disciplina()
        elif op == "12": deletar_disciplina()
        elif op == "0": break
        else: print("Opção inválida!")


menu()