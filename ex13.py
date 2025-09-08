nota = 0
lista = []

while True:
    nota = int(input("Insira sua nota: "))
    if nota < 0:
        break
    lista.append(nota)

print(f"A lista tem {len(lista)} notas")
print(f"A lista é: {lista}")
print(f"A média aritmética é: {sum(lista) / len(lista)}")

