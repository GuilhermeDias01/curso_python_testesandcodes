"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


print('----' * 10)

lista_c= ['Luiz', 'Maria', 1, True, 1.2]
lista_d = lista_c

lista_c[0] = 'Qualquer coisa'
print(lista_c)
print(lista_d)