nota = int(input("Digite uma nota entre 0 e 10: "))

while nota >= 10 or nota <= 0:
    print("Digite uma nota válida!")
    nota = int(input("Digite uma nota entre 0 e 10: "))

else:
    print(f"Sua nota é: {nota}")