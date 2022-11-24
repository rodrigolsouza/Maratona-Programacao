 class nodo():
    
    def __init__(self, dado, pai, fe, fd, cor = "vermelho"):
        
        self.__dado = dado
        self.__pai = pai
        self.__fe = fe
        self.__fd = fd
        self.__cor = cor 
        
    def getdado(self):
        return self.__dado
    def setdado (self, dado):
        self.__dado = dado

    def getpai (self):
        return self.__pai
    def setpai(self, pai):
        self.__pai = pai

    def getfilhoesquerdo(self):
        return self.__fe
    def setfilhoesquerdo(self, fe):
        self.__fe = fe

    def getfilhodireito(self):
        return self.__fd
    def setfilhodireito(self, fd):
        self.__fd = fd

    def getcor(self):
        return self.__cor
    def setcor(self, cor):
        self.__cor = cor

    def __str__(self):
        if self.__dado == None:
           return "None"
        else:
           return str(self.getdado())


class arvore():

    def __init__(self):

        
        self.__raiz=nulo
        

    def getraiz(self):
        return self.__raiz

    def setraiz(self, raiz):
        self.__raiz=raiz

       
    def verarvorecompleta(self, x):

        if x != nulo:
            self.verarvorecompleta(x.getfilhoesquerdo())
            print(x.getdado().getnumero(),x.getcor())
            if x.getfilhodireito()!=nulo:
                print("FD ->", + x.getfilhodireito().getdado().getnumero(), x.getfilhodireito().getcor())
            if x.getfilhoesquerdo()!=nulo:
                print("FE ->", + x.getfilhoesquerdo().getdado().getnumero(), x.getfilhoesquerdo().getcor())         
            self.verarvorecompleta(x.getfilhodireito())

    def buscarno(self, x, nodo):
    
        if x==nulo or x.getdado().getnumero()==nodo:
            return x
        if nodo < x.getdado().getnumero():
            x=x.getfilhoesquerdo()
            return self.buscarno(x,nodo)
        else:
            x=x.getfilhodireito()
            return self.buscarno(x,nodo)


            
    def minimo(self, x):  
        while x.getfilhoesquerdo() != nulo:
            x = x.getfilhoesquerdo()
        return x
        
    def maximo(self, x):
        while x.getfilhodireito() != nulo:
            x =  x.getfilhodireito()
        return x


    def sucessor(self, x):
        if x.getfilhodireito() != nulo:
            return self.minimo(x.getfilhodireito())
        y = x.getpai()
        while y != nulo and x == y.getfilhodireito():
            x = y
            y = y.getpai()
        return y
    
    def predecessor(self, x): 
        if x.getfilhoesquerdo() != nulo:
            return self.maximo(x.getfilhoesquerdo())

        elif x.getfilhoesquerdo()==nulo and x.getpai()!=nulo and x.getpai().getpai()!=nulo:
            return x.getpai().getpai().getdado().getnumero()
        else:
            print ("titulo não existe")

    def rotacaoesquerda(self, nodo): 
        
        y =nodo.getfilhodireito()
        nodo.setfilhodireito(y.getfilhoesquerdo()) 

        if y.getfilhoesquerdo()!=nulo:
            y.getfilhoesquerdo().setpai(nodo)

        y.setpai(nodo.getpai()) 

        if nodo.getpai()==nulo:
            self.setraiz(y)
        else:
            if nodo==nodo.getpai().getfilhoesquerdo():
                nodo.getpai().setfilhoesquerdo(y)
            else:
                nodo.getpai().setfilhodireito(y)
        y.setfilhoesquerdo(nodo)   
        nodo.setpai(y)

    def rotacaodireita(self, nodo):
        
        y =nodo.getfilhoesquerdo()
        nodo.setfilhoesquerdo(y.getfilhodireito()) 

        if y.getfilhodireito()!=nulo:
        
            y.getfilhodireito().setpai(nodo)

        y.setpai(nodo.getpai()) 

        if nodo.getpai()==nulo:
            
            self.setraiz(y)
        else:
            if nodo==nodo.getpai().getfilhodireito():
                nodo.getpai().setfilhodireito(y)
            else:
                nodo.getpai().setfilhoesquerdo(y)
        y.setfilhodireito(nodo)
        nodo.setpai(y)

    def ajustedoinserir(self, novonodo):        

        while novonodo.getpai().getcor()=="vermelho":
            if novonodo.getpai() == novonodo.getpai().getpai().getfilhoesquerdo():
                y=novonodo.getpai().getpai().getfilhodireito()
                if y.getcor()=="vermelho":
                    novonodo.getpai().setcor("preto")
                    y.setcor("preto")
                    novonodo.getpai().getpai().setcor("vermelho")
                    novonodo=novonodo.getpai().getpai()
                else:
                    if novonodo == novonodo.getpai().getfilhodireito():
                        novonodo=novonodo.getpai()
                        self.rotacaoesquerda(novonodo)
                    novonodo.getpai().setcor("preto")
                    novonodo.getpai().getpai().setcor("vermelho")
                    self.rotacaodireita(novonodo.getpai().getpai())


            else:
                y=novonodo.getpai().getpai().getfilhoesquerdo()
                if y.getcor()=="vermelho":
                    novonodo.getpai().setcor("preto")
                    y.setcor("preto")
                    novonodo.getpai().getpai().setcor("vermelho")
                    novonodo=novonodo.getpai().getpai()
                else:
                    if novonodo == novonodo.getpai().getfilhoesquerdo():
                        novonodo=novonodo.getpai()
                        self.rotacaodireita(novonodo)
                    novonodo.getpai().setcor("preto")
                    novonodo.getpai().getpai().setcor("vermelho")
                    self.rotacaoesquerda(novonodo.getpai().getpai())
        self.getraiz().setcor("preto")

    def inserirnodo(self, novonodo):
        
        y = nulo
        x = self.getraiz()
        while x != nulo:
            y = x            
            if novonodo.getdado().getnumero() < x.getdado().getnumero():
                x = x.getfilhoesquerdo()
            else:
                x = x.getfilhodireito()
        novonodo.setpai(y)
        if y == nulo:
            self.setraiz(novonodo)
        else:
            if  novonodo.getdado().getnumero() < y.getdado().getnumero():
                y.setfilhoesquerdo(novonodo)
            else:
                y.setfilhodireito(novonodo)
        novonodo.setfilhodireito(nulo)
        novonodo.setfilhoesquerdo(nulo)
        novonodo.setcor("vermelho")
        self.ajustedoinserir(novonodo)

    def ajustedodeletar(self, nodo):

        while nodo != self.getraiz() and nodo.getcor()=="preto":
            if nodo==nodo.getpai().getfilhoesquerdo():
                w=nodo.getpai().getfilhodireito()
                if w.getcor()=="vermelho":
                    w.setcor("preto")
                    nodo.getpai().setcor("vermelho")
                    self.rotacaoesquerda(nodo.getpai())
                    w=nodo.getpai().getfilhodireito()

                if w.getfilhoesquerdo().getcor()=="preto" and w.getfilhodireito().getcor()=="preto":
                    w.setcor("vermelho")
                    nodo=nodo.getpai()
                else:
                    if w.getfilhodireito().getcor()=="preto":
                        w.getfilhoesquerdo().setcor("preto")
                        w.setcor("vermelho")
                        self.rotacaodireita(w)
                        w=nodo.getpai().getfilhodireito()
                    w.setcor(nodo.getpai().getcor())
                    nodo.getpai().setcor("preto")
                    w.getfilhodireito().setcor("preto")
                    self.rotacaoesquerda(nodo.getpai())
                    nodo=self.getraiz()

            else:
                w=nodo.getpai().getfilhoesquerdo()
                if w.getcor()=="vermelho":
                    w.setcor("preto")
                    nodo.getpai().setcor("vermelho")
                    self.rotacaodireita(nodo.getpai())
                    w=nodo.getpai().getfilhoesquerdo()

                if w.getfilhodireito().getcor()=="preto" and w.getfilhoesquerdo().getcor()=="preto":
                    w.setcor("vermelho")
                    nodo=nodo.getpai()
                else:
                    if w.getfilhoesquerdo().getcor()=="preto":
                        w.getfilhodireito().setcor("preto")
                        w.setcor("vermelho")
                        self.rotacaoesquerda(w)
                        w=nodo.getpai().getfilhoesquerdo()
                    w.setcor(nodo.getpai().getcor())
                    nodo.getpai().setcor("preto")
                    w.getfilhoesquerdo().setcor("preto")
                    self.rotacaodireita(nodo.getpai())
                    nodo=self.getraiz()




    def deletarnodo(self, nodo):

        if nodo.getfilhoesquerdo()==nulo or nodo.getfilhodireito()==nulo:
            y=nodo
        else:
            y=self.sucessor(nodo)

        if y.getfilhoesquerdo()!=nulo:
            x=y.getfilhoesquerdo()
        else:
            x=y.getfilhodireito()
        x.setpai(y.getpai())

        if y.getpai()==nulo:
            self.setraiz(x)
        else:
            if y==y.getpai().getfilhoesquerdo():
                y.getpai().setfilhoesquerdo(x)

            else:
                y.getpai().setfilhodireito(x)

        if y != nodo:
            nodo.setdado(y.getdado())

        if y.getcor()=="preto":
            self.ajustedodeletar(nodo)

        return y.getdado().getnumero()

nulo=nodo(None, None, None, None, cor = "preto")
nulo.setfilhodireito(nulo)
nulo.setfilhoesquerdo(nulo)
nulo.setpai(nulo)
"""
arvore = arvore()
class eleitores():

    def __init__(self, nome, titulo):

        self.__nome=nome
        self.__titulo=titulo

    def getnumero(self):

        return self.__titulo

    def getnome(self):

        return self.__nome

        
dado = eleitores('daivid', 15)
no = nodo(dado, nulo, nulo, nulo)
dado = eleitores('daivid', 10)
no2 = nodo(dado, nulo, nulo, nulo)
dado = eleitores('daivid', 5)
no3 = nodo(dado, nulo, nulo, nulo)
dado = eleitores('daivid', 4)
no4 = nodo(dado, nulo, nulo, nulo)
dado = eleitores('daivid', 2)
no5 = nodo(dado, nulo, nulo, nulo)

arvore.inserirnodo(no)
arvore.inserirnodo(no2)
arvore.inserirnodo(no3)
arvore.inserirnodo(no4)
arvore.inserirnodo(no5)"""