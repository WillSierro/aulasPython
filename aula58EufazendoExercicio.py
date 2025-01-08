"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_compra = []



                
while True:
    selecione_opcao = input('Selecione uma opção: \n'
                  '[I]Inserir [A]Apagar [L]Listar [S]Sair: \n'
                  '').upper()

    if selecione_opcao == "I":
        os.system('cls')
        print(f'Sua Lista de compras já contém os seguintes itens: {lista_compra}')
        inserir_nome = input('Digite o nome do novo item a ser adicionado na Lista: ')
        lista_compra.append(inserir_nome)
        continue
    if selecione_opcao == 'A':
        for i in enumerate(lista_compra):
            print(i)
        apagar = input('Selecione o Indice referente ao Item ao qual deseja remover de sua lista: ')
        apagar = int(apagar)
        lista_compra.pop(apagar)
        continue
    if selecione_opcao == 'L':
        for i in enumerate(lista_compra):
            print(i)
            print(lista_compra)
    
    break
    