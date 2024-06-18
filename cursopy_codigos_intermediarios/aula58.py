import os

lista_de_compras = []
indices_lista = range(len(lista_de_compras))

while True:
    acao_usuario = input('Digite [I] para inserir, [A] para apagar e [L] para listar: ')
    acao_usuario_upper = acao_usuario.upper()

    if len(acao_usuario) > 1:
        print('Você não digitou uma opção válida ')
        continue

    if (acao_usuario_upper != 'I') and (acao_usuario_upper != 'A') and (acao_usuario_upper != 'L'):
        print('Selecione apenas uma das opções informas: [I]nserir, [A]pagar e [L]istar ')
        continue

    if acao_usuario_upper == 'I':
        os.system('cls')
        item_inserido_usuario = input('A AÇÃO selecionada foi a de INSERIR, informe qual item deseja inserir: ')
        lista_de_compras.append(item_inserido_usuario)
        indices_lista = range(len(lista_de_compras))

        for indice in indices_lista:
            print(indice, lista_de_compras[indice])

    elif acao_usuario_upper == 'A':
        os.system('cls')
        indice_apagar_item_usuario = int(input('A AÇÃO selecionada foi a de APAGAR, informe o indice do item que deseja apagar: '))
        lista_de_compras.pop(indice_apagar_item_usuario)
        print(f'O item de indice {indice_apagar_item_usuario} foi removido da Lista.')
        indices_lista = range(len(lista_de_compras))

        for indice in indices_lista:
            print(indice, lista_de_compras[indice])

    elif acao_usuario_upper == 'L':

        if lista_de_compras == list():
            
            print('Primeiro adicione valores a lista.')
            
        else:
            os.system('cls')
            print('A AÇÃO selecionada foi a de LISTAR, segue lista abaixo: ')

            indices_lista = range(len(lista_de_compras))

            for indice in indices_lista:
                print(indice, lista_de_compras[indice])
    else:
        ...            
