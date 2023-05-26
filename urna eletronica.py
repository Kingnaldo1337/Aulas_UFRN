import random

def votar():
    votos_senna = 0
    votos_barri = 0

    while True:
        voto = input("Digite o número do piloto que deseja votar (1 - Ayrton Senna | 2 - Rubens Barrichello | 0 - Encerrar votação): ")

        if voto == "1":
            votos_senna += 1
        elif voto == "2":
            votos_barri += 1
        elif voto == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

    return votos_senna, votos_barri


def calcular_porcentagem(votos_senna, votos_barri):
    total_votos = votos_senna + votos_barri
    porcentagem_senna = (votos_senna / total_votos) * 100
    porcentagem_barri = (votos_barri / total_votos) * 100
    return porcentagem_senna, porcentagem_barri


def exibir_resultados(votos_senna, votos_barri):
    porcentagem_senna, porcentagem_barri = calcular_porcentagem(votos_senna, votos_barri)
    print("======= Resultados =======")
    print("Ayrton Senna: {} votos, {:.2f}%".format(votos_senna, porcentagem_senna))
    print("Rubens Barrichello: {} votos, {:.2f}%".format(votos_barri, porcentagem_barri))


def main():
    print("======= Urna Eletrônica =======")
    print("Digite o número correspondente ao piloto que deseja votar.")
    print("1 - Ayrton Senna")
    print("2 - Rubens Barrichello")
    print("0 - Encerrar votação")

    votos_senna, votos_barri = votar()
    exibir_resultados(votos_senna, votos_barri)


# Execução do programa
main()