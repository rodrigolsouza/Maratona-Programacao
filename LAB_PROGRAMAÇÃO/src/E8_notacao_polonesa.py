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
while True:
    try:        
        operacoes=Pilha()
        entrada=input()
        listaentrada=entrada.split(" ")
        cont=len(listaentrada)-1
        while cont>-1:
            if listaentrada[cont]!='+' and listaentrada[cont] != '-' and listaentrada[cont]!= '*' and listaentrada[cont]!= '/':
                operacoes.empilha(listaentrada[cont])

            else:
                if listaentrada[cont]=="+":
                    operando1=operacoes.desempilha()
                    operando2=operacoes.desempilha()
                    resultado=int(operando1) + int(operando2)
                    operacoes.empilha(resultado)
                        
                elif listaentrada[cont]=="-":
                    operando1=operacoes.desempilha()
                    operando2=operacoes.desempilha()
                    resultado=int(operando1) - int(operando2)
                    operacoes.empilha(resultado)
                        
                elif listaentrada[cont]=="*":
                    operando1=operacoes.desempilha()
                    operando2=operacoes.desempilha()
                    resultado=int(operando1) * int(operando2)
                    operacoes.empilha(resultado)
                        
                elif listaentrada[cont]=="/":
                    operando1=operacoes.desempilha()
                    operando2=operacoes.desempilha()
                    if (operando1<0 and operando2>0)  or (operando1>0 and operando2<0):
                        resultado=(int(operando1) // int(operando2))+1
                    else:
                        resultado=int(operando1) // int(operando2)
                    operacoes.empilha(resultado)
            cont-=1
        print(operacoes.desempilha())
    except:
        if entrada=="":
            break