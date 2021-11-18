poupanca = 10000
taxa_p = 0.007
taxa_carro = 0.004
preco_carro = float(input('Insira o valor do carro: '))
meses = 0

while preco_carro > poupanca:
    poupanca = (poupanca * taxa_p) + poupanca
    preco_carro = (preco_carro * taxa_carro) + preco_carro
    meses += 1

print(f'Você vai precisar esperar {meses} meses para conseguir comprar o carro à vista!')