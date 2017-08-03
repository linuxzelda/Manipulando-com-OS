import os
import time




def my_arq():
    try:
        
        print("[+] Manipulando Diretorios Com Modulo OS[+]:\n[+]#Administrar Diretorios Arquivos E Pastas#[-]")    #imprima esta mensagem
        opcao = input("Selecione Uma Opçao:\n(c) Criar[+]:\n(e) Eliminar[-]:\n(l) Ler Arquivo[+]:\n#:")          #Entrada de string para uma escolha de uma determinada função --->
        if opcao == "c":                                                                              #se opção for igual a 'c'
            rota = input("Informe o local onde pretende Ultilizar: ")              #entrada de string perguntando Qual diretorio pretende ultizar --->
            if rota == "": rota = os.getcwd() + "\\"                         #Informa o diretorio Atual --->
            if (os.path.isdir(rota)):                                   #os.path.isdir para encaminhar aum determinado diretorio --->
                tipo = input("Escolha uma Opcao:\n(a) = Arquivo:\n(p) = Pasta: ")             #tipo de a = arquivo ou p = Pastaque deseja criar --->
                if(tipo == "a"):                                                         #se o tipo for igual a "a" --->
                    arquivo = input("Indique o nome do Arquivo: ")         #entrada de string "indique o nome do arqivo"--->            
                    escreva = input("Escreva algo:\n#:")     #Escreva algo nesse arquivo --->
                    tempo1 = time.time()                  #coloquei o tempo pra calcular o tempo que o arquivo foi criado ---->
                    with open(rota+ arquivo, "w") as f:       #abra o arquivo com a determinada rota informad aacima ,"w"= writeEscreva --->
                        f.write(escreva)                        #escreva Algo --->
                        start_time1 = time.time() - tempo1             #Calculando o tempo --->
                        f.close()                                          #feche... --->
                        print("Arquvio",arquivo,"criado com sucesso: ")     #prima Arquivo criado com sucesso ---->
                        print("Arquivo foi Criado Em %.2f Sgundos" % (start_time1))  #imprima o tempo em que o arquivo foi criado ---->
                elif tipo == "p":                                         #seguindo a linha aacima se tipo for igual a "p" ---->
                    tempo = time.time()                             #para calcular o tempo ---->
                    pasta = input("Indique o nome da Pasta:\n#:")       #entrada de string informe o nome da pasta que deseja criar --->
                    os.mkdir(rota +pasta)                       #os.mkdir = abra uma apsta no determinado diretorio
                    start_tempo = time.time() - tempo          #calculando o tempo--->
                    print("Pasta",pasta,"criada com sucesso em %.2f Segundos" % (start_tempo))
                else: my_arq()                        #se não chame a função novamente como um "loop" --->
        elif opcao == "e":                             #seguindo a linha Acima da opção --->
            eliminar_arq() 
        elif opcao == 'l':
            ler_arq()
    except KeyboardInterrupt as msg:                #Exceto se o teclado interromper --->()
        print(msg)                                 #imprima a interrupção do teclado --->()


def eliminar_arq():
    try:

        while True:

            rota1 = input("Informe O Diretorio, Caso Contrario Diretorio Atual:\n#: ")
            if rota1 == "": os.getcwd() + "\\"
            apagar1 = input("Informe O Nome Da 'Pasta' Ou 'Arquivo' que deseja Apagar:\n#: ")
            if os.path.isfile(rota1 +apagar1):
                print("Arquivo-->",apagar1,"Excluido Com Sucesso: ")
            elif (os.path.isdir(rota1 +apagar1)):
                os.rmdir(rota1 +apagar1)
                print("Pasta",apagar1,"Excluida Com Sucesso: ")
            opcao1 = int(input("(1) Continuar[+]:\n(2) Sair[-]:\n(3)Voltar ao principal[M]:\n#: "))
            if opcao1 == 1:
                eliminar_arq()
            elif opcao1 == 2:
                break
            elif opcao1 == 3:
                my_arq()

    except KeyboardInterrupt as msg:
        print(msg)


def ler_arq():
    try:

        while True:

            info = input("Informe o Arquivo Que Deseja Ler:\n#: ")
            start = time.time()
            with open (info,"r") as f:
                for i in range(10):
                    x = f.readline()
                    print(x)
                    start_time = time.time() - start
                f.close()
            print("Arquivo Foi lido em %.2f Segundos:" % (start_time))
            print("Arquvio:",info,"Lido com sucesso: ")
            opcao2 = int(input("(1) Continuar[+]:\n(2) Sair[-]:\n(3) Voltar ao Principal[M]:\n#: "))
            if opcao2 == 1:
                ler_arq()
            elif opcao2 == 2:
                break
            elif opcao2 == 3:
                my_arq()

    except KeyboardInterrupt as msg:
        print(msg)

if __name__ == '__main__':
    my_arq()
