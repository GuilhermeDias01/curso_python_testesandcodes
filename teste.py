def soma (x, y):
    return x + y

def chama_funcao(func, x):
    def interna(y):
        return func(x,y)
    return interna

soma_10 = chama_funcao(soma,10)
print(soma_10(20))


def soma_20(y):
    x = 20
    return x+y

print(soma_20(30))