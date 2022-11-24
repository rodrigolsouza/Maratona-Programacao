'''
Created on 22/10/2017

@author: Rodrigo
'''

numeros=input("")
lista_numeros=numeros.split(" ")
N=lista_numeros[0]
M=lista_numeros[1]

            
dicionario=[]
while len(dicionario)<int(N):
    pal_correta=input("")
    dicionario.append(pal_correta)

            
palavras=[]
while len(palavras)<int(M):
    pal_analisada=input("")
    palavras.append(pal_analisada)
    
lista_interm=[]            
for x in palavras:
    w=""
    j=0
    while j<int(N):
        padrao=dicionario[j]
        if abs(len(x)-len(padrao))>2:
            w=""
        else:
            cont=0
            for ch in x:
                lista_iguais=[]
                if ch in padrao:
                    cont+=1
                if x.count(ch)>padrao.count(ch):
                    if ch not in lista_iguais:
                        lista_iguais=[ch]*(x.count(ch)-padrao.count(ch))
                cont=cont-len(lista_iguais)       
            if abs(cont-len(padrao))<=2:
                lista_interm.append(padrao)
                        
        j+=1
    for z in (lista_interm):
        if len(lista_interm)==0:
            w=""
        elif len(lista_interm)==1:
            w=z
        else:
            w+=z + " "
    print(w)
    lista_interm=[]  