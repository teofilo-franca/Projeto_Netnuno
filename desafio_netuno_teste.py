import time
from datetime import datetime

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

    def mostrar_informacoes_customizacao(self):
        print("\n** Informações de customização **")
        print(f"Cabelo: {self.cabelo}")
        print(f"Pele: {self.pele}")
        print(f"Altura: {self.altura} cm")
        print(f"Força: {self.forca}")

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
    avatar.mostrar_informacoes_customizacao()

def escolher_classe():
    print("----- Escolha seu Herói -----")
    print("[1] Paladino")
    print("[2] Atirador")
    print("[3] Guerreiro")
    print("[4] Bárbaro")
    print("[5] Arqueiro")

    while True:
        class_choice = input("Escolha o número do seu Herói: ")

        if class_choice == "1":
            print("Você escolheu o Paladino.")
            return class_choice
        elif class_choice == "2":
            print("Você escolheu o Atirador.")
            return class_choice
        elif class_choice == "3":
            print("Você escolheu o Guerreiro.")
            return class_choice
        elif class_choice == "4":
            print("Você escolheu o Bárbaro.")
            return class_choice
        elif class_choice == "5":
            print("Você escolheu o Arqueiro.")
            return class_choice
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 5.")

def escolher_ferramenta_batalha(classe):
    if classe == "1":
        return "lança e escudo"
    elif classe == "2":
        return "arma"
    elif classe == "3":
        return "Espada e escudo"
    elif classe == "4":
        return "machado e marreta"
    elif classe == "5":
        return "Arco"

def escolher_montaria():
    montarias = [
        ("Cavalo de Guerra", "3.0 m/s", "5 minutos"),
        ("Panda", "2.5 m/s", "6 minutos"),
        ("Lobo Gigante", "3.2 m/s", "4 minutos"),
        ("Dragão Pequeno", "4.5 m/s", "8 minutos"),
        ("Hipogrifo", "3.8 m/s", "7 minutos")
    ]

    print("\n----- Escolha sua Montaria -----")
    for i, (nome, _, _) in enumerate(montarias, 1):
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
    print("\n----- Customização do Avatar -----")
    cabelo = input("Digite o estilo de cabelo: ")
    pele = input("Digite o tom de pele: ")
    altura = int(input("Digite a altura (em cm): "))
    forca = int(input("Digite o nível de força (em escala de 1 a 10): "))

    avatar.customizar_avatar(cabelo, pele, altura, forca)
    print("Avatar customizado com sucesso!")

def distribuir_pontos_classe(classe):
    if classe == "1":
        atributos = ["Vida", "Mana", "Velocidade de Ataque"]
        pontos = 100

        vida = int(input("Vida: "))
        pontos -= vida
        mana = int(input("Mana: "))
        pontos -= mana
        velocidade_ataque = float(input("Velocidade de Ataque: "))
        pontos -= velocidade_ataque

        mostrar_atributos(atributos, pontos)

def distribuir_pontos_montaria(montaria):
    atributos = ["Velocidade", "Tempo para descanso"]
    pontos = 50

    velocidade = float(input("Velocidade da montaria: "))
    pontos -= velocidade
    tempo_descanso = int(input("Tempo para descanso da montaria: "))
    pontos -= tempo_descanso

    mostrar_atributos(atributos, pontos)

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
    print(f"Montaria: {montaria[0]}")
    print(f"Velocidade da montaria: {montaria[1]}")
    print(f"Tempo para descanso da montaria: {montaria[2]}")

# Exemplo de uso
tela_cadastro()
