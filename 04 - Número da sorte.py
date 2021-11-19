nascimento = int(input('Digite sua data de nascimento no formato ddmmaaaa'))
soma = 0

while nascimento > 0:
    soma = (nascimento % 10) + soma
    nascimento = (nascimento // 10)

print(f'Seu número da sorte é {soma}')