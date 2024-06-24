# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Exercício: Minha resposta (Após correção)

qntd_acertos = 0

for pergunta in perguntas:
    print('Pergunta :', pergunta['Pergunta'])
    print('')

    for i , opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')
        
    print('')

    escolha_usuario = input('Escolha sua resposta: ')

    
    try:
        if escolha_usuario.isdigit():  
            escolha_usuario_int = int(escolha_usuario) 
           
        if pergunta['Opções'][escolha_usuario_int] == pergunta['Resposta']:
            print('Acertou.')
            print('')
            qntd_acertos += 1
        else:
            print('Errou.')
            print('')

    except IndexError:
        print('Errado, você não selecionou uma opção válida.')
    except NameError:    
        print('Errado, você não selecionou uma opção válida.')

print(f'Você acertou {qntd_acertos} de {len(perguntas)}')


# Exercício: Correção

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')