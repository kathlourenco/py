num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais um numero: "))

def soma_igual(num1, num2, num3):
    if num1 + num2 == num3 or num2 + num3 == num1 or num1 + num3 == num2:
        return True

print(soma_igual(num1, num2, num3))