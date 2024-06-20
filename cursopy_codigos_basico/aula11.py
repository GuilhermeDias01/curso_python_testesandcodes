# Prescedência dos Operadores:
# Traduzindo, qual a ordem dos operadores que o Python segue:
# 1. (n+n)
# 2. **
# 3. *, /, // e %
# + e -

conta_1 = 1 + 1 ** 5 + 5   # 7
print(conta_1)

conta_1 = (1 + 1) ** (5 + 5)   # 1024
print(conta_1)