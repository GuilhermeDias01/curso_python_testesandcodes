import importlib

import aula109_m

print(aula109_m.variavel)

for i in range(10):
    importlib.reload(aula109_m)
    print(i)

print('Fim')