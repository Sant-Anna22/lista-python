import os

lista = []
while True:
    print ('O que deseja fazer com a sua lista? (Tenha em mente que sair exclui a lista.)')
    opcao = input ('[i]nserir; [a]pagar; [l]istar; [e]svaziar; [s]air: ').lower()

    if opcao == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        inserido = input ('Insira seu item: ')
        lista.append(inserido)
    elif opcao == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            apagar = input('Insira o índice que deseja apagar: ')
            apagar_int = int(apagar)
            del lista[apagar_int]
        except ValueError:
            print ('O índice tem que ser um número. Caso não saiba, verifique na lista o número ao lado do item.')
        except IndexError:
            print ('Esse índice não existe na sua lista.')
    elif opcao == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')
        for indice, item in enumerate(lista):
            print (indice, item)
    elif opcao == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Sua lista agora está vazia.')
        lista.clear()
    elif opcao == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Você saiu.')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Insira uma opção válida')