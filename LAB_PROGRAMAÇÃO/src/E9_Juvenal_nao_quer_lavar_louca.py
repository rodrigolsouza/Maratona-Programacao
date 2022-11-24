class No():
    def __init__(self,dado):
        self.dado=dado
        self.apontador=None

    """MÉTODOS DA LISTA"""
      
    def get_Dados(self):
        return self.dado
    
    def set_Dados(self,dado):
        self.dado=dado


    def get_Apontador(self):
        return self.apontador
    def set_Apontador(self,novo_no):
        self.apontador=novo_no
        
class lista():
    def __init__(self):
        self.inicio=None
        self.fim=None
        
    """MÉTODO LISTAR LISTA"""
    def __str__(self):
        if self.isEmpty():
            print("Lista vazia")
        no_Atual=self.inicio
        string="A lista é: "
        while no_Atual!=None:
            string+=str(no_Atual.get_Dados()) +" "    
            no_Atual=no_Atual.get_Apontador()        
        return string   
    
    def isEmpty(self):
        return self.inicio==None
     
    def inserir_inicio(self,valor):
        novo_no= No(valor)
        if self.isEmpty():
            self.fim=novo_no
            self.inicio=novo_no
        else:
            novo_no.set_Apontador(self.inicio)
            self.inicio=novo_no
            
    def inserir_fim(self,valor):
        novo_no=No(valor)
        if self.isEmpty():
            self.inicio=novo_no
            self.fim=novo_no
        else:
            self.fim.set_Apontador(novo_no)
            self.fim=novo_no
        
    
    def remover_inicio(self):
        if self.isEmpty():
            raise IndexError("não há elementos para ser removido")
        valor_primeiro_no=self.inicio.get_Dados()
        if self.inicio==self.fim:
            self.inicio=None
            self.fim=None
        else:
            self.inicio=self.inicio.get_Apontador()
        return valor_primeiro_no
    
    def remover_fim(self):
        if self.isEmpty():
            raise IndexError("não há elementos para ser removido")
        valor_Final=self.fim.get_Dados()
        if self.fim==self.inicio:
            self.fim=None
            self.inicio=None
        else:
            no_Atual=self.inicio
            while no_Atual.get_Apontador() is not self.fim:
                no_Atual=no_Atual.get_Apontador()
            no_Atual=no_Atual.set_Apontador(None)
            self.fim=no_Atual
        return valor_Final
    
class Pilha(lista):
    def empilha(self,dado):
        self.inserir_inicio(dado)
        
    def desempilha(self):
        return self.remover_inicio()
    
class fila(lista):
    def empilha_fim(self,dado):
        self.inserir_fim(dado)
        
    def desempilha_inicio(self):
        return self.remover_inicio()
 
 
    
festas=int(input(""))
contfestas=1

"criacao fila do deck da mesa"

while contfestas<=festas:
    f_mesa=fila()
    mesa=input("")
    lista_mesa=mesa.split(" ")
    for i in range(len(lista_mesa)-1):
        f_mesa.empilha_fim(lista_mesa[i])    
    print(f_mesa)
    print(lista_mesa)
    lista_c=[]
    while True:
        c=input("")
        lista_carta=c.split(" ")
        if c=="-1":
            break
        else:
            cartas_convidado=fila()
            for i in lista_carta:
                cartas_convidado.empilha_fim(i)
            lista_c.append(cartas_convidado)

    ganhador=0
    rodada=1
    while rodada<=1000:
        carta_aberta=f_mesa.desempilha_inicio()
        for x in range(len(lista_c)-1):    
            carta_mao=lista_c[x].desempilha_inicio()
            if carta_aberta !=carta_mao:
                ganhador=0
                lista_c[x].empilha_fim(carta_mao)
            elif carta_aberta==carta_mao:
                if lista_c[x].isEmpty()==True:
                    ganhador=x+1
                    break
        if ganhador!=0:
            break
        f_mesa.empilha_fim(carta_aberta)
        rodada+=1
    print(ganhador)
    contfestas+=1
                
            
        
        

        
        