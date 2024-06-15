#Exercício:

usuario_nome = input('Digite o seu nome completo: ')
usuario_idade = input('Digite a sua idade: ')

usuario_idade_int = int(usuario_idade)

if usuario_idade_int != None and usuario_nome != None:
    print('-' * 10)
    print(f'Seu nome é: {usuario_nome}')
    print(f'Seu nome invertio é: {usuario_nome[::-1]}')

    if ' ' in usuario_nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')

    print(f'Seu nome tem {len(usuario_nome)} letras.')
    print(f'A primeira letra do seu nome é {usuario_nome[0:1:len(usuario_nome)]}')
    print(f' A última letra do seu nome é:{usuario_nome[-1:-2:-1]}')
else:
    print('Desculpe, você deixou campos vazios.')

