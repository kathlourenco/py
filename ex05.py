raio = int(input("Digite o tamanho do raio em cm: "))

def area():
    return (raio * raio) * 3.14

def perimetro():
    return (3.14 * raio * 2)

print(f"O perimetro do circulo com o raio {raio} é {perimetro()}cm e a área é {area()}cm2")
