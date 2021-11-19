populacao_a = int(input('População do país A: '))
populacao_b = int(input('População do país B: '))

ano = 0
if populacao_a > populacao_b:
    while populacao_a > populacao_b:
        populacao_a = (populacao_a * 0.02) + populacao_a
        populacao_b = (populacao_b * 0.03) + populacao_b
        ano += 1

    print(f'Levará {ano} anos para a população do país B ultrapassar a poplução do país A!')

else:
    while populacao_b > populacao_a:
        populacao_a = (populacao_a * 0.03) + populacao_a
        populacao_b = (populacao_b * 0.02) + populacao_b
        ano += 1

    print(f'Levará {ano} anos para a população do país A ultrapassar a população do país B!')