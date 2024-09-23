from socket import *

# Configuração da Conexão
HOST = '127.0.0.1'  # Altere para o IP do servidor se necessário
PORTA = 12345        # Escolha uma porta livre

# Estabelece a conexão
conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((HOST, PORTA))

# Função para autenticação
def autenticar():
    while True:
        matricula = input("Informe sua matrícula: ")
        senha = input("Informe sua senha: ")
        conexao.send(f"{matricula},{senha}".encode())
        resposta = conexao.recv(1024).decode()
        print(resposta)
        if "sucesso" in resposta:
            return True

# Função para menu do cliente
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Visualizar Saldo")
        print("4 - Sair")
        opcao = input("Opção: ")
        
        if opcao == '1':
            valor = input("Digite o valor a ser depositado: ")
            conexao.send(f"depositar,{valor}".encode())
            print(conexao.recv(1024).decode())
        elif opcao == '2':
            valor = input("Digite o valor a ser sacado: ")
            conexao.send(f"sacar,{valor}".encode())
            print(conexao.recv(1024).decode())
        elif opcao == '3':
            conexao.send("saldo".encode())
            print("Saldo:", conexao.recv(1024).decode())
        elif opcao == '4':
            conexao.send("sair".encode())
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Autenticar e exibir menu
if autenticar():
    menu()

conexao.close()
