"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada estána palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""
palavra_secreta = 'perfume'
iterador = iter(palavra_secreta)
mascara_palavra_secreta = ''

for letra in palavra_secreta:
    mascara_palavra_secreta += letra
    print(mascara_palavra_secreta)
'''
while contador == True:
    
    letra_digitada_usuario_str = input('Digite uma letra: ')

    
else:
    ...
'''