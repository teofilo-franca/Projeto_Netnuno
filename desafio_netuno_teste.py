import time
from datetime import datetime
import re

class Avatar:
    def __init__(self, nome, data_nascimento, email, senha, confirmar_senha):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
        self.senha = senha
        self.confirmar_senha = confirmar_senha
        self.cabelo = None
        self.pele = None
        self.altura = None
        self.forca = None

    def validar_login(self, email, senha):
        return self.email == email and self.senha == senha

    def customizar_avatar(self, cabelo, pele, altura, forca):
        self.cabelo = cabelo
        self.pele = pele
        self.altura = altura
        self.forca = forca

    def mostrar_informacoes(self, personagem, ferramenta_batalha, montaria):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Personagem: {personagem['nome']}")
        print(f"Cabelo: {self.cabelo}")
        print(f"Pele: {self.pele}")
        print(f"Altura: {self.altura} cm")
        print(f"Força: {self.forca}")
        print(f"Vida: {personagem['vida']}")
        print(f"Mana: {personagem['mana']}")
        print(f"Velocidade de Ataque: {personagem['velocidade_ataque']}")
        print(f"Ferramenta de batalha: {ferramenta_batalha}")
        print(f"Montaria: {montaria['nome']}")
        print(f"Velocidade da montaria: {montaria['velocidade']}")
        print(f"Tempo para descanso da montaria: {montaria['tempo_descanso']}")

def validar_data_nascimento(data_nascimento):
    datetime.strptime(data_nascimento, "%d/%m/%Y")

def imprimir_letra_por_letra(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.1)
    print()

def tela_cadastro():
    imprimir_letra_por_letra(" * * * * * JOGO NETUNO * * * * * ")
    print()
    time.sleep(1)
    print("Há algo de bom neste mundo e vale a pena lutar por isso")
    print()
    time.sleep(1)

    while True:
        nome_completo = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")

        try:
            validar_data_nascimento(data_nascimento)
            break
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    while True:
        email = input("Email: ")

        if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Verifica o formato do email
            break
        else:
            print("Formato de email inválido. Tente novamente.")

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
    while True:
        print("\n*** LOGIN ***")
        email = input("Email: ")
        senha = input("Senha: ")

        if avatar.validar_login(email, senha):
            print("\nLogin bem-sucedido!")
            return avatar
        else:
            print("Credenciais incorretas. Tente novamente.")

def tela_jogo(avatar):
    print("\n### TELA DO JOGO NETUNO ###")
    print()
    personagem = escolher_personagem()
    ferramenta_batalha = escolher_ferramenta_batalha(personagem)
    montaria = escolher_montaria()

    customizar_avatar(avatar)

    avatar.mostrar_informacoes(personagem, ferramenta_batalha, montaria)

    
    print("\n       Obrigado por jogar o JOGO NETUNO!")

def escolher_personagem():
    personagens = [
        {"nome": "Paladino", "vida": 70, "mana": 30, "velocidade_ataque": 1.80},
        {"nome": "Atirador", "vida": 80, "mana": 20, "velocidade_ataque": 1.95},
        {"nome": "Guerreiro", "vida": 90, "mana": 10, "velocidade_ataque": 2.00},
        {"nome": "Bárbaro", "vida": 85, "mana": 15, "velocidade_ataque": 1.60},
        {"nome": "Arqueiro", "vida": 75, "mana": 25, "velocidade_ataque": 2.20},
    ]

    print("----- Escolha seu Herói -----")
    for i, personagem in enumerate(personagens, 1):
        print(f"[{i}] {personagem['nome']}")

    while True:
        personagem_choice = input("Escolha o número do seu Herói: ")

        if personagem_choice.isdigit() and 1 <= int(personagem_choice) <= len(personagens):
            index = int(personagem_choice) - 1
            personagem_escolhido = personagens[index]
            print(f"Você escolheu o {personagem_escolhido['nome']}.")
            return personagem_escolhido
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 5.")

def escolher_ferramenta_batalha(personagem):
    if personagem["nome"] == "Paladino":
        return "lança e escudo"
    elif personagem["nome"] == "Atirador":
        return "arma"
    elif personagem["nome"] == "Guerreiro":
        return "Espada e escudo"
    elif personagem["nome"] == "Bárbaro":
        return "machado e marreta"
    elif personagem["nome"] == "Arqueiro":
        return "Arco"

def escolher_montaria():
    montarias = [
        {"nome": "Leão", "velocidade": "2.0 m/s", "tempo_descanso": "3 minutos"},
        {"nome": "Tigre", "velocidade": "1.6 m/s", "tempo_descanso": "4 minutos"},
        {"nome": "Lobo", "velocidade": "1.8 m/s", "tempo_descanso": "4 minutos"},
        {"nome": "Rinoceronte", "velocidade": "4.5 m/s", "tempo_descanso": "1 minutos"},
        {"nome": "Helefante", "velocidade": "4.0 m/s", "tempo_descanso": "2 minutos"},
    ]

    print("\n----- Escolha sua Montaria -----")
    for i, montaria in enumerate(montarias, 1):
        print(f"[{i}] {montaria['nome']}")

    while True:
        ride_choice = input("Escolha o número da sua montaria: ")

        if ride_choice.isdigit() and 1 <= int(ride_choice) <= len(montarias):
            index = int(ride_choice) - 1
            montaria_escolhida = montarias[index]
            print(f"Você escolheu a montaria: {montaria_escolhida['nome']}")
            return montaria_escolhida
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 5.")

def customizar_avatar(avatar):
    cabelo = input("Digite o estilo de cabelo: ")
    pele = input("Digite o tom de pele: ")
    altura = input("Digite a altura (em cm): ")
    forca = input("Digite o nível de força (em escala de 1 a 10): ")

    avatar.customizar_avatar(cabelo, pele, altura, forca)
    print("\nAvatar customizado com sucesso!")

tela_cadastro()
