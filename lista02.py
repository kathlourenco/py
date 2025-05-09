listaNum = []

for i in range(10):
    num = int(input("Digite um número: "))
    listaNum.append(num)
print(listaNum)

media = (sum(listaNum)) / 10
print(f"A media dos numeros da lista é: {media}")


