import os
import sys
import dbm
import struct

def main():
    
    #abre os bancos de dados
    global db
    global stock_db
    db = dbm.open('users.db', 'c')
    stock_db = dbm.open('stock.db', 'c')
    #verifica de o primeiro argumento passado está escrito se o usuário é um administrador ou não. 
    #Depois de verificar, manda para suas respectivas funções.
    if(sys.argv[1] == "administrator"):
        administrator(sys.argv[2])
    elif(sys.argv[1] == "employee"):
        employee(sys.argv[2])

#funções que trata a entrada do administrador
def administrator(func):
    
    #registra um novo usuário
    def new_user():
        
        while True:
            #trata o erro no caso de uma interrupção
            try:
                user = input("\nDigite um nome de usuário com até 10 letras: ")
                if(len(user) > 10 or len(user) < 3):
                    print("\nPor favor, digite um nome de usuário com, no máximo, 10 letras e, no mínimo, 3 letras.")
                else:
                    #É criado laços de repetição para que, caso aconteça um erro, o usuário possa repetir sua entrada de dado
                    #Se a entrada for identificada como verdadeira, passa para o próximo e, ao final, encerra o laço
                    while True:
                        password = input("\nDigite uma senha com até 20 dígitos: ")
                        if(len(password) > 20 or len(password) < 5):
                            print("\nPor favor, digite uma senha com, no máximo, 20 dígitos e, no mínimo, 5 letras.")
                        else:
                            while True:
                                adm = input("\nEste usuário é um gerente? Digite sim ou não: ")
                                if(adm.lower()[0] == 's'):
                                    s = struct.Struct('10s 20s ?')
                                    db[str(int(max(db.keys()))+1)] = s.pack(user.encode(), password.encode(), True)
                                    print("\nUsuário registrado com sucesso!")
                                    break
                                elif(adm.lower()[0] == 'n'):
                                    s = struct.Struct('10s 20s ?')
                                    db[str(int(max(db.keys()))+1)] = s.pack(user.encode(), password.encode(), False)
                                    print("\nUsuário registrado com sucesso!")
                                    break
                                else:
                                    print("\nDigite uma opção válida.")
                        break
            except (EOFError, KeyboardInterrupt):
            
                print("\nDigite uma opção válida.")
            break
    
    def delete_user():

        while True:
            try:
                identification = input("\nDigite o número de identificação do usuário ou aperte enter para sair: ")
                if(identification == '1'):
                    #não é possível remover o usuário 1 porque ele é o usuário supremo do sistema
                    print("\nNão é possível remover este usuário porque ele é o administrador de todo o sistema.")
                
                elif(identification == ""):
                    exi = input("\nTem certeza que deseja sair? Digite sim ou não: ")
                    if(exi.lower()[0] == 's'):
                        break
                    elif(exi.lower()[0] == 'n'):
                        continue
                    else:
                        print("\nDigite uma opção válida.")
                else:
                    try:
                        db.pop(identification)
                        print("\nUsuário removido com sucesso!")
                    except:
                        print("\nDigite o número de identificação corretamente.")
            except (EOFError, KeyboardInterrupt):
            
                print("\nDigite uma opção válida.")

    def user_list():
        
        #lista os usuários
        s = struct.Struct("10s 20s ?")
        print("\n\n==========LISTA DE USUÁRIOS==========")
        for i in db.keys():
            
            print("\n"+i.decode()+": "+s.unpack(db[i])[0].decode())
        print("\n=====================================")
        input("\nAperte enter para voltar ao menu inicial.\n\n")

    if(func == '1'):
        new_user()
    elif(func == '2'):
        delete_user()
    elif(func == '3'):
        user_list()
    elif(func == '4'):
        list_items()
    elif(func == '5'):
        add_item()
    elif(func == '6'):
        refresh_item()
    else:
        print("\nEscolha uma opção válida.")

#funções que trata a entrada do funcionário
def employee(func):
    if(func == '1'):
        list_items()
    elif(func == '2'):
        add_item()
    elif(func == '3'):
        refresh_item()
    else:
        print("\nEscolha uma opção válida.")

#lista os istens do estoque
def list_items():
    s = struct.Struct('20s f 3s ?')
    stock_db = dbm.open('stock.db', 'c')
    print("\n\n==========LISTA DE ITENS==========")
    for items in stock_db.keys():
        print("\n\n===============")
        #ferifica o quarto elemento da estrutura.
        #caso ele for True, ele está disponível
        if(s.unpack(stock_db[items])[3]):
            disp = "Sim"
        elif(s.unpack(stock_db[items])[3] == False):
            disp = "Não"

        print("ID: %s\nNome: %s\nPreço: %.2f\nCorredor: %s\nDisponível: %s"%(items.decode(), s.unpack(stock_db[items])[0].decode(),
        s.unpack(stock_db[items])[1], s.unpack(stock_db[items])[2].decode(), disp))
        print("===============")
    print("\n===================================")
    input("\nAperte enter para continuar")

#adiciona item ao estoque
def add_item():

    try:
        while True:
            procuct_name = input("\nDigite o nome do produto com até 20 letras: ")
            if(len(procuct_name) > 3):
                while True:
                    while True:
                        product_price = float(input("\nDigite o preço do produto (2.00, 30.00, etc): "))
                        #verifica se o valor do preço não possui outro caractere que não seja número
                        if(str(product_price).isalpha()):
                            print("\nPor favor, digite o preço corretamente.")
                        else:
                            while True:
                                procuct_hall = input("\nEm qual corredor está o produto? ")
                                if(len(product_price) < 1):
                                    print("\nDigite o corredor em que o produto se encontra.")
                                else:
                                    product_disp = input("\nO produto está disponível? ")

                                    if(product_disp.lower()[0] == 's'):
                                        #guarda no banco de daods do estoque
                                        product_disp = True 
                                        s = struct.Struct('20s f 3s ?')
                                        stock_db = dbm.open('stock.db', 'c')
                                        stock_db[str(len(stock_db))] = s.pack(procuct_name.encode(), product_price, procuct_hall.encode(), True)
                                        stock_db.close()

                                    elif(product_disp.lower()[0] == 'n'):
                                        
                                        product_disp = False
                                        s = struct.Struct('20s f 3s ?')
                                        stock_db = dbm.open('stock.db', 'c')
                                        stock_db[str(len(stock_db)+1)] = s.pack(procuct_name.encode(), product_price, procuct_hall.encode(), False)
                                        stock_db.close()

                                    else:
                                        print("\nPor favor, digite uma entrada válida.")
                                    break
                            break
                        break
                    break
                break
            else:
                print("\nO nome do produto deve ter mais que 3 letras.")

    except (EOFError, KeyboardInterrupt):
        print("\nPor favor, digite um valor válido.")

#atualiza os dados de um item no banco de dados do estoque

def refresh_data(identif):
    
    while True:
        try:
            choice = input("\nDigite o número da opção que deseja atualizar (ex: 2 para nome) ou aperte enter para sair: ")
            #um dicionário com as respectivas chaves de cada posição do elemento do db
            choice_keys = {'2': 0, '3': 1, '4': 2, '5': 3}
            #é criado um array auxiliar que guarda as informações da estrutura, já que não é possível alterar diretamente
            aux = []
            s = struct.Struct('20s f 3s ?')
            for keys in s.unpack(stock_db[identif.encode()]):
                aux.append(keys)
                #adiciona no array os dados da estrutura

            if(choice == ""):
                break
            elif(choice == '1'):
                print("\nO número de identificação não pode ser mudado.")
            elif(choice == '2'):

                while True:
                    aux_entry = input("\nDigite o novo nome: ").encode()
                    if(len(aux_entry) < 1 or len(aux_entry) >= 4):
                        print("\nO nome não pode estar vazio e deve ter, no mínimo, 4 letras.")
                    else:
                        break
                aux[choice_keys[choice]] = aux_entry

            elif(choice == '3'):

                aux_entry = float(input("\nDigite o novo preço: "))
                aux[choice_keys[choice]] = aux_entry

            elif(choice == '4'):
                
                while True:
                    aux_entry = input("\nDigite o corredor em que se encontra o produto: ").encode()
                    if(len(aux_entry) < 1 or len(aux_entry) >= 4):
                        print("\nO nome do corredor não pode estar vazio e deve ter, no máximo, 4 dígitos.")
                    else:
                        break
                aux[choice_keys[choice]] = aux_entry

            elif(choice == '5'):

                aux_aux = input("\nO produto ainda está disponível? ")
                if(aux_aux.lower()[0] == 's'):
                    aux[choice_keys[choice]] = True
                elif(aux_aux.lower()[0] == 'n'):
                    aux[choice_keys[choice]] = False    
                else:
                    print("\nDigite sim ou não.")
            else:
                print("\nDigite uma opção válida.")
            
            #ao final, ele guarda em uma nova estrutura cada item que foi guardado no array e limpa ele
            stock_db[identif.encode()] = s.pack(aux[0], aux[1], aux[2], aux[3])
            aux.clear()
        except (EOFError, KeyboardInterrupt):
            print("\nPor favor, digite uma entrada válida.")

#pega o id do produto que será mudado
def refresh_item():
    
    try:
        while True:
            identif = input("\nDigite o ID do produto ou aperte enter para sair: ")
            s = struct.Struct('20s f 3s ?')
            if(identif == ""):
                break
            elif(identif.encode() in stock_db.keys()):
                if(s.unpack(stock_db[identif.encode()])[3]):
                    disp = "Sim"
                    print("\n\n===============")
                    print("ID: %s\n2- Nome: %s\n3- Preço: %.2f\n4- Corredor: %s\n5- Disponível: %s"%(identif, s.unpack(stock_db[identif.encode()])[0].decode(), s.unpack(stock_db[identif.encode()])[1], s.unpack(stock_db[identif.encode()])[2].decode(), disp))
                    print("===============")
                    #manda o número de identificação do produto
                    refresh_data(identif)

                elif(s.unpack(stock_db[identif.encode()])[3] == False):
                    disp = "Não"
                    print("\n\n===============")
                    print("ID: %s\n2- Nome: %s\n3- Preço: %.2f\n4- Corredor: %s\n5- Disponível: %s"%(identif, s.unpack(stock_db[identif.encode()])[0].decode(), s.unpack(stock_db[identif.encode()])[1], s.unpack(stock_db[identif.encode()])[2].decode(), disp))
                    print("===============")
                    refresh_data(identif)
            else:
                    print("\nID não encontrado.")
    except:
        print("\nPor favor, digite uma entrada válida.")
    

main()