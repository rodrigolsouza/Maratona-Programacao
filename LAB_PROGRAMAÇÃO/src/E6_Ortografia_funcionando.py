'''
Created on 03/11/2017

@author: Rodrigo
'''
def corretor(s1,s2):
    matriz= [None]*(len(s2)+1)
    for a in range(len(s2)+1):
        matriz[a]=[0]*(len(s1)+1)
    for b in range(1, len(s2)+1):
        matriz[b][0] = b
    for c in range(1,len(s1)+1):
        matriz[0][c]=c
        
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1]==s2[i-1]:
                distancia=0
            else:
                distancia=1
            matriz[i][j]=min(matriz[i-1][j-1]+distancia,matriz[i][j-1]+1,matriz[i-1][j]+1)
    if matriz[i][j] <= 2:
        return s2 + ' '
    return ''


quant_palavras = input("").split(" ")


z= ""
for x in range(int(quant_palavras[0])):
    z+= input("")+" "
dicionario= z.split(" ")
del dicionario[-1]


for x in range(int(quant_palavras[1])):
    Palavra_a_analisar= input("")
    sugestao= ""
    for C in dicionario:
        if abs(len(Palavra_a_analisar)-len(C))<=2:
            sugestao+=corretor(Palavra_a_analisar,C)
    print(sugestao[:-1])
