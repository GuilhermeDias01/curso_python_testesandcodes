# Exercício:

def multiplica_numeros(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
numeros = 5, 5, 5

total_multiplicacao = multiplica_numeros(*numeros)  
print(total_multiplicacao)

# Exercício 2:
def retorna_par_ou_impar(valor):
    if valor % 2 == 0:
        return 'PAR'
    return 'IMPAR'

valor = 1

converter = retorna_par_ou_impar(valor)
print(f'O valor informado é : {converter}')


# Exercício 2 > respota Professor:
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)


