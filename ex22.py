def contar_palavras(frase):
    palavras = frase.split()  # divide a frase em palavras
    return len(palavras)      # retorna a quantidade de palavras

# Programa principal
texto = input("Digite uma frase: ")
quantidade = contar_palavras(texto)
print(f"A frase tem {quantidade} palavras.")