# Questao 3
numero = int(input("Digite um valor: "))
vetorValores = []
for i in range(1, numero):
    if numero % i == 0:
        vetorValores.append(i)
if sum(vetorValores) == numero:
    print(numero, "é um numero perfeito.")
else:
    print(numero, "não é um numero perfeito.")