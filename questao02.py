# Questao 2
import random
repeticoes = int(input("Digite a quantia de valores aleatorios: "))
for i in range(0, repeticoes):
    print(i + 1,"o numero aleatorio:",random.randint(1, 100))