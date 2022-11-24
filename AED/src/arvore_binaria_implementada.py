class No():
    
    def __init__(self, dado=None, pai=None, esq=None, direito=None):
        self._dado = dado
        self._pai = pai
        self._filho_direito = direito
        self._filho_esquerdo = esq
    
    def getDado(self):
        return self._dado
    
    def setDado(self, dado):
        self._dado = dado
        
        
    
    def getPai(self):
        return self._pai
    
    def setPai(self, dado):
        self._pai = dado
        
        
    
    def getFilho_Direito(self):
        return self._filho_direito
    
    def setFilho_Direito(self, dado):
        self._filho_direito = dado
    
    
    
    def getFilho_Esquerdo(self):
        return self._filho_esquerdo
    
    def setFilho_Esquerdo(self, dado):
        self._filho_esquerdo = dado
    
    
    
class Arvore_Binaria():
    
    def __init__(self, raiz = None):
        self._Raiz = raiz
    
    def getRaiz(self):
        return self._Raiz
    
    def setRaiz(self, dado):
        self._Raiz = dado
    
    def isVazia(self):
        return self._Raiz == None
    
    def Buscar(self,x,d):
        if x==None or x.getDado()==d:
            return x
        if d<x.getDado():
            return self.Buscar(x.getFilho_Esquerdo(), d)
        else:
            return self.Buscar(x.getFilho_Direito(),d)

        
    def pre_Ordem(self,x):
        if x!=None:
            print("%d "%(x.getDado()))
            self.pre_Ordem(x.getFilho_Esquerdo())
            self.pre_Ordem(x.getFilho_Direito())

        
    def pos_Ordem(self,x):
        if x!=None:
            self.pos_Ordem(x.getFilho_Esquerdo())
            self.pos_Ordem(x.getFilho_Direito())
            print("%d "%(x.getDado()))
        
    def em_Ordem(self,x):
        if x!=None:
            self.em_Ordem(x.getFilho_Esquerdo())
            print("%d "%(x.getDado()))
            self.em_Ordem(x.getFilho_Direito())
        
        
        
    def minimo(self,x):
        while x.getFilho_Esquerdo()!=None:
            x=x.getFilho_Esquerdo()
        return x
    def maximo(self,x):
        while x.getFilho_Direito()!=None:
            x=x.getFilho_Direito()
        return x
    
    def sucessor(self,x):
        if x.getFilho_Direito()!=None:
            return self.minimo(x.getFilho_Direito())
        y=x.getPai()
        while y!=None and x==y.getFilho_Direito():
            x=y
            y=y.getPai()
        return y
    
    def predecessor(self,x):
        if x.getFilho_Esquerdo()!=None:
            return self.maximo(x.getFilho_Esquerdo())
        y=x.getPai()
        while y!=None and x==y.getFilho_Esquerdo():
            x=y
            y=y.getPai()
        return y
    
    def Inserir(self, dado):
        z = No(dado = dado)
        x = self._Raiz
        y = None
        while x != None:
            y = x
            if dado < x.getDado():
                x = x.getFilho_Esquerdo()
            else:
                x = x.getFilho_Direito()
        z.setPai(y)
        if y == None:
            self._Raiz = z
        elif dado < y.getDado():
            y.setFilho_Esquerdo(z)
        else:
            y.setFilho_Direito(z)

    def Deletar(self,dado):
        x=self.getRaiz()
        z=self.Buscar(x,dado)
        if z==None:
            return "valor nao pertence a arvore"
        else:
            if z.getFilho_Esquerdo()==None or z.getFilho_Direito()==None:
                y=z
            else: 
                y=self.predecessor(z)
            if y.getFilho_Esquerdo()!=None:
                x=y.getFilho_Esquerdo()
            else:
                x=y.getFilho_Direito()
            if x!=None:
                x.setPai(y.getPai())
            if y.getPai()==None:
                self.setRaiz(x)
            else:
                if y==y.getPai().getFilho_Esquerdo():
                    y.getPai().setFilho_Esquerdo(x)
                else:
                    y.getPai().setFilho_Direito(x)
            if y!=z:
                z.setDado(y.getDado())


N=int(input())
arvore=Arvore_Binaria()
cont_caso=1
while cont_caso<=N:
    lista_Entrada=input().split(" ")
    codigo=lista_Entrada[0]
    
    if codigo=="A":
        valor=int(lista_Entrada[1])
        arvore.Inserir(valor)
        
    elif codigo=="B":
        valor=int(lista_Entrada[1])
        arvore.Deletar(valor)
        
    elif codigo=="C":
        valor=int(lista_Entrada[1])
        a=arvore.getRaiz()
        z=arvore.Buscar(a, valor)
        resultado=arvore.predecessor(z)
        if resultado!=None:
            print(resultado.getDado())
        else:
            print(0)
        
        
    elif codigo=="PRE":
        x=arvore.getRaiz()
        if x==None:
            print(0)
        else:
            arvore.pre_Ordem(x)
    elif codigo=="IN":
        x=arvore.getRaiz()
        if x==None:
            print(0)
        else:
            arvore.em_Ordem(x)
    elif codigo=="POST":
        x=arvore.getRaiz()
        if x==None:
            print(0)
        else:
            arvore.pos_Ordem(x)
    cont_caso+=1