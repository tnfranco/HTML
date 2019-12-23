usuario = input("Digite o nome do seu usuario: ")
senha = input("Digite sua senha: ")
while senha == usuario:
    print("Senha nao pode ser igual ao usuario")
    usuario = input("Digite o nome do seu usuario: ")
    senha = input("Digite sua senha: ")
