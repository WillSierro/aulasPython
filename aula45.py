"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = 'William'.__iter__()
# print(texto)
# texto = iter('William')
# print(texto.__next__())
# texto = iter('William')
# print(next(texto))

# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)