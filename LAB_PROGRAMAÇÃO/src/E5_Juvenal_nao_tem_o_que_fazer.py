'''
Created on 03/11/2017

@author: Rodrigo
'''

def formula_juvenal(n,cont=0):
    if n==1:
        cont+=1
        return 1,cont
    elif n%2==0:
        cont+=1
        return formula_juvenal(n/2,cont)
    elif n%2!=0:
        cont+=1
        return formula_juvenal(3*n+1,cont)
    

T=int(input(""))
i=1
while i<=T:
    Entrada=input("")
    lista_Entrada=Entrada.split(" ")
    A=int(lista_Entrada[0])
    B=int(lista_Entrada[1])
    maior=0
    for j in range(A,B):
        contador=formula_juvenal(j)[1]
        if contador>maior:
            maior=contador
    
    print("Caso %d: %d"%(i,maior))
    i+=1