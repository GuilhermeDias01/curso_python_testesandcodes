# importando os módulos através do arquivo __init__.py 

# esse aquivo praticamente diz ao python que o package é um modulo, fazendo
# com que as chamadas sejam feitas diretas do package


from aula110_package import soma_do_modulo, fala_oi

print(soma_do_modulo(2, 3))
fala_oi()
