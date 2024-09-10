# Exercício - Adiando execução de funções
from dados_package import soma, multiplica, criar_funcao

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)


print(soma_com_cinco(5))
print(multiplica_por_dez(20))