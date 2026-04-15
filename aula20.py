primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

int_primeiro = int(primeiro_valor)
int_segundo = int(segundo_valor)

if int_primeiro > int_segundo:
    print(f'primeiro_valor={primeiro_valor} é maior que segundo_valor={segundo_valor}')
elif int_primeiro < int_segundo:
    print(f'primeiro_valor={primeiro_valor} é menor que segundo_valor={segundo_valor}')
elif int_primeiro == int_segundo:
    print(f'primeiro_valor={primeiro_valor} é igual ao segundo_valor={segundo_valor}')