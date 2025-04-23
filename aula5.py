
while True:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if num1 != num2:
        break
    else:
        print("Digite números diferentes entre si")

soma = num1 + num2
print(f"A soma entre os numeros é: {soma}")
