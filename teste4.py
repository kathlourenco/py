
print("1- Linux")
print("2- Banco de dados")
print("3- Windows server")
print("4- Lógica e programação")
palestra = int(input("Digite o código da palestra que você irá:  "))

match palestra:
    case 1:
        print("A palestra será no auditório 1")
    case 2:
        print("A palestra será no auditório 2")
    case 3:
        print("A palestra será no auditório 3")
    case 4:
        print("A palestra será no auditório 4")

