nome = 'Kauã Patrik'
altura = 1.80
peso = 95
imc = peso / (altura * altura)    # IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
# print(nome, 'tem', altura, end=',\r\n')
# print('pesa', peso, 'quilos e seu IMC é')
# print(imc)

# Kauã Patrik tem 1.75,
# pesa 95 quilos e seu IMC é
# 31.020408163265305