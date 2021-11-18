metros_tartaruga = float(input('Insira o valor da distância em que a tartaruga começará: '))
metros_lebre = 0
minuto = 0

while metros_tartaruga > metros_lebre:
    tartaruga = metros_tartaruga
    lebre = metros_lebre
    minuto += 1
    metros_tartaruga += 1
    metros_lebre += 10

print(f'A lebre passará a tartatuga em {minuto} minutos')