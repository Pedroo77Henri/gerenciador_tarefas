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

lista = []

def adicionar_tarefa():
    tarefa = input('Digite as tarefas que deseja adicionar: ')
    lista.append(tarefa)

def listar_tarefa():
    print(lista)

def remover_tarefa():
    retirar_da_lista = input('Digite a tarefa que deseja remover: ')
    if retirar_da_lista in lista:
        lista.remove(retirar_da_lista)
        print('Removido!')
    else:
        print('Tarefa não encontrada')

opcoes()