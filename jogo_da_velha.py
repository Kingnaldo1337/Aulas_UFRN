#Reinaldo Alves Pereira Junior

import random

# Função para imprimir o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + tabuleiro[i][j] + " ", end="|")
        print("\n-------------")

def verificar_vitoria(tabuleiro, player): #função de veridicar vitória
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == player:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == player:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == player:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == player:
        return True
    return False

def jogada_newbee(tabuleiro): #função de jogada newbee
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = "O"
            break

def jogada_nerd(tabuleiro): #função de jogada nerd
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == "O" and tabuleiro[i][2] == " ":
            tabuleiro[i][2] = "O"
            return
        if tabuleiro[i][0] == tabuleiro[i][2] == "O" and tabuleiro[i][1] == " ":
            tabuleiro[i][1] = "O"
            return
        if tabuleiro[i][1] == tabuleiro[i][2] == "O" and tabuleiro[i][0] == " ":
            tabuleiro[i][0] = "O"
            return
        if tabuleiro[0][i] == tabuleiro[1][i] == "O" and tabuleiro[2][i] == " ":
            tabuleiro[2][i] = "O"
            return
        if tabuleiro[0][i] == tabuleiro[2][i] == "O" and tabuleiro[1][i] == " ":
            tabuleiro[1][i] = "O"
            return
        if tabuleiro[1][i] == tabuleiro[2][i] == "O" and tabuleiro[0][i] == " ":
            tabuleiro[0][i] = "O"
            return
    if tabuleiro[0][0] == tabuleiro[1][1] == "O" and tabuleiro[2][2] == " ":
        tabuleiro[2][2] = "O"
        return
    if tabuleiro[0][0] == tabuleiro[2][2] == "O" and tabuleiro[1][1] == " ":
        tabuleiro[1][1] = "O"
        return
    if tabuleiro[1][1] == tabuleiro[2][2] == "O" and tabuleiro[0][0] == " ":
        tabuleiro[0][0] = "O"
        return
    if tabuleiro[0][2] == tabuleiro[1][1] == "O" and tabuleiro[2][0] == " ":
        tabuleiro[2][0] = "O"
        return
    if tabuleiro[0][2] == tabuleiro[2][0] == "O" and tabuleiro[1][1] == " ":
        tabuleiro[1][1] = "O"
        return
    if tabuleiro[1][1] == tabuleiro[2][0] == "O" and tabuleiro[0][2] == " ":
        tabuleiro[0][2] = "O"
        return

    for i in range(3): #função para verificar se é preciso bloquear o player de ganhar.
        if tabuleiro[i][0] == tabuleiro[i][1] == "X" and tabuleiro[i][2] == " ":
            tabuleiro[i][2] = "O"
            return
        if tabuleiro[i][0] == tabuleiro[i][2] == "X" and tabuleiro[i][1] == " ":
            tabuleiro[i][1] = "O"
            return
        if tabuleiro[i][1] == tabuleiro[i][2] == "X" and tabuleiro[i][0] == " ":
            tabuleiro[i][0] = "O"
            return
        if tabuleiro[0][i] == tabuleiro[1][i] == "X" and tabuleiro[2][i] == " ":
            tabuleiro[2][i] = "O"
            return
        if tabuleiro[0][i] == tabuleiro[2][i] == "X" and tabuleiro[1][i] == " ":
            tabuleiro[1][i] = "O"
            return
        if tabuleiro[1][i] == tabuleiro[2][i] == "X" and tabuleiro[0][i] == " ":
            tabuleiro[0][i] = "O"
            return
    if tabuleiro[0][0] == tabuleiro[1][1] == "X" and tabuleiro[2][2] == " ":
        tabuleiro[2][2] = "O"
        return
    if tabuleiro[0][0] == tabuleiro[2][2] == "X" and tabuleiro[1][1] == " ":
        tabuleiro[1][1] = "O"
        return
    if tabuleiro[1][1] == tabuleiro[2][2] == "X" and tabuleiro[0][0] == " ":
        tabuleiro[0][0] = "O"
        return
    if tabuleiro[0][2] == tabuleiro[1][1] == "X" and tabuleiro[2][0] == " ":
        tabuleiro[2][0] = "O"
        return
    if tabuleiro[0][2] == tabuleiro[2][0] == "X" and tabuleiro[1][1] == " ":
        tabuleiro[1][1] = "O"
        return
    if tabuleiro[1][1] == tabuleiro[2][0] == "X" and tabuleiro[0][2] == " ":
        tabuleiro[0][2] = "O"
        return

    # Caso contrário, joga de forma aleatória
    jogada_newbee(tabuleiro)

# Função principal do jogo
def jogar_jogo_da_velha():
    tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)

        # Verifica se houve empate
        if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
            print("Empate!")
            break

        # Verifica se algum player venceu
        if verificar_vitoria(tabuleiro, "X"):
            print("Você venceu!")
            break
        if verificar_vitoria(tabuleiro, "O"):
            print("O computador venceu!")
            break

        if player == "X":
            while True:
                linha = int(input("Digite a linha (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))
                if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "X"
                    break
                print("Jogada inválida. Tente novamente.")
        else:
            if modo_jogo == "NEWBEE":
                jogada_newbee(tabuleiro)
            else:
                jogada_nerd(tabuleiro)

        player = "O" if player == "X" else "X"

# Início do jogo
print("Bem-vindo ao Jogo da Velha!")
modo_jogo = input("Escolha o modo de jogo (NEWBEE ou NERD): ").upper()

if modo_jogo != "NEWBEE" and modo_jogo != "NERD":
    print("Modo de jogo inválido.")
else:
    jogar_jogo_da_velha()