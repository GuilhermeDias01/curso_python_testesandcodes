""" while/else """
# Executa o Else somente quando o laço for finalizado pelo contador, caso seja forçado pelo break o else não será executado. 
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')