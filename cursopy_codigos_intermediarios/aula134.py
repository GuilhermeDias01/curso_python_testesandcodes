# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar'
import os

def listar_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa a listar.')
        print()
        return
    
    for tarefa in tarefas:
        print(f'{tarefa}')
    print()
    
def desfazer_tarefa(tarefas, tarefas_refazer):
    if not tarefas:
        print('Nenhuma tarefa a desfazer.')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer_tarefa(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa a refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adcionar(tarefa, tarefas):   
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    
    tarefas.append(tarefa)

    
tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: LISTAR, DESFAZER, REFAZER e LIMPAR ')
    tarefa = input('Digite um comando ou uma tarefa: ')
    print()

    tarefa = tarefa.upper()

    if tarefa == 'LISTAR':
        listar_tarefas(tarefas)

    elif tarefa == 'DESFAZER':
        desfazer_tarefa(tarefas, tarefas_refazer)

    elif tarefa == 'REFAZER':
        refazer_tarefa(tarefas, tarefas_refazer)

    elif tarefa == 'LIMPAR':
        os.system('CLS')
       
    else:
        adcionar(tarefa, tarefas)