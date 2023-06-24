# -*- coding: ISO-8859-1 -*-
import _thread
import time, random
import threading
from time import sleep
from threading import Thread

N = 5 #inicialização da variavel
PENSAR = 0#inicialização da variavel
FOME = 1#inicialização da variavel
COMER = 2#inicialização da variavel
#usando mutex
mutex = threading.Semaphore(1)#inicialização da variavel
S = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0)]  # inicializacao do semáforo de cada filósofo
estado = [PENSAR, PENSAR, PENSAR, PENSAR, PENSAR]#inicialização do array

#imprimir o estado dos filosfosos
def imprimir():
    print("ESTADO DOS FILOSOFOS  " + str(estado))

#nomes dos filosofos
filosofos = ["Mario", "Karnal", "Marilene Chaui'","Ponde","Divalte"]
#cor de identifica de cada filosofo
def corFilosofo(dado,id):
    if(id==0):
        print(f'\033[0;34;34m {filosofos[id]} esta {dado} \033[m')
    elif(id==1):
        print(f'\033[0;37;37m {filosofos[id]} esta {dado} \033[m')
    elif (id == 2):
        print(f'\033[0;35;35m {filosofos[id]} esta {dado} \033[m')
    elif (id == 3):
        print(f'\033[2;0;31m \033{filosofos[id]} esta {dado} \033[m')
    else:
        print(f'\033[0;0;40m {filosofos[id]} esta {dado} \033[m')



#busca o indice a esquerda
def buscarEsquerdo(i,N):
    return (i+N-1)%N
#busca o indice a direita
def buscarDireito(i,N):
    return (i+1)%N

#metodo que imprimi o filofoso da esquerda, o filosofo que esta pensando, e o filosofo a direita
def think(nfilosofo):
    print(f" vizinho esquerdo {filosofos[buscarEsquerdo(nfilosofo,5)]} <{buscarEsquerdo(nfilosofo,5)+1}> \033[0;45;45m === Filosofo {filosofos[nfilosofo]} {nfilosofo+1} esta pensando === \033[m filoso direito {filosofos[buscarDireito(nfilosofo,5)]} <{buscarDireito(nfilosofo,5)+1}> \n")
    #corFilosofo("Pensando", nfilosofo)

# Implementar
#metodo que imprimi o filofoso da esquerda, o filosofo que esta comendo, e o filosofo a direita
def eat(nfilosofo):
    print(f" vizinho esquerdo {filosofos[buscarEsquerdo(nfilosofo,5)]} {buscarEsquerdo(nfilosofo,5)+1} \033[0;47;42m === Filosofo {filosofos[nfilosofo]} {nfilosofo+1} esta comendo === \033[m filoso direito {filosofos[buscarDireito(nfilosofo,5)]} <{buscarDireito(nfilosofo,5)+1} >\n")

# Implementar

#filosofo que agarra o garfo
# metodo que tambem entra na regiao critica
# metodo que imprime qie p filosoofo esta com fome
def agarraGarfo(nfilosofo):

    mutex.acquire()
    estado[nfilosofo]=FOME
    print(f" vizinho esquerdo {filosofos[buscarEsquerdo(nfilosofo, 5)]} < {buscarEsquerdo(nfilosofo, 5) + 1}> \033[0;45;41m === Filosofo {filosofos[nfilosofo]} {nfilosofo + 1} esta com fome === \033[m filoso direito {filosofos[buscarDireito(nfilosofo, 5)]} <{buscarDireito(nfilosofo, 5) + 1}> \n")

    testar1(nfilosofo)

    mutex.release()
    S[nfilosofo].acquire()



# Implementar
#filosofo entra na refiao critica
# o filosofo deixa o garfo e passa para o esquerdo e direito os garfos
def deixaGarfo(nfilosofo):
    mutex.acquire()
    estado[nfilosofo] = PENSAR
    testar(buscarEsquerdo(nfilosofo, 5),"esquerdo")
    testar(buscarDireito(nfilosofo, 5),"direito")

    mutex.release()
    S[nfilosofo].acquire()
# Implementar

#metodo que pega verifica se o filosofo da esquerda ou direita estao comendo e se o filosfo em questao esta com fome
#se o direito e  esquerdo nao estiverem comendo, o filosofo passa para o estado comer
# imprime que o filosofo pegou os garfos do direito e esquerdo
def testar1(nfilosofo):
    global N
    if(estado[nfilosofo]==FOME and estado[buscarEsquerdo(nfilosofo,N)] != COMER and estado[buscarDireito(nfilosofo,N)]!= COMER):
        estado[nfilosofo] = COMER
        print(f"Filosofo {nfilosofo} {filosofos[nfilosofo]} , pega garfo Direito e esquerdo \n")
        S[nfilosofo].release()
#metodo que pega verifica se o filosofo da esquerda ou direita estao comendo e se o filosfo em questao esta com fome
#se o direito e  esquerdo nao estiverem comendo, o filosofo passa para o estado comer
# imprime o filosofo em questao passando o garfo pro seu vizinho
def testar(nfilosofo,dados):
    global N
    if (dados == "esquerdo"):
        print(
            f"Filosofos {filosofos[buscarDireito(nfilosofo, N)]} {buscarDireito(nfilosofo, N)+1} deixa o garfo esquerdo e passa para {filosofos[nfilosofo]} {nfilosofo+1}  \n")

    elif (dados == "direito"):
        print(
            f"Filosofos {filosofos[buscarEsquerdo(nfilosofo, N)]} {buscarEsquerdo(nfilosofo, N)+1} deixa o garfo direito e passa para {filosofos[nfilosofo]} {nfilosofo+1}  \n")


    if(estado[nfilosofo]==FOME and estado[buscarEsquerdo(nfilosofo,N)] != COMER and estado[buscarDireito(nfilosofo,N)]!= COMER):
        estado[nfilosofo] = COMER
        dado1 = dados
        print(dado1)
        S[nfilosofo].release()


def filosofo(i):
    while(True):

        think(i)#filosofo pensando
        agarraGarfo(i)#pegar dois garfos ou bloqueia
        eat(i)#hummm sopa

        deixaGarfo(i)#devolver garfos :D

if __name__ == '__main__':
    #imprimir um manual
    print("JANTAR DOS FILOSOFOS BRASILEIROS")
    print("COR VERDE = O FILOSOFO ESTA COMENDO \n COR ROXA = O FILOSOFO ESTA PENSANDO \n COR VERMELHA = O FILOSOFO ESTA COM FOME")
    print("O numero é  identificação dos filósofos ")
    print("\n ")

    count=0#inicialização da variavel
    # o while indica quantas vezes o filosofo vai comer, no caso, 1 vez
    while(count<1):
        for i in range(5):# criando 5 filosofos
            filo=Thread(target=filosofo,args=[i])#criando a thread
            filo.start()#startando a thread

        count=count+1 #incrementar a variavel



