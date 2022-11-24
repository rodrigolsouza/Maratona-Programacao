
entrada=input("")
lista_Entrada=entrada.split(" ")
mod=int(lista_Entrada[1])
pais=int(lista_Entrada[0])
lista_Paises=[]

for x in range(pais+1):
    lista_Paises.append(0)

for y in range(mod):
    lista_Podium=input("").split(" ")
    for z in range (pais+1):   
        if int(lista_Podium[0])== z:
            lista_Paises[z]+=100000
        if int(lista_Podium[1])== z:
            lista_Paises[z]+=1000
        if int(lista_Podium[2])==z:
            lista_Paises[z]+=1
lista_Paises[0]=-1
seq=""
w=0
lista_P2=lista_Paises[:]

while len(lista_P2)!=1:
    maior=max(lista_P2)
    if lista_P2.count(maior)>1:
        indice_maior=lista_Paises.index(maior)
        lista_Paises[indice_maior]=-1
        lista_P2.remove(maior)
    elif lista_P2.count(maior)==1:
        indice_maior=lista_Paises.index(maior)
        lista_P2.remove(maior)
    seq+=str(indice_maior) + " "

print(seq)
      
    