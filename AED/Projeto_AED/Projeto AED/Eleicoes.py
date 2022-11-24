
from arvore import *
from random import randint


naovotou=arvore()
votou=arvore()
candidatos=arvore()
id_votar="votar"


class eleitores():

        def __init__(self, nome, titulo):

                self.__nome=nome
                self.__titulo=titulo

        def getnumero(self):

                return self.__titulo

        def getnome(self):

                return self.__nome

        

class candidato():

        def __init__(self, nome, numero):

                self.__nome=nome
                self.__numero=numero
                self.__qtdvotos=0

        def getnome(self):
                return self.__nome


        def getnumero(self):

                return self.__numero

        def setqtdvotos(self):

                self.__qtdvotos+=1

        def getqtdvotos(self):

                return self.__qtdvotos

                

def cadastrareleitor(nome, titulo):
        
        x=eleitores(nome,titulo)
        no=nodo(x, nulo, nulo, nulo)
        if naovotou.buscarno(naovotou.getraiz(), titulo)!=nulo:
                print ("Eleitor ja foi cadastrado.")
        else:
                naovotou.inserirnodo(no)

def removereleitor(titulo):
        no=naovotou.buscarno(naovotou.getraiz(), titulo)
        if no!=nulo:
                naovotou.deletarnodo(no)
                print ("Titulo removido com sucesso.")
        else:
                print ("Titulo nao existe.")


def cadastrarcandidato(nome, numero):

        x=candidato(nome,numero)
        no=nodo(x, nulo, nulo, nulo)
        if candidatos.buscarno(candidatos.getraiz(), numero)!=nulo:
                print ("Candidato ja foi cadastrado.")
        else:
                candidatos.inserirnodo(no)


def cadastrarvotou(nome,numero):

        eleitor=eleitores(nome,numero)
        no=nodo(eleitor, nulo,nulo,nulo)
        if votou.buscarno(votou.getraiz(), numero)!=nulo:
                print ("Candidato ja votou.")
        else:
                votou.inserirnodo(no)
        

def verificartitulo(titulo):
        if votou.buscarno(votou.getraiz(), titulo)!=nulo:

                return True

        elif votou.buscarno(votou.getraiz(), titulo)==nulo and naovotou.buscarno(naovotou.getraiz(), titulo)==nulo:

                return False

        elif votou.buscarno(votou.getraiz(), titulo)==nulo and naovotou.buscarno(naovotou.getraiz(), titulo)!=nulo:

                return id_votar
        


def votar(titulo, numero):

         #define variavel para add e rem das arvores
        candidatoX=candidatos.buscarno(candidatos.getraiz(), numero)
        candidatoX.getdado().setqtdvotos()  #define variavel para alterar na arvore
        nome=naovotou.buscarno(naovotou.getraiz(),titulo).getdado().getnome()
        numero=naovotou.buscarno(naovotou.getraiz(),titulo).getdado().getnumero()
        naovotou.deletarnodo(naovotou.buscarno(naovotou.getraiz(),titulo))
        cadastrarvotou(nome,numero)
        
        

        

def gerarvotosA():

        
        while naovotou.getraiz()!=nulo:
                x=randint(1,conta)
                candidatoX=candidatos.buscarno(candidatos.getraiz(), x)
                candidatoX.getdado().setqtdvotos()  #define variavel para alterar na arvore
                nome=naovotou.getraiz().getdado().getnome()
                numero=naovotou.getraiz().getdado().getnumero()
                naovotou.deletarnodo(naovotou.getraiz())
                eleitor=eleitores(nome,numero)
                no=nodo(eleitor, nulo,nulo,nulo)
                votou.inserirnodo(no)

def resultado():
        lista=[]
        aux=candidatos.minimo(candidatos.getraiz())
        x=aux
        while aux!=nulo:
                a,b = aux.getdado().getqtdvotos(), aux.getdado().getnome()
                lista.append((a,b)) 
                aux=candidatos.sucessor(aux)                   
        lista.sort(reverse = True)
        return lista

def maisvotado():
        aux=candidatos.minimo(candidatos.getraiz())
        x=aux
        while aux!=nulo:
                aux=candidatos.sucessor(aux)
                if aux!=nulo:
                        if x.getdado().getqtdvotos() < aux.getdado().getqtdvotos():
                                x=aux
        return x.getdado().getnome() + ' -> ' + str(x.getdado().getqtdvotos())
        
def reset():

        del naovotou
        del votou
        del candidatos
        global candidatos
        global votou
        global naovotou
        naovotou = arvore()
        votou = arvore()
        candidatos = arvore()


def gerararvoreE(qtd):

        for i in range(1,qtd+1):
                cadastrareleitor("Eleitor "+str(i), i)

def gerararvoreC(qtd):

        global conta
        conta = qtd
        for i in range(1,qtd+1):
                cadastrarcandidato("Candidato "+str(i), i)
