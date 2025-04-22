numero = int(input("Digite um número: "))

print("1- O dobro")
print("2- A metade")
print("3- 10% do número")
calc = int(input("Qual cálculo você quer realizar? "))

match calc:
    case 1:
        r1 = numero * 2
        print(f"O valor final será: {r1}")
    case 2:
        r2 = numero / 2
        print(f"O valor final será: {r2}")
    case 3:
        r3 = numero * 0.1
        print(f"O valor final será: {r3}")

