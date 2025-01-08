"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Willia', 'João', 'Ricardo']
nome1, nome2, nome3 = nomes
print(nome1)
# *resto = *_ como convensão universal
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, _)