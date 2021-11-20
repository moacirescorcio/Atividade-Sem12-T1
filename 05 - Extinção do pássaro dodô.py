ano = 1599
populacao = int(input('Insira a população de dodôs: '))
extincao = (populacao * 0.1)

while populacao > extincao:    
    nascidos = (populacao * 0.01)
    mortes = (populacao * 0.06)
    populacao = (populacao - mortes + nascidos)
    ano = ano + 1
    print(f'Ano: {ano}Nascidos: {nascidos:.0f}Mortes: {mortes:.0f}População: {populacao:.0f}')