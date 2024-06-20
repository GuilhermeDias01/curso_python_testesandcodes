# Exercício:

lista = ['Maria', 'Helena', 'Luiz']
i = 0

for nome in lista:
    print(f'{i} {nome}')
    i += 1

print('----' * 10)

# Outra forma

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])