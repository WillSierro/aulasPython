primeiroValor = input('Digite um valor: ')
segundoValor = input('Digite outro valor: ')

primeiroValorInt = int(primeiroValor)
segundoValorInt = int(segundoValor)

if primeiroValor > segundoValor:
    print(f'O {primeiroValor=} é maior que o {segundoValor=}')
elif primeiroValor == segundoValor:
    print(f'O {primeiroValor=} é igual ao {segundoValor=}')
elif primeiroValor < segundoValor:
    print(f'O {primeiroValor=} é menor que o {segundoValor=}')
else:
    print('Você não digitou nenhum numéro valido!')

