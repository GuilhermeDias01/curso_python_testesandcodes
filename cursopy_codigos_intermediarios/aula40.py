# Exercício: 
while True:

    valor1_string= input('Digite o primeiro valor: ')
    valor2_string = input('Digite o segundo valor: ')
    operador_string = input('Digite o operador a ser utilizado [+]Adição, [-]Subtração, [*]Multiplicação e [/]Divisão: ')
    sair = False
    valor1_float = 0
    valor2_float = 0
    valor_total = 0

    try:
        valor1_float = float(valor1_string)
        valor2_float = float(valor2_string)

        if operador_string == '+':
            valor_total = valor1_float + valor2_float 
            print(f'O valor da soma é: {valor_total}')

        elif operador_string == '-':
            valor_total = valor1_float - valor2_float
            print(f'O valor da subtração é: {valor_total}')

        elif operador_string == '*':
            valor_total = valor1_float * valor2_float
            print(f'O valor da multiplicação é: {valor_total}')

        elif operador_string == '/':
            valor_total = valor1_float / valor2_float
            print(f'O valor da soma é: {valor_total}')

        else:
            print('O operador não é reconhecido.')    
    except:
        print('O valor informado não é reconhecido como um número.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair == True:
        break