# Exercício
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro_str = input('Digite um número inteiro: ')

try:
    numero_inteiro_int = int(numero_inteiro_str)
    numero_par_ou_impar = numero_inteiro_int % 2   

    if numero_par_ou_impar == 0:
        print(f'O número {numero_inteiro_int} é um número par.')
    else:
        print(f'O número {numero_inteiro_int} é um número impar.')
except:
    print('Você não digitou um número inteiro, execuçaõ encerrada.')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
horas_usuario_string = input('Digite que horas são para o formato: ')

try:    
    hora_usuario_int = int(horas_usuario_string)
    
    if hora_usuario_int >= 0 and hora_usuario_int <= 11:
        print('Bom dia.')
    elif hora_usuario_int >= 12 and hora_usuario_int <= 17:
        print('Boa tarde.')
    elif hora_usuario_int >= 18 and hora_usuario_int <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora.') 
except:
    print('Você não digitou o horário correto.')   

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

usuario_nome = input('Digite o seu primeiro nome: ')
tamanho_usuario_nome = len(usuario_nome)

try:
    if tamanho_usuario_nome <= 4:
        print('Seu nome é curto') 
    elif (tamanho_usuario_nome) >= 5 and (tamanho_usuario_nome <= 6):
        print('Seu nome é normal')
    else: 
        print('Seu nome é muito grande')
except:
    print('Você não digitou um nome correto.') 
