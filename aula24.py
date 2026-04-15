# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 
#  K a u ã
# -4-3-2-1
# nome = 'Kauã'
# # print(nome[-4])
# print('ã' in nome)
# print('zero' in nome)
# print(10*'-')
# print('Kau' not in nome)
# print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')