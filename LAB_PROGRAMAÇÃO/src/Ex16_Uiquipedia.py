'''
Created on 29/01/2018

@author: Rodrigo
'''
import sys
class vertice():
    def __init__(self,id,nome):
        self.id=id
        self.nome=nome
        self.minima_distancia= sys.maxsize
        self.visitado=False
        self.anterior=None

class aresta(): 
    def __init__(self,vertice_inicial,vertice_final):
        self.vertice_inicial=vertice_inicial
        self.vertice_final=vertice_final
        
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




g= grafo()
lista_palavras=[]
lista_caminhos_palavras=[]
N= int(input(""))
linhas=N+2
for n in range(linhas):
    if n<N:
        lista_Entrada=input("").split(" ")
        lista_caminhos_palavras.append(lista_Entrada[0])
        if lista_Entrada[0] not in lista_palavras:
            lista_palavras.append(lista_Entrada[0])
        lista_caminhos_palavras.append(lista_Entrada[1])
        if lista_Entrada[1] not in lista_palavras:
            lista_palavras.append(lista_Entrada[1])
    else:
        Entrada=input("")
        if Entrada!="":
            lista_Entrada=Entrada.split(" ")
            P=lista_Entrada[0]
            A=lista_Entrada[1]
            
listaordenada=lista_palavras[:]
listaordenada.sort()

for x in range(len(listaordenada)):
    v=vertice(x,listaordenada[x])
    g.lista_vertices.append(v)
    
for i in range(len(g.lista_vertices)):
    linhamatriz=[]
    for j in range(len(g.lista_vertices)):
        linhamatriz.append(-1)
    g.matriz_adjacencia.append(linhamatriz)
    
for i in range(len(g.lista_vertices)):
    for j in range(len(g.lista_vertices)):
        if g.lista_vertices[j].id==0:
            if g.lista_vertices[j].id==g.lista_vertices[j+1].id-1:
                g.matriz_adjacencia[j][j+1]=1
                g.matriz_adjacencia[j+1][j]=1
            else:
                g.matriz_adjacencia[j][j+1]=-1
                g.matriz_adjacencia[j+1][j]=-1
                
        elif g.lista_vertices[j].id==len(g.lista_vertices)-1:
            if g.lista_vertices[j].id==g.lista_vertices[j-1].id+1:
                g.matriz_adjacencia[j][j-1]=1
                g.matriz_adjacencia[j-1][j]=1
            else:
                g.matriz_adjacencia[j][j-1]=-1
                g.matriz_adjacencia[j-1][j]=-1
                
        else:        
            if g.lista_vertices[j].id==g.lista_vertices[j+1].id-1 and g.lista_vertices[j].id==g.lista_vertices[j-1].id+1:
                g.matriz_adjacencia[j][j+1]=1
                g.matriz_adjacencia[j+1][j]=1
                g.matriz_adjacencia[j][j-1]=1
                g.matriz_adjacencia[j-1][j]=1
            else:
                g.matriz_adjacencia[j][j+1]=-1
                g.matriz_adjacencia[j+1][j]=-1
                g.matriz_adjacencia[j][j-1]=-1
                g.matriz_adjacencia[j-1][j]=-1
                

lista_numeros=[]
for y in lista_caminhos_palavras:
    for x in g.lista_vertices:
        if y==x.nome:
            lista_numeros.append(x.id)
z=1            
while z<len(lista_numeros):
    g.matriz_adjacencia[lista_numeros[z-1]][lista_numeros[z]]=1
    z+=2

for x in g.lista_vertices:
    if P==x.nome:
        partida=x   
for x in g.lista_vertices:
    if A==x.nome:
        chegada=x

resposta=Dijkstra(g, partida)[chegada.id].minima_distancia
print(resposta)


'''print(lista_caminhos_palavras)
print(lista_numeros)
for i in range(len(g.lista_vertices)):
    acumulador=""
    for j in range(len(g.lista_vertices)):
        acumulador+=str(g.matriz_adjacencia[i][j])+" "  
    print (acumulador)'''
    
    