'''
Created on 22/10/2017

@author: Rodrigo
'''
while True:
    N=int(input(""))
    if N>=2 and N<=1000:
        break
while True:    
    peças=input("")
    lista_peças=peças.split(" ")
    if len(lista_peças)==N-1:
        if len(lista_peças)==len(set(lista_peças)):
            break

lista=[]
for x in lista_peças:
    z=int(x)
    lista.append(z)
lista.sort()
for i in range(1,N):
    if i not in lista:
        print(i)
