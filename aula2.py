cont = 1
verif = 0
while cont <= 10:
    idade = int(input("Digite sua idade: "))

    if idade < 18 :
        verif = verif + 1
    cont += 1

print(f"{verif} pessoas")

