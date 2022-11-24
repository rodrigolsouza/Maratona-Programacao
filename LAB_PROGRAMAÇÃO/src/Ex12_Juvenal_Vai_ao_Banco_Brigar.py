'''
Created on 13/12/2017

@author: Rodrigo
'''
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
    
    
class fila(lista):
    def empilha_fim(self,dado):
        self.inserir_fim(dado)
        
    def desempilha_inicio(self):
        return self.remover_inicio()
        
    def isEmpty(self):
        return self.inicio==None

T=int(input(""))
cont_casos=1
while True:
    if cont_casos>T:
        break
    fila_regular=0
    fila_priori=0
    fr=fila()
    fp=fila()
    N=int(input(""))
    total=""
    for x in range(N):
        comandos=input("")
        if comandos[0]=="f":
            valor_comandos=comandos.split(" ")
            fr.empilha_fim(int(valor_comandos[1]))
                
        elif comandos[0]=="p":
            valor_comandos=comandos.split(" ")
            fp.empilha_fim(int(valor_comandos[1]))
                
                
        elif comandos[0]=="A":
            if fr.isEmpty():
                if fp.isEmpty():
                    fila_regular=0
                    fila_priori=0
                else:
                    fp.desempilha_inicio()
            else:
                fr.desempilha_inicio()
                    
                    
        elif comandos[0]=="B":
            if fp.isEmpty():
                if fr.isEmpty():
                    fila_regular=0
                    fila_priori=0
                else:
                    fr.desempilha_inicio()
            else:
                fp.desempilha_inicio()
                    
                    
        elif comandos[0]=="I":
            if fr.isEmpty()==False and fp.isEmpty()==False:
                fila_regular=fr.desempilha_inicio()
                fila_priori=fp.desempilha_inicio()
                fr.inserir_inicio(fila_regular)
                fp.inserir_inicio(fila_priori)
                total+=str(fila_regular)+" "+str(fila_priori)+"/"
                
            elif fr.isEmpty()==False and fp.isEmpty()==True:
                fila_priori=0
                fila_regular=fr.desempilha_inicio()
                fr.inserir_inicio(fila_regular)
                total+=str(fila_regular)+" "+str(fila_priori)+"/"

                
            elif fr.isEmpty()==True and fp.isEmpty()==False:
                fila_regular=0
                fila_priori=fp.desempilha_inicio()
                fp.inserir_inicio(fila_priori)
                total+=str(fila_regular)+" "+str(fila_priori)+"/"
                
            else:
                if fr.isEmpty()==True and fp.isEmpty()==True:
                    fila_regular=0
                    fila_priori=0
                    total+=str(fila_regular)+" "+str(fila_priori)+"/"

    lista_total=total.split("/")
    del lista_total[-1]
    print("Caso %d:"%(cont_casos))
    for resposta in lista_total:
        print(resposta)
    cont_casos+=1