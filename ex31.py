lista_par = []
lista_impar = []

for i in range(10):
    num = int(input("digite um número: "))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(lista_par)
print(lista_impar)