import time
from datetime import datetime
import os

class Avatar:
    def __init__(self, nome, data_nascimento, email, senha, confirmar_senha):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
        self.senha = senha
        self.confirmar_senha = confirmar_senha

    def validar_login(self, email, senha):
        return self.email == email and self.senha == senha

def imprimir_letra_por_letra(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.1) 

texto_para_imprimir = " * * * * * JOGO NETUNO * * * * * "
imprimir_letra_por_letra(texto_para_imprimir)
print()
print()
time.sleep(1)
print("Há algo de bom neste mundo e vale a pena lutar por isso")
print()
time.sleep(1)

def tela_cadastro():
    nome_completo = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    email = input("Email: ")
    senha = input("Senha: ")
    confirmar_senha = input("Confirmar senha: ")

    if not validar_idade(data_nascimento):
        print("Você deve ter no mínimo 18 anos.")
        return

    if senha != confirmar_senha:
        print("As senhas não são iguais.")
        return

    avatar = Avatar(nome_completo, data_nascimento, email, senha, confirmar_senha)
    print("Cadastro realizado com sucesso!")

    avatar_logado = tela_login(avatar)
    if avatar_logado:
        tela_jogo(avatar_logado)

def validar_idade(data_nascimento):
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade >= 18

def tela_login(avatar):
    print("\n*** LOGIN ***")
    email = input("Email: ")
    senha = input("Senha: ")

    if not avatar.validar_login(email, senha):
        print("Credenciais incorretas.")
        return None

    print("\nLogin bem-sucedido!")
    return avatar

def tela_jogo(avatar):
    print("\n### TELA DO JOGO NETUNO ###")
    classe = escolher_classe()
    ferramenta_batalha = escolher_ferramenta_batalha(classe)
    montaria = escolher_montaria()

    customizar_avatar(avatar)

    distribuir_pontos_classe(classe)
    distribuir_pontos_montaria(montaria)

    mostrar_informacoes(avatar, classe, ferramenta_batalha, montaria)

def escolher_classe():
    print("-----Escolha seu Herói-----")
    print("[1] Paladino")
    print("[2] Atirador")
    print("[3] Guerreiro")
    print("[4] Bárbaro")
    print("[5] Arqueiro")

    while True:
        class_choice = input("Escolha o número do seu Herói: ")

        if class_choice == "1":
            print("Você escolheu o Paladino.")
            return "Paladino"
        elif class_choice == "2":
            print("Você escolheu o Atirador.")
            return "Atirador"
        elif class_choice == "3":
            print("Você escolheu o Guerreiro.")
            return "Guerreiro"
        elif class_choice == "4":
            print("Você escolheu o Bárbaro.")
            return "Bárbaro"
        elif class_choice == "5":
            print("Você escolheu o Arqueiro.")
            return "Arqueiro"
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 5.")

def escolher_ferramenta_batalha(classe):
    if classe == "Paladino":
        return "lança e escudo"
    elif classe == "Atirador":
        return "arma"
    elif classe == "Guerreiro":
        return "Espada e escudo"
    elif classe == "Bárbaro":
        return "machado e marreta"
    elif classe == "Arqueiro":
        return "Arco"

def escolher_ferramenta(op1, op2):
    while True:
        print(f"Escolha entre {op1} e {op2}: ")
        opcao = input()

        if opcao not in (op1, op2):
            print("Opção inválida.")
            continue

        return opcao

def escolher_montaria():
    print("\nEscolha a montaria:")
    montarias = [
        ("Lobo", "2.0 m/s", "3 minutos"),
        ("Urso", "4.5 m/s", "8 minutos"),
        ("Tigre", "2.2 m/s", "4 minutos"),
        ("Leão", "2.5 m/s", "3 minutos"),
        ("Rinoceronte", "3.2 m/s", "4 minutos")
    ]

    for i, (nome, velocidade, tempo_descanso) in enumerate(montarias, 1):
        print(f"{i}) {nome}")

    while True:
        ride_choice = input("Escolha o número da sua montaria: ")

        if ride_choice.isdigit() and 1 <= int(ride_choice) <= len(montarias):
            index = int(ride_choice) - 1
            montaria_escolhida = montarias[index]
            print(f"Você escolheu a montaria: {montaria_escolhida[0]}")
            return montaria_escolhida
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 5.")

def customizar_avatar(avatar):
    # Implementar opções de customização de cabelo, pele, etc.
    pass

def distribuir_pontos_classe(classe):
    if classe == "Paladino":
        atributos = ["Vida", "Mana", "Velocidade de Ataque"]
        pontos = 100

        vida = int(input("Vida: "))
        pontos -= vida
        mana = int(input("Mana: "))
        pontos -= mana
        velocidade_ataque = float(input("Velocidade de Ataque: "))
        pontos -= velocidade_ataque

        mostrar_atributos(atributos, pontos)

    # Adicionar lógica para outras classes

def distribuir_pontos_montaria(montaria):
    if montaria[0] == "Cavala do guerra":
        atributos = ["Velocidade", "Tempo para descanso"]
        pontos = 50

        velocidade = float(input("Velocidade: "))
        pontos -= velocidade
        tempo_descanso = int(input("Tempo para descanso: "))
        pontos -= tempo_descanso

        mostrar_atributos(atributos, pontos)

    # Adicionar lógica para outras montarias

def mostrar_atributos(atributos, pontos):
    print("Distribua seus pontos:")
    for i, atributo in enumerate(atributos):
        print(f"{i + 1}) {atributo}: ")
        valor = int(input())
        pontos -= valor

    print(f"Pontos restantes: {pontos}")

def mostrar_informacoes(avatar, classe, ferramenta_batalha, montaria):
    print("\n** Informações do seu personagem **")
    print(f"Nome: {avatar.nome}")
    print(f"Email: {avatar.email}")
    print(f"Classe: {classe}")
    print(f"Ferramenta de batalha: {ferramenta_batalha}")
    print(f"Montaria: {montaria[0]} (Velocidade: {montaria[1]}, Tempo de Descanso: {montaria[2]})")

# Exemplo de uso
tela_cadastro()
