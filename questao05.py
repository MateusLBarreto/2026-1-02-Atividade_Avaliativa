# Questao 5
import math
repeticoes = int(input("Digite quantos valores seram digitados: "))
vetorValores = []
vMaiorMeida = 0
for i in range(1, repeticoes + 1):
    valor = int(input("Digite um valor; "))
    vetorValores.append(i)
soma = sum(vetorValores)
media = soma / repeticoes
print(f"A soma desses numeros é igual a: {soma}\nA media aritmetica desses numeros é igual a: {media}")
print(f"O maior desses numeros é: {max(vetorValores)}\nO menor desses numeros é: {min(vetorValores)}")
for j in vetorValores:
    if j > media:
        vMaiorMeida += 1
print("Existem", vMaiorMeida, "Valores maiores que a media.")