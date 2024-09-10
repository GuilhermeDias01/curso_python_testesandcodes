# Exercício:

# copy, sorted, produtos.sort

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

from dados_package import pprint, produtos

novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in copy.deepcopy(produtos)
]



# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'], reverse= True
)



# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco'],
)

print(produtos_ordenados_por_preco)