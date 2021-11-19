populacao_a = int(input())
populacao_b = int(input())

ano = 0

while populacao_a > populacao_b:
    populacao_a = (populacao_a * 0.02) + populacao_a
    populacao_b = (populacao_b * 0.03) + populacao_b
    ano += 1

print(ano)