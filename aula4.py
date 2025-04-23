n = int(input("Quantos numeros voce quer digitar?: "))
somapares = 0
somaimpares = 0
contpares = 0
contimpares = 0

while n > 0:
    num = int(input("Digite um numero: "))

    if num % 2 == 0:
        somapares += num
        contpares += 1
    else:
        somaimpares += num
        contimpares += 1
    n -= 1
mediapares = somapares / contpares
mediaimpares = somaimpares / contimpares
print(f"{mediapares}")
print(f"{mediaimpares}")