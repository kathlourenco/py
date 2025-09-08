def letra(palavra):
    vogais = "aeiouAEIOU"
    cont = 0
    for letra in palavra:
        if letra in vogais:
            cont += 1
    return cont 


palavra = input("Digite uma palavra: ")
qtd = letra(palavra)
print(qtd)