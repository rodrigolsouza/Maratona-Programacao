class No():

    def _init_(self, dado=None, pai=None, filho1=None, filho2=None):
        self._dado = dado
        self._pai = pai
        self._filho_direito = filho1
        self._filho_esquerdo = filho2

    def getDado(self):
        return self._dado

    def setDado(self, dado):
        self._dado = dado

    def getPai(self):
        return self._pai

    def getFilho1(self):
        return self._filho_direito

    def getFilho2(self):
        return self._filho_esquerdo

    def setPai(self, dado):
        self._pai = dado

    def setFilho1(self, dado):
        self._filho_direito = dado

    def setFilho2(self, dado):
        self._filho_esquerdo = dado


class ArvoreBinaria():

    def _init_(self):
        self._Raiz = None

    def getRaiz(self):
        return self._Raiz

    def setRaiz(self, dado):
        self._Raiz = dado

    def isVazia(self):
        return self._Raiz == None

    def Busca(self, chave, dado):
        while chave is not None and dado is not chave.getDado():
            if dado < chave.getDado():
                chave = chave.getFilho2()
            else:
                chave = chave.getFilho1()
        return chave

    def Minimo(self, no):
        i = no
        while i.getFilho2() is not None:
            i = i.getFilho2()
        return i

    def Maximo(self, no):
        i = no
        while i.getFilho1() is not None:
            i = i.getFilho1()
        return i

    def Sucessor(self, no):
        if no.getFilho1() is not None:
            return self.Minimo(no.getFilho1())
        y = no.getPai()
        while y is not None and no is y.getFilho1():
            no = y
            y = y.getPai()
        return y

    def Antecessor(self, no):
        if no.getFilho2() is not None:
            return self.Maximo(no.getFilho2())
        y = no.getPai()
        while y is not None and no is y.getFilho2():
            no = y
            y = y.getPai()
        return y

    def PreOrdem(self, x):
        if x is not None:
            print(x.getDado())
            self.PreOrdem(x.getFilho2())
            self.PreOrdem(x.getFilho1())

    def EmOrdem(self, x):
        if x is not None:
            self.EmOrdem(x.getFilho2())
            print(x.getDado())
            self.EmOrdem(x.getFilho1())

    def PosOrdem(self, x):
        if x is not None:
            self.PosOrdem(x.getFilho2())
            self.PosOrdem(x.getFilho1())
            print(x.getDado())

    def _str_(self):
        s = ""
        self.EmOrdem(self._Raiz)
        return s


class AVL(ArvoreBinaria):

    def _init_(self):
        ArvoreBinaria._init_(self)

    def Altura(self, no):
        if no == None:
            return -1
        h1 = self.Altura(no.getFilho2())
        h2 = self.Altura(no.getFilho1())
        return (1 + max(h1, h2))

    def FatorBalanceamento(self, no):
        return self.Altura(no.getFilho1()) - self.Altura(no.getFilho2())

    def Nivel(self, raiz, no):
        if self.Busca(raiz, no) == None:
            return print(-1)
        y = raiz
        count = 0
        while y.getDado() != no:
            if no < y.getDado():
                count += 1
                y = y.getFilho2()
            else:
                count += 1
                y = y.getFilho1()
        return print(1+count)

    def L(self, raiz, numero1, numero2):
        s, s1 = "", " "
        while numero1 <= numero2:
            no = self.Busca(raiz, numero1)
            if no != None:
                s += str(numero1)
                s += s1
                numero1+=1
            else:
                numero1+=1
        print(s)

    def Decide(self, no):
        if self.FatorBalanceamento(no) == 2:
            while no.getFilho2() != None:
                no = no.getFilho1()
            if self.FatorBalanceamento(no.getFilho1()) == -1:
                self.RightRotate(no.getFilho1())
                self.LeftRotate(no)
            else:
                self.LeftRotate(no)

        if self.FatorBalanceamento(no) == -2:
            while no.getFilho1() != None:
                no = no.getFilho2()
            if self.FatorBalanceamento(no.getFilho2()) == 1:
                self.LeftRotate(no.getFilho2())
                self.RightRotate(no)
            else:
                self.RightRotate(no)

    def LeftRotate(self, x):
        y = x.getFilho1()
        x.setFilho1(y.getFilho2())
        if y.getFilho2() != None:
            y.getFilho2().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().getFilho2():
                x.getPai().setFilho2(y)
            else:
                x.getPai().setFilho1(y)
        y.setFilho2(x)
        x.setPai(y)

    def RightRotate(self, x):
        y = x.getFilho2()
        x.setFilho2(y.getFilho1())
        if y.getFilho1() != None:
            y.getFilho1().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().getFilho1():
                x.getPai().setFilho1(y)
            else:
                x.getPai().setFilho2(y)
        y.setFilho1(x)
        x.setPai(y)

    def Insere(self, dado):
        z = No(dado=dado)
        x = self._Raiz
        y = None
        while x != None:
            y = x
            if z.getDado() < x.getDado():
                x = x.getFilho2()
            else:
                x = x.getFilho1()
        z.setPai(y)
        if y == None:
            self.setRaiz(z)
        elif z.getDado() < y.getDado():
            y.setFilho2(z)
        else:
            y.setFilho1(z)
        self.Altura(self._Raiz)


ArvoreFilmes = AVL()
a = int(input())
for filmes in range(a):
    count = 0
    while True:
        b = input().split(" ")
        if b[0] == "F":
            ArvoreFilmes = AVL()
            break
        elif b[0] == "I":
            ArvoreFilmes.Insere(int(b[1]))
            count += 1
            if ArvoreFilmes.getRaiz() != None:
                ArvoreFilmes.Decide(ArvoreFilmes.getRaiz())
            if count > 3:
                n = ArvoreFilmes.Busca(ArvoreFilmes.getRaiz(), int(b[1]))
                n2 = n.getPai().getPai()
                if n2 != None:
                    if ArvoreFilmes.Busca(ArvoreFilmes.getRaiz(), n2.getDado()) != None:
                        ArvoreFilmes.Decide(n.getPai().getPai())
        elif b[0] == "N":
            ArvoreFilmes.Nivel(ArvoreFilmes.getRaiz(), int(b[1]))
        elif b[0] == "L":
            ArvoreFilmes.L(ArvoreFilmes.getRaiz(), int(b[1]), int(b[2]))