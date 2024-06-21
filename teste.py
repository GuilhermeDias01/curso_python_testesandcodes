

def retorna_par_ou_impar(valor):
    if valor % 2 == 0:
        return 'PAR'
    return 'IMPAR'

valor = 1

converter = retorna_par_ou_impar(valor)
print(f'O valor informado é : {converter}')