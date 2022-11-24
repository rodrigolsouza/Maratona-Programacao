'''
Calculando o Fibonnaci de um numero em uma máquina que não tem recursividade.(Simulação das pilhas de execução)

author: Rodrigo
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
    
class Pilha(lista):
    def empilha(self,dado):
        self.inserir_inicio(dado)
        
    def desempilha(self):
        return self.remover_inicio()
    

def func_PilhaFib(n):
    while True:
        if n>2:
            pilha.empilha(str(n))
            n-=1
        elif n>0 and n<=2:
            pilha.empilha(1)
            n-=1
        else:
            if n==0:
                break 

    while True:
        fator2=pilha.desempilha()
        fator1=pilha.desempilha()
        pilha.desempilha()
        resultado=fator1+fator2
        fator1,fator2=fator2,resultado
        if pilha.isEmpty()==True:
            return resultado
            break
        else:
            pilha.empilha(fator1)
            pilha.empilha(fator2)    
        
pilha=Pilha()
valor=int(input(""))
teste=func_PilhaFib(valor)
print(teste)       
        
    
    