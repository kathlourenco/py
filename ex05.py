def somatorio(lista):
    soma = 0
    for numero in lista:
        try:
            soma += numero
        except TypeError:
            print(f"Ignorando valor inválido: {numero}")
    return soma

valores = [10, "a", 20, "xyz", 30]
print(f"A soma dos valores é {somatorio(valores)}")