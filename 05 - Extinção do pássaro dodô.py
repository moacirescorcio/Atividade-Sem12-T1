ano = 1599
nascidos = 0
mortes = 0
populacao = int(input())
extincao = (populacao * 0.1)

while populacao > extincao:    
    nascidos = round((populacao * 0.01), 0)
    mortes = round((populacao * 0.06), 0)
    populacao = round((populacao - mortes) + (populacao + nascidos), 0)
    ano += 1
    print(f'{ano:},{nascidos},{mortes},{populacao}')