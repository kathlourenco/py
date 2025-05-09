nome= input("Digite seu nome (use ao menos 3 caracteres): ")

while len(nome) <= 3:
    print("Digite um nome válido! ")
    nome = input("Digite seu nome (use ao menos 3 caracteres): ")

idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
    print("Digite uma idade válida!")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salario: "))

while salario <0:
    print("Digite um salário válido!")
    salario = float(input("Digite seu salario: "))

sexo = input("Digite seu sexo: f- feminino / m- masculino: ")

while sexo != "f" and sexo != "m":
    print("Digite um sexo válido!")
    sexo = input("Digite seu sexo: f- feminino / m- masculino: ")

estadoCivil = input("Digite seu estado civil: s- solteiro / c- casado/ v- viuvo/ d- divorciado: ")

while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
    print("Digite um estado civil válido!")
    estadoCivil = input("Digite seu estado civil: s- solteiro / c- casado/ v- viuvo/ d- divorciado: ")

else:
    print(f"Seu nome é: {nome}")
    print(f"Sua idade é: {idade}")
    print(f"Seu salário é: {salario}")
    print(f"Seu sexo é: {sexo}")
    print(f"Seu estado civil é: {estadoCivil}")