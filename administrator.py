import os
import sys
def main():
    #pega o argumento passado, ou seja, o nome do usuário.
    print("\nBem-vindo, %s!"%(sys.argv[1]))
    print("\nAqui estão as funcionalidades do sistema:")
    while True:
        try:
            #mostra as funcionalidades do sistema e envia a opção escolhida como argumento para o programa func.py
            print("\n1- Registrar um novo usuário\n2- Excluir um usuário\n3- Ver lista de usuários\n4- Ver itens no estoque\n5- Adicionar item ao estoque\n6- Atualizar item no estoque\n7- Sair")
            func = int(input("\nDigite uma opção: "))
            if(func == 7):
                print("\nObrigado por usar nosso sistema!")
                sys.exit()
            else:
                os.system("python func.py administrator %i"%(func))
        except (EOFError, KeyboardInterrupt):
            print("\nDigite uma opção válida.")

main()