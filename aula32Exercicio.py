"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um numero Inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 ==0
#     par_impar_texto = 'Impar'

#     if par_impar:
#         par_impar_texto = 'Par'
#     print(f'O numero digitado: ({numero}) ele é {par_impar_texto}')
# else:
#     print(f'O numero digitado: ({numero}) não é um numero inteiro')

# try:
#     numero_int = int(numero)
#     par_impar = numero_int % 2 ==0
#     par_impar_texto = 'Impar'

#     if par_impar:
#         par_impar_texto = 'Par'
#     print(f'O numero digitado: ({numero}) ele é {par_impar_texto}')
# except:
#     print(f'O numero digitado: ({numero}) não é um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora: ')
# hora_int = int(hora)

# if hora_int >= 0 and hora_int <= 11:
#     print('Bom dia!')
# elif hora_int >= 12 and hora_int <= 17:
#     print('Boa tarde!')
# elif hora_int >= 18 and hora_int <= 23:
#     print('Boa noite')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#             print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Digitou uma hora que não existe')
# except:
#     print('Por favor digite um numero inteiro valido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Digite o seu primeiro nome: ')

if entrada:
    if len(entrada) <= 4:
        print('Seu nome é curto!')
    elif len(entrada) >= 5 and len(entrada) <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é grande!')
else:
    print('Digite alguma noisa')