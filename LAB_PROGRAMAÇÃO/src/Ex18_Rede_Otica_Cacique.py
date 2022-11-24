'''
Created on 02/02/2018

@author: Rodrigo
'''
import sys
class vertice():
    def __init__(self,nome):
        self.id=nome
        self.minima_distancia= sys.maxsize
        self.visitado=False
        self.anterior=None
        
        
class aresta(): 
    def __init__(self,vertice_inicial,vertice_final,peso):
        self.vertice_inicial=vertice_inicial
        self.vertice_final=vertice_final
        self.peso=peso
        
class grafo():
    def __init__(self):
        self.numvertices=0
        self.lista_vertices=[]
        self.lista_arestas=[]
        self.matriz_adjacencia=[]

def insertionSort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i-1
        while j>=0 and x.peso<A[j].peso:
            A[j+1] = A[j]
            j=j-1
        A[j+1]= x

    return A

def insertionSort2(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i-1
        while j>=0 and x.vertice_inicial<=A[j].vertice_inicial:
            if x.vertice_inicial==x.vertice_inicial and x.vertice_final<A[j].vertice_final:
                A[j+1] = A[j]
                j=j-1
            elif x.vertice_inicial<A[j].vertice_inicial:
                A[j+1] = A[j]
                j=j-1
            A[j+1]= x
    return A
teste=1
while True:
    Entrada=input("").split(" ")
    N=int(Entrada[0])
    M=int(Entrada[1])
    if N==0:
        break
    else:
        g=grafo()
        for x in range(N):
            v=vertice(x)
            g.lista_vertices.append(v)
            
        for y in range(M):
            rede=input("").split(" ")
            E=aresta(int(rede[0]),int(rede[1]),int(rede[2]))
            g.lista_arestas.append(E)
        
        insertionSort(g.lista_arestas)
        A=[]
        Lista_arestas=[]
        for x in g.lista_arestas:
            if x.vertice_inicial in A and x.vertice_final not in A:
                A.append(x.vertice_final)
                Lista_arestas.append(x)
            elif x.vertice_inicial not in A and x.vertice_final in A:
                A.append(x.vertice_inicial)
                Lista_arestas.append(x)
            elif x.vertice_inicial not in A and x.vertice_final not in A:
                A.append(x.vertice_inicial)
                A.append(x.vertice_final)
                Lista_arestas.append(x)
        if teste==1:
            print("Teste %d"%(teste))
            for x in Lista_arestas:
                if x.vertice_final<x.vertice_inicial:
                    x.vertice_final,x.vertice_inicial=x.vertice_inicial,x.vertice_final
            insertionSort2(Lista_arestas)
            for x in Lista_arestas:
                print (str(x.vertice_inicial)+" "+str(x.vertice_final))
        else:
            print("")
            print("Teste %d"%(teste))
            for x in Lista_arestas:
                if x.vertice_final<x.vertice_inicial:
                    x.vertice_final,x.vertice_inicial=x.vertice_inicial,x.vertice_final
            insertionSort2(Lista_arestas)
            for x in Lista_arestas:
                print (str(x.vertice_inicial)+" "+str(x.vertice_final))
    teste+=1
    
    