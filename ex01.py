def aprovacao(prova1, prova2):
    media = (prova1 + prova2)/2
    if media >= 6:
        print("Voce foi aprovado")
    else:
        print("Voce foi reprovado")

nota1 = int(input("Digite sua primeira nota de 0 a 10: "))
nota2 = int(input("Digite sua primeira nota de 0 a 10: "))

aprovacao(nota1, nota2)