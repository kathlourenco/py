def fazer_lista(frase):
    return frase.split()


frase = input("Digite uma frase: ")
palavras = fazer_lista(frase)
print(palavras)