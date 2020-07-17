import os
import sys
import struct
import dbm

def create():


    print("\nBem-vindo ao seu programa de gerenciamento de estoque. \nComo é a primeira vez deste programa nesta máquina, preciso adicionar um usuário que tenha a posição de gerência na empresa.")
    while True:
        #trata os erros, caso o usuário crie uma interrupção
        try:
            user = input("\nDigite seu nome de usuário em até 20 letras ou, no mínimo, 3 letras: ")
            if(len(user) > 10 or len(user) < 3):
                print("\nPor favor, digite um usuário com, no máximo, 10 letras ou, no mínimo, 3 letras.")
            
            else:
                password = input("\nDigite sua senha em até 20 dígitos: ")
                if(len(password) > 20):
                    print("\nPor favor, digite uma senha com, no máximo, 20 dígitos.")
                else:
                    #como é a primeira vez, cria o banco de dados do usuário (user_db) e o de estoque (stock_db)
                    s = struct.Struct('10s 20s ?')
                    user_db = dbm.open("users.db", 'c')
                    stock_db = dbm.open("stock.db", 'c')
                    stock_db.close()
                    user_db['1'] = s.pack(user.encode(), password.encode(), True)
                    user_db.close()
                    break
        except (EOFError, KeyboardInterrupt):
            print("\nPor favor, digite uma entrada válida.")

create()