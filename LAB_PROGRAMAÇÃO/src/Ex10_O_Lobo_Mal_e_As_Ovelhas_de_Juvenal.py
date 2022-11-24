'''
Created on 09/12/2017

@author: Rodrigo
'''
ovelha=0
lobo_mau=0
TotalLobo = 0
TotalOvelha = 0
def pasto(i,j,T,m,n):
    global ovelha
    global lobo_mau
    if i<0 or j<0:
        return
    if i>m or j>m:
        return
    if i>n or j>n:
        return
    if T[i][j]==".":
        T[i][j]="x"
        pasto(i,j+1,T,m,n)
        pasto(i,j-1,T,m,n)
        pasto(i+1,j,T,m,n)
        pasto(i-1,j,T,m,n)

    if T[i][j]=="#":
        return
    if T[i][j]=='k':
        ovelha+=1
        T[i][j]="x"
        pasto(i,j+1,T,m,n)
        pasto(i,j-1,T,m,n)
        pasto(i+1,j,T,m,n)
        pasto(i-1,j,T,m,n)
        
    if T[i][j]=='v':
        lobo_mau+=1
        T[i][j]="x"
        pasto(i,j+1,T,m,n)
        pasto(i,j-1,T,m,n)
        pasto(i+1,j,T,m,n)
        pasto(i-1,j,T,m,n)
    

entrada=input("")
lista_entrada=entrada.split(" ")
m=int(lista_entrada[0])
n=int(lista_entrada[1])
T=[]
total_ovelha=0
total_lobo=0

for x in range (m):
  construtordematriz=[None]*(n)
  T.append(construtordematriz)

for i in range(m):
    c=input("")
    for ch in range(len(c)):
        for j in range (n):
            T[i][j]=c[j]
            
    
for i in range(m-1):
    for j in range(n-1):
        pasto(i,j,T,m,n)
        if lobo_mau>= ovelha:
            ovelha = 0
        else:
            lobo_mau = 0
    TotalOvelha += ovelha
    TotalLobo += lobo_mau
    ovelha = 0
    lobo_mau = 0
    
print("%d %d"%(TotalOvelha,TotalLobo))