import json
lista = []
def opcoes():
    while True:
        opcao = input('Digite uma opção: 1 add tarefa; 2 listar; 3 remover; 4 sair: ')
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefa()
        elif opcao == '3':
            remover_tarefa()
        elif opcao == '4':
            break    
        else:
            print('Opção invalida')        



def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista, arquivo)

def carregar_tarefas():
    global lista
    try:
        with open("tarefas.json", "r") as arquivo:
            lista = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        lista = []





def adicionar_tarefa():
    tarefa = input('Digite as tarefas que deseja adicionar: ')
    lista.append(tarefa)
    salvar_tarefas()

def listar_tarefa():
    if not lista:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(lista, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa():
    retirar_da_lista = input('Digite a tarefa que deseja remover: ')
    if retirar_da_lista in lista:
        lista.remove(retirar_da_lista)
        salvar_tarefas()
        print('Removido!')
    else:
        print('Tarefa não encontrada')

carregar_tarefas()
opcoes()