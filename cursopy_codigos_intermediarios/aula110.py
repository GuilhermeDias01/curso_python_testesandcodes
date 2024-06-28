# formas de import para package and modulos

from sys import path

#1
import aula110_package.modulo
#2
from aula110_package.modulo import soma_do_modulo
#3
from aula110_package import modulo
#4 para funcionar no import all, as variaveis devem ser adcionadas no __all__= []
from aula110_package.modulo import *

#1
print(aula110_package.modulo.soma_do_modulo(1, 2))
#2
print(soma_do_modulo(1, 2))
#3
print(modulo.soma_do_modulo(1,2))
#4
print(soma_do_modulo(1, 2))
#4
print(variavel)
#4
print(nova_variavel)