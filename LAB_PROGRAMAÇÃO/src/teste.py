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

        
    def pre_Ordem(self,l,x):
        if x!=None:
            l.append(x.getDado())
            self.pre_Ordem(l,x.getFilho_Esquerdo())
            self.pre_Ordem(l,x.getFilho_Direito())

        
    def pos_Ordem(self,l,x):
        if x!=None:
            
            self.pos_Ordem(l,x.getFilho_Esquerdo())
            self.pos_Ordem(l,x.getFilho_Direito())
            l.append(x.getDado())

    def em_Ordem(self,l,x):
        if x!=None:
            self.em_Ordem(l,x.getFilho_Esquerdo())
            l.append(x.getDado())
            self.em_Ordem(l,x.getFilho_Direito())

        
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
            return False
        else:
            if z.getFilho_Esquerdo()==None or z.getFilho_Direito()==None:
                y=z
            else: 
                y=self.sucessor(z)
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
        
        
class arvore_Avl(Arvore_Binaria):
        
    def altura(self,x):
        if x==None:
            return -1
        else:
            h1=self.altura(x.getFilho_Esquerdo())
            h2=self.altura(x.getFilho_Direito())
            return(1+max(h1,h2))
    
    def balanceamento(self,x):
        if x==None:
            return 0
        return self.altura(x.getFilho_Direito())-self.altura(x.getFilho_Esquerdo())
    
    def Nivel(self, nodo):
        y=self.Buscar(self._Raiz,nodo)
        if y == None:
            return -1
        else:
            nivel = 1
            while y != self.getRaiz():
                y = y.getPai()
                nivel += 1
            return nivel
        
        
    def rotacao_Esq(self,x):
        x.setPai(None)
        y=x.getFilho_Direito()
        y.setPai(x.getPai())
        if y.getPai() is None:
            self.setRaiz(y)
        else:
            if y.getPai().getFilho_Esquerdo()is x:
                y.getPai().setFilho_Esquerdo(y)
            elif y.getPai().getFilho_Direito() is x:
                y.getPai().setFilho_Direito(y)
        x.setFilho_Direito(y.getFilho_Esquerdo())
        if x.getFilho_Direito() is not None:
            x.getFilho_Direito().setPai(x)
        y.setFilho_Esquerdo(x)
        x.setPai(y)
        
    def rotacao_Esq2(self,x):
        y = x.getFilho_Direito()
        x.setFilho_Direito(y.getFilho_Esquerdo())
        if y.getFilho_Esquerdo() != None:
            y.getFilho_Esquerdo().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().getFilho_Esquerdo():
                x.getPai().setFilho_Esquerdo(y)
            else:
                x.getPai().setFilho_Direito(y)
        y.setFilho_Esquerdo(x)
        x.setPai(y)

        
    def rotacao_Dir(self,x):
        y=x.getFilho_Esquerdo()
        y.setPai(x.getPai())
        if y.getPai() is None:
            self.setRaiz(y)
        else:
            if y.getPai().getFilho_Esquerdo() is x:
                y.getPai().setFilho_Esquerdo(y)
            elif y.getPai().getFilho_Direito() is x:
                y.getPai.setFilho_Direito(y)
        x.setFilho_Esquerdo(y.getFilho_Direito)
        if x.getFilho_Esquerdo is not None:
            x.getFilho_Esquerdo().setPai(x)
        y.setFilho_Direito(x)
        x.setPai(y)

    def rotacao_Dir2(self,x):
        y = x.getFilho_Esquerdo()
        x.setFilho_Esquerdo(y.getFilho_Direito())
        if y.getFilho_Direito() != None:
            y.getFilho_Direito().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().getFilho_Direito():
                x.getPai().setFilho_Direito(y)
            else:
                x.getPai().setFilho_Esquerdo(y)
        y.setFilho_Direito(x)
        x.setPai(y)

    def rebalanceamento(self, nodo):
        while nodo.getPai() != None:
            if self.balanceamento(nodo.getPai()) == 2 and self.balanceamento(nodo) == 1:
                self.rotacao_Dir(nodo.getPai())
            if self.balanceamento(nodo.getPai()) == -2 and self.balanceamento(nodo) == -1:
                self.rotacao_Esq(nodo.getPai())
            if self.balanceamento(nodo.getPai()) == 2 and self.balanceamento(nodo) == -1:
                self.rotacao_Esq(nodo)
                self.rotacao_Dir(nodo.getPai().getPai())
            if self.balanceamento(nodo.getPai()) == -2 and self.balanceamento(nodo) == 1:
                self.rotacao_Dir(nodo)
                self.rotacao_Esq(nodo.getPai().getPai())
            nodo = nodo.getPai()
 
     
        
    def rebalanceamento2(self,x):
        if self.balanceamento(x)>=-1 and self.balanceamento(x)<=1:
            return
        elif self.balanceamento(x)>1:
            if self.balanceamento(x.getFilho_Direito())<0:
                self.rotacao_Dir(x.getFilho_Direito())
                self.rotacao_Esq(x)
            else:
                self.rotacao_Esq(x)
                
        elif self.balanceamento(x)<1:
            if self.balanceamento(x.getFilho_Esquerdo())>0:
                self.rotacao_Esq(x.getFilho_Esquerdo())
                self.rotacao_Dir(x)
            else:
                self.rotacao_Dir(x)
            
        
    def Inserir_Avl(self,dado):
        z = No(dado = dado)
        x = self._Raiz
        y = None
        while x != None:
            y = x
            if z.getDado() < x.getDado():
                x = x.getFilho_Esquerdo()
            else:
                x = x.getFilho_Direito()
        z.setPai(y)
        if y == None:
            self._Raiz = z
        elif z.getDado() < y.getDado():
            y.setFilho_Esquerdo(z)
        else:
            y.setFilho_Direito(z)
        self.rebalanceamento(z)
        
    
    
#    def Deletar_Avl(self,dado):
#        super().Deletar(dado)
        
        
    
'''lista=[13,7,5,20,30]
a=Arvore_Binaria()
for i in lista:
    a.inserir(i)
    
print("pre ordem")
a.preordem(a.getraiz())

print("Em ordem")
a.emordem(a.getraiz())

print("Pos ordem")
a.posordem(a.getraiz())
a.Inserir(30)
print(a.getRaiz().getDado())'''


C=int(input(""))
for x in range(C):
    a=arvore_Avl()
    while True:
        comando=input("")
        if len(comando)==1:
            codigo=comando
        elif len(comando)==3:
            lista_comando=comando.split(" ")
            codigo=lista_comando[0]
            serie=int(lista_comando[1])
        elif len(comando)==5:
            lista_comando=comando.split(" ")
            codigo=lista_comando[0]
            serie=int(lista_comando[1])
            serie2=int(lista_comando[2])
            
        if codigo=="I":
            a.Inserir_Avl(serie)
            
        elif codigo=="N":
            
            print(a.Nivel(serie))
            
        elif codigo=="L":
            l1=[]
            l2=[]
            a.em_Ordem(l1,a.getRaiz())
            res=""
            for i in l1:
                if i>=serie and i<=serie2:
                    res+=str(i)+" "
            print(res[:-1])
                
        elif codigo=="F":
            print("\n")
            break