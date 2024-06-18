# Exercício:

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada estána palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""
import os


palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    
    letra_digitada_usuário = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada_usuário) > 1:
        print('Digite apenas uma letra.')
        continue    

    if letra_digitada_usuário in palavra_secreta:
        letras_acertadas += letra_digitada_usuário

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada: {palavra_formada}')       
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou! Parabens.')
        print(f'A palavra secreta é: {palavra_secreta}')
        print(f'O número de tentativas foi: {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0

    
