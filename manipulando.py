import os
import time


def my_arq():
    try:
        print("[+] Manipulando Diretorios Com Modulo OS[+]:\n[+]#Administrar Diretorios Arquivos E Pastas#[-]")#imprima esta mensagem

        opcao = input("Selecione Uma Opçao:\n(c) Criar[+]:\n(e) Eliminar[-]:\n(l) Ler Arquivo[+]:\n#:")#Entrada de string para uma escolha de uma determinada função --->
        if opcao == "c": #se opção for igual a 'c'
            rota = input("Informe o local onde pretende uliliazr: ")#entrada de string perguntando Qual diretorio pretende ultizar --->
            if rota == "": rota = os.getcwd() + "\\" #Informa o diretorio Atual --->
            if (os.path.isdir(rota)): #os.path.isdir para encaminhar aum determinado diretorio --->
                tipo = input("Indique a=arquivo ou P=pasta: ") #tipo de a = arquivo ou p = Pastaque deseja criar --->
                if(tipo == "a"): #se o tipo for igual a "a" --->
                    arquivo = input("Indique o nome do Arquivo: ") #entrada de string "indique o nome do arqivo"--->            
                    escreva = input("escreva algo:") #Escreva algo nesse arquivo --->
                    tempo1 = time.time() #coloquei o tempo pra calcular o tempo que o arquivo foi criado ---->
                    with open(rota+ arquivo, "w") as f: #abra o arquivo com a determinada rota informad aacima ,"w"= writeEscreva --->
                        f.write(escreva) #escreva Algo --->
                        start_time1 = time.time() - tempo1 #Calculando o tempo --->
                        f.close()#feche... --->
                        print("Arquvio",arquivo,"criado com sucesso: ")#prima Arquivo criado com sucesso ---->
                        print("Arquivo foi Criado Em %.2f Sgundos" % (start_time1))  #imprima o tempo em que o arquivo foi criado ---->
                elif tipo == "p": #seguindo a linha aacima se tipo for igual a "p" ---->
                    tempo = time.time() #para calcular o tempo ---->
                    pasta = input("Indique o nome da Pasta: ")#entrada de string informe o nome da pasta que deseja criar --->
                    os.mkdir(rota +pasta) #os.mkdir = abra uma apsta no determinado diretorio
                    start_tempo = time.time() - tempo #calculando o tempo--->
                    print("Pasta",carpeta,"criada com sucesso em %.2f Segundos" % (start_tempo))
                else: my_arq() #se não chame a função novamente como um "loop" --->
        elif opcao == "e": #seguindo a linha Acima da opção --->
            rota = input("Indique o diretorio caso contrario Diretorio Atual: ") #rota entrada de string informe o diretorio---->
            if rota == "": rota = os.getcwd() + "\\" #se a rota for " " = nada crie no ms diretorio
            apagar = input("Indique a pastA ou arquvo que deseja Apagar: ") #informe o arquivo ou pasta que deseja apagar apar = entrada de string --->
            if (os.path.isfile(rota +apagar)): #encaminhando ao diretorio --->
                 print("Arquvi",apagar,"eliminado com sucesso") #imprima arquivo "  " apagado com sucesso --->
            elif (os.path.isdir(rota +apagar)): #se nao --->
                os.rmdir(rota +apagar) #encaminhado ao diretorio ---->
                print("Pasta",apagar,"Eliminado Com sucesso: ") #imprima pasta " " apagada com sucesso ---->
            else: my_arq() #se não chame a função novamente --->
        elif opcao == 'l': #se opção for igual a 'l' --->
            info = input("informe o Arquvio que deseja Ler: ") #informe o arquivo que dejeja ler --->
            start = time.time() #calclulandp p tempo --->
            with open (info,"r") as f: #informe o arquivo que deseja ler --->
                for i in range(10): #gere o loop de 10 --->
                    x = f.readline() # x recebe f.leia em linha em linha --->
                    print(x) #imprima oq tem no arquivo --->
                    start_time = time.time() - start #calculando o tempo --->
                f.close() #feche --->
            print("Arquivofoi lido em %.2f Segundos" % (start_time))#imprimao tempo em que o arquivo foi lidop --->
            print("Arquivo ->",info,"Lido com Sucesso") #imprima arquivo foi lido com sucesso --->
            print(os.getcwd()) #mostre o diretorio atual --->
        else: my_arq() #se nao volte para função --->
    except KeyboardInterrupt as msg: #Exceto se o teclado interromper --->
        print(msg) #imprima a interrupção do teclado --->


if __name__ == '__main__':
    my_arq()