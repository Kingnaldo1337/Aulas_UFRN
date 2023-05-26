# Reinaldo Alves Pereira Junior

from os import system #biblioteca para limpar tela.
from time import sleep #biblioteca para dar um tempinho antes de aparecer as informações.
lista_nomes = [] #lista de nomes.
lista_tel = [] #lista de números telefonicos.

def login(): #Função para verificarção de login.
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    system("cls")
    
    if usuario == "admin" and senha == "admin":
        print("Login bem-sucedido!")
        menu()
    else:
        print("Credenciais inválidas. Tente novamente.")
        login()
        
def menu(): #função para menu.
    print("*****AGENDA*****")
    print("1 CADASTRAR USUÁRIO")
    print("2 PESQUISAR USUÁRIO")
    print("3 ATUALIZAR USUÁRIO")
    print("4 APAGAR USUÁRIO")
    print("5 LISTAR USUÁRIOS")
    print("0 SAIR")
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        pesquisar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        apagar()
    elif opcao == "5":
        listar()
    elif opcao == "0":
        exit()
    else:
        print("Opção inválida. Digite uma das opções acima.")
        menu()    
        system("cls")
def cadastrar(): #função para cadastrar contato.
    system("cls")
    nome = input("Digite seu nome: ")
    tel = int(input("Digite seu número de celular: "))
    lista_nomes.append(nome)
    lista_tel.append(tel)
    print("Usuário cadastrado com sucesso")
    menu()
    
def pesquisar(): #função para pesquisar contato.
    pesquisa = input("Digite o nome do usuário que você deseja procurar: ")
    if pesquisa in lista_nomes:
        index = lista_nomes.index(pesquisa)
        telefone = lista_tel[index]
        print("Nome: ", pesquisa)
        print("Telefone: ", telefone)
    else:
        print("Usuário não encontrado.")
           
    menu()
    system("cls")
def listar(): #função para listar todos contatos.
        system("cls")
        for i in range(len(lista_nomes)):
            print("contatos:")
            print("Nome: ", lista_nomes[i])
            print("Telefone: ", lista_tel[i])
        sleep(4)
        menu()
        
    
    
def atualizar(): #função para atualizar nome e número do contato.
    system("cls")
    pesq = input("Digite o nome do contato que deseja atualizar: ")

    if pesq in lista_nomes:
        index = lista_nomes.index(pesq)

        novo_nome = input("Digite o novo nome: ")
        novo_tel = int(input("Digite o novo número telefônico: "))

        lista_nomes[index] = novo_nome
        lista_tel[index] = novo_tel

        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado.")

    menu()
    
def apagar(): #função para apagar contato.
    system("cls")
    apagar_contato = input("Digite o nome do contato que deseja apagar: ")

    if apagar_contato in lista_nomes:
        index = lista_nomes.index(apagar_contato)

        del lista_nomes[index]
        del lista_tel[index]

        print("Contato apagado com sucesso!")
    else:
        print("Contato não encontrado.")

    menu()
login() #chama o login primeiro e se caso o login for certo, irá chamar o Menu abaixo.
menu()# chama o menu toda vez que seleciona uma opção.