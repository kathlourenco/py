def remover_espaco(frase):
    return frase.strip()


frase = input("Digite uma frase com espaços no inicio e no final: ")
nova = remover_espaco(frase)
print(nova)