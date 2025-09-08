lista1 = []
lista2 = []

for i in range (5):
    num1 = int(input("Digite um número para a tupla 1: "))
    lista1.append(num1)

for i in range (5):
    num2 = int(input("Digite um número para a tupla 2:"))
    lista2.append(num2)

lista3 = lista1 + lista2
lista3 = list(tuple(lista3))
print(lista3)
