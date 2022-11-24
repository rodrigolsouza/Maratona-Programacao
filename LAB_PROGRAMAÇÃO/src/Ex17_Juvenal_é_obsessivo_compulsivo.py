'''
Created on 31/01/2018

@author: Rodrigo
'''
import sys
class vertice():
    def __init__(self,nome):
        self.id=nome
        self.minima_distanciaF= sys.maxsize
        self.minima_distanciaS= sys.maxsize
        self.qtd_arestas=0
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
 
def extrator_minimo(g,S):
    min=None
    for v in g.lista_vertices:
        if not S[v.id-1]:
            if min==None:
                min=v
            elif v.minima_distanciaF<min.minima_distanciaF:
                min=v
    return min 
        
def Dijkstra(g,s):
    S=[]
    for v in g.lista_vertices:
        v.minima_distanciaF= sys.maxsize
        v.minima_distanciaS= sys.maxsize
        v.anterior=-1
        v.visitado=False
        S.append(v.visitado)
    s.minima_distanciaF=0
    
    Q=g.lista_vertices[:]
    
    for i in range(len(g.lista_vertices)):
        u=extrator_minimo(g,S)
        S[u.id-1]=True
        for j in g.lista_vertices:
            if g.matriz_adjacencia[u.id-1][j.id-1]!=-1:
                if u.qtd_arestas%2==0:
                    if j.minima_distanciaS>u.minima_distanciaF + int(g.matriz_adjacencia[u.id-1][j.id-1]):
                        j.minima_distanciaS=u.minima_distanciaF+ int(g.matriz_adjacencia[u.id-1][j.id-1])
                        j.anterior=u.id
                        j.qtd_arestas+=1
                        
                if u.qtd_arestas%2!=0:
                    if j.minima_distanciaF>u.minima_distanciaS + int(g.matriz_adjacencia[u.id-1][j.id-1]):
                        j.minima_distanciaF=u.minima_distanciaS+ int(g.matriz_adjacencia[u.id-1][j.id-1])
                        j.anterior=u.id
                        j.qtd_arestas+=1
                    
    return g.lista_vertices




        
g=grafo()
lista_Entrada=input("").split(" ")
cidades=int(lista_Entrada[0])
estradas=int(lista_Entrada[1])

for x in range(cidades):
    x=x+1
    v=vertice(x)
    g.lista_vertices.append(v)

for y in range(estradas):
    destino=input("").split(" ")
    E=aresta(int(destino[0]),int(destino[1]),int(destino[2]))
    g.lista_arestas.append(E)
        
    
    
for i in range(len(g.lista_vertices)):
    linhamatriz=[]
    for j in range(len(g.lista_vertices)):
        linhamatriz.append(-1)
    g.matriz_adjacencia.append(linhamatriz)
       
    
for x in g.lista_arestas:
    g.matriz_adjacencia[x.vertice_inicial-1][x.vertice_final-1]=x.peso
    g.matriz_adjacencia[x.vertice_final-1][x.vertice_inicial-1]=x.peso


partida=g.lista_vertices[0]
chegada=g.lista_vertices[-1]

resultado= Dijkstra(g, partida)[chegada.id-1].minima_distanciaF
if resultado==sys.maxsize:
    print(-1)
else:
    print(resultado)
    
'''res=Dijkstra(g, partida) 
for x in res:
    print(x.minima_distanciaS)
    print(x.qtd_arestas) 
    
for i in range(len(g.lista_vertices)):
    acumulador=""
    for j in range(len(g.lista_vertices)):
        acumulador+=str(g.matriz_adjacencia[i][j])+" "  
    print (acumulador)'''
    

    