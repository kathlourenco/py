def poligonos(lados):
    if lados == 3:
        print("triangulo")
    elif lados == 4:
        print("quadrilatro")
    elif lados == 5:
        print("pentagono")
    else:
        print("valor invalido")
lados = int(input("Digite a quantidade de lados: "))
poligonos(lados)