# Exercício:

numero = float(input('Digite um numero: '))

def duplicar_numero (numero):
    print(f'O número duplicado é {numero * 2}')
    def triplicar_numero (numero):
        print(f'O número triplicado é {numero * 3}')
        def quaduplicar_numero (numero):
            print(f'O número quaduplicado é {numero * 4}')
        return quaduplicar_numero(numero)
    return triplicar_numero(numero)

duplicar_numero(numero)


# Exercício - Resposta professor: 

def criar_mutiplicador (multiplicador):
    def multiplicar (numero):
        return numero * multiplicador
    return multiplicar
        
duplicar = criar_mutiplicador(2)
triplicar = criar_mutiplicador(3)
quadruplicar = criar_mutiplicador(4)

print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))