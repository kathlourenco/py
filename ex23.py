nota1 = int(input("Digite sua nota 1: "))
nota2 = int(input("Digite sua nota 2: "))
media = (nota1 + nota2) / 2

def aprovado_reprovado(media):
    if media < 6:
        print("reprovado")
    else:
        print("aprovado")
aprovado_reprovado(media)