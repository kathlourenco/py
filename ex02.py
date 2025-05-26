nota = int(input("Digite a nota entre 0 e 10: "))
cont = 0
while nota < 0 or nota > 10:
    print("Insira dados válidos")
    cont += 1
    nota = int(input("Digite a nota entre 0 e 10: "))
