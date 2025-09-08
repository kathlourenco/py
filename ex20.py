def contar_vogais(texto): # definiu uma funcao para contar voais de um texto que é o parametro
    vogais = "aeiouAEIOU" # definiu uma variavel contendo todas as vogais
    contador = 0  # definiu um contador que ira contar as vogais percorrendo na frase
    for letra in texto: # definiu um for para percorrer letras de uma uma string
        if letra in vogais: # definiu uma condicao para saber se a letra é uma vogal
            contador += 1 # definiu um contador para somar vogais quando fossem percorridas
    return contador # retornou o processo ate ele ser finalizado

frase = "Engenharia de Software"
print(f"A frase tem {contar_vogais(frase)} vogais.")
