usu = input("Digite o nome do seu usuario: ")
senha = input("Digite sua senha: ")
cont = 0

while usu == senha:
    print("Insira dados diferentes")
    cont += 1
    usu = input("Digite o nome do seu usuario: ")
    senha = input("Digite sua senha: ")