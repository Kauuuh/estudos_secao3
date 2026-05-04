"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    resto = numero_int % 2

    if resto == 0:
        print('Seu número é par')
    else:
        print('Seu número é impar')
except:
    print('Você não colocou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Quê horas são? ')
horario_int = int(horario)

if horario_int >= 0 and horario_int <= 11:
    print('Bom dia')
elif horario_int >= 12 and horario_int <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual é o seu primeiro nome? ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto.')
elif letras >= 5 and letras <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")