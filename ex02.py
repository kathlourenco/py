def somar(a, b):
    if type(a) == str or type(b) == str:
        raise TypeError("Os valores devem ser numéricos")
    c = a + b
    print(f"Resultado: {c}")

somar(10, 20)
somar(2.5, 5.9)

try:
    somar("abc", "xyz")
except TypeError as mensagem:
    print(mensagem)
