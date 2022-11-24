'''
Created on 27/01/2018

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


def extrator_minimo(g,S):
    min=None
    for v in g.lista_vertices:
        if not S[v.id]:
            if min==None:
                min=v
            elif v.minima_distancia<min.minima_distancia:
                min=v
    return min        
            

def Dijkstra(g,s):
    S=[]
    for v in g.lista_vertices:
        v.minima_distancia= sys.maxsize
        v.anterior=-1
        v.visitado=False
        S.append(v.visitado)
    s.minima_distancia=0
    
    Q=g.lista_vertices[:]
    
    for i in range(len(g.lista_vertices)):
        u=extrator_minimo(g,S)
        S[u.id]=True
        for j in g.lista_vertices:
            if g.matriz_adjacencia[u.id][j.id]!=-1:
                if j.minima_distancia>u.minima_distancia + int(g.matriz_adjacencia[u.id][j.id]):
                    j.minima_distancia=u.minima_distancia+ int(g.matriz_adjacencia[u.id][j.id])
                    j.anterior=u.id
    return g.lista_vertices

  
        
g=grafo()
Entrada=input("").split(" ")
cidades=int(Entrada[0])
voos=int(Entrada[1])


for x in range(cidades):
    v= vertice(x)
    g.lista_vertices.append(v)
    
for y in range(voos):
    destino=input("").split(" ")
    E=aresta(int(destino[0]),int(destino[1]),int(destino[2]))
    g.lista_arestas.append(E)
    
    
    
for i in range(len(g.lista_vertices)):
    linhamatriz=[]
    for j in range(len(g.lista_vertices)):
        linhamatriz.append(-1)
    g.matriz_adjacencia.append(linhamatriz)
    
        
for x in g.lista_arestas:
    g.matriz_adjacencia[x.vertice_inicial][x.vertice_final]=x.peso
    g.matriz_adjacencia[x.vertice_final][x.vertice_inicial]=x.peso

           
                
                
'''for i in range(len(g.lista_vertices)):
    acumulador=""
    for j in range(len(g.lista_vertices)):
        acumulador+=str(g.matriz_adjacencia[i][j])+" "  
    print (acumulador)'''
    
lista_me_maior_dist=[]    
for s in g.lista_vertices:
    listadijkstra=Dijkstra(g, s)
    maior=0
    for v in listadijkstra:
        if v.minima_distancia>maior:
            maior=v.minima_distancia
    lista_me_maior_dist.append(maior)
    
print(min(lista_me_maior_dist)) 
    

    
'''for i in g.lista_arestas:
    print (i.peso)''' 


