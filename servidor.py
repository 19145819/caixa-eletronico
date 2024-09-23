from socket import *

# Configura a Conexão
HOST = '127.0.0.1'  # Altere para o IP desejado
PORTA = 12345        # A mesma porta escolhida no cliente

# Estabelece a conexão
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORTA))
sockobj.listen(1)
saldo = 0  # Saldo inicial

while True:
    # Aceita conexão do cliente
    conexao, endereco = sockobj.accept()
    print('Conectado:', endereco)
    
    while True:
        # Recebe informação e decodifica para string
        data = conexao.recv(1024).decode()
        if not data:
            break

        print("Cliente:", data)
        
        if data.startswith("sair"):
            conexao.send("Conexão encerrada.".encode())
            break
        
        if "," in data:
            matricula, senha = data.split(",")
            if matricula == "123456" and senha == "123456":
                conexao.send("Login realizado com sucesso.".encode())
            else:
                conexao.send("Falha no login. Tente novamente.".encode())
                continue
        
        comando, *args = data.split(",")
        
        if comando == "depositar":
            valor = float(args[0])
            saldo += valor
            conexao.send(f"Depósito realizado. Saldo atual: {saldo}".encode())
        elif comando == "sacar":
            valor = float(args[0])
            if valor > saldo:
                conexao.send("Saldo insuficiente.".encode())
            else:
                saldo -= valor
                conexao.send(f"Saque realizado. Saldo atual: {saldo}".encode())
        elif comando == "saldo":
            conexao.send(str(saldo).encode())
    
    print('Desconectado', endereco)
    conexao.close()
