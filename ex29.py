def lados_poligono(poligono):
    if poligono == 3:
        print("triangulo")
    elif poligono == 4:
        print("quadrilatero")
    elif poligono == 5:
        print("pentagono")
    else:
        print("valor invalido")

poligono = int(input("digite o numero de lados do poligono: "))
lados_poligono(poligono)

