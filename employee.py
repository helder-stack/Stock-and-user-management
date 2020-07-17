import os
import sys
def main():
    #pega o argumento passado, ou seja, o nome do usuário.
    print("\nBem-vindo, %s!"%(sys.argv[1]))
    print("\nAqui estão as funcionalidades do sistema:")
    while True:  
        #mostra as funcionalidades do sistema e envia a opção escolhida como argumento para o programa func.py
        print("\n1- Ver itens no estoque\n2- Adicionar item ao estoque\n3- Atualizar item no estoque\n4- Sair")
        try:
            func = int(input("\nDigite uma opção: "))
            if(func == 4):
                print("\nObrigado por usar nosso sistema!")
                sys.exit()
            
            else:
                os.system("python func.py employee %i"%(func))

        except (EOFError, KeyboardInterrupt):
            print("\nDigite uma opção válida.")

main()