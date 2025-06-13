lista = []
while len(lista) < 5:
    try:
        n = int(input("Informe um número: "))
        lista.append(n)
    except ValueError:
        print("O valor deve ser inteiro")
print(lista)

while True:
    try:
        indice = int(input("Informe um índice: "))
        print(f"No indice {indice} está o valor {lista[indice]}")
    except IndexError:
        print("O índice não existe na lista")
    except ValueError:
        print("O valor deve ser inteiro")
    else:
        break