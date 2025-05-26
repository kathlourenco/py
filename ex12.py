soma = 0
quantidade = 0
nota = float(input("Digite uma nota (ou -1 para encerrar): "))

while nota != -1:             # enquanto for diferente de -1
    if 0 <= nota <= 10:       # se a nota for maior que zero e menor que 10
        soma += nota          # soma a nota ao total
        quantidade += 1
    else:
        print("Nota inválida.")
    nota = float(input("Digite outra nota (ou -1 para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
    print("Média das notas:", media)
else:
    print("Nenhuma nota válida foi digitada.")