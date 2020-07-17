import os
import sys
import struct
import dbm

#cria uma classe sobre o usuário. Guardando seu usuário e a verificação se ele é um administrador ou não.
class user(object):

    def __init__(self):
        self.__user = ""
        self.isAdm = False
    def setUsers(self, username):
        self.__user = username
    def getUser(self):
        return self.__user
    def getAdmStatus(self):
        return self.isAdm

def main():
    """
        verifica se os arquivos de banco de dados existem. 
        Caso não existirem, significa que é a primeira vez que o programa está rodando na máquina e é mandado para
        o arquivo create_db.py, que criará o banco de dados com a inclusão de um funcionário gerente para que, futuramente,
        possa adicionar outros membros.
    """
    if(file_verify()):
        
        global db
        s = struct.Struct('10s 20s ?')
        db = dbm.open('users.db', 'c')
        #trata o erro no caso de uma interrupção
        try:
            User_found = False
            identification = input("\nDigite seu número de identificação: ")
            for users in db.keys():
                if(identification == users.decode()): #Procura o ID em db
                    #se o usuário for encontrado, ele seta a variável para True
                    User_found = True
                    
                    password = input("\nSenha: ")
                    #caso a senha esteja correta, ele manda usuário e se o user é admin ou não para a classe user
                    #depois chama a função run
                    #.replace("\x00", "") --> Serve para remover os espaços que são ocupados pelos caracters que faltam no limite de caracteres
                    if(password == s.unpack(db[users.decode()])[1].decode().replace("\x00", "")):
                        user_info.setUsers(s.unpack(db[users])[0].decode().replace("\x00", ""))
                        user_info.isAdm = s.unpack(db[users.decode()])[2]
                        run()   
                        break   
                    else:
                        print("\nA senha está incorreta.")  
                    

            if(User_found == False):
                print("\nUsuário não encontrado")

        except (EOFError, KeyboardInterrupt):
            print("\nPor favor, digite uma entrada válida.")
        #verifica se o usuário existe no banco de dados
    else:
        os.system("python create_db.py")
        
def run():
    
    #verifica se o usuário é um admnistrador.
    #caso for um adm, chama o programa administrator.py e manda como argumento seu nome de usuário.
    if(user_info.getAdmStatus()):

        os.system("python administrator.py %s"%(user_info.getUser()))
    #se for um funcionário, chama o programa employee.py e manda como argumento seu nome de usuário.
    else:
        
        os.system("python employee.py %s"%(user_info.getUser()))
    while True:
        try:
            exi = input("\nDigite 1 para fechar o programa ou 2 para voltar para o login: ")
            if(exi == '1'):
                sys.exit()
                db.close()
                break
            elif(exi == '2'):
                break
            else:
                print("\nDigite uma opção válida.")
        except (EOFError, KeyboardInterrupt):
            
            print("\nDigite uma opção válida.")

def file_verify():
    if("users.db.dir" in os.listdir()):
        return True
    else:
        return False


user_info = user()

if __name__ == '__main__'   :
    print("\nBem-vindo! Por favor, entre com suas credenciais abaixo.")
    while True:
        main()

#DOCUMENTAR O CÓDIGO

#func