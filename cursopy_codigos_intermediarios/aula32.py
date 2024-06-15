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

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas_usuario = input('Digite que horas são: ')

try:
    hora_usuario_int = int(hora_usuario)
    if (hora_usuario_int >= and hora_usuario_int <= 11):
        print('')
except:
    ...    


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""