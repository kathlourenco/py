def contar_palavras(string):
    return len(string.split())

string = input("digite uma frase: ")
palavras = contar_palavras(string)
print(palavras)
