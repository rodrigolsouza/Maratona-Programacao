'''
Forma mais enxuta de se calcular a soma fatorial de inteiros que resulta num numero N qualquer

@author: Rodrigo
'''
while True:
    Nfixo= int(input(""))
    if Nfixo>=1 and Nfixo<=100000:
        break   
lista=[]
soma=0
conttermos=0    
N=Nfixo

while soma<Nfixo:
    fat=1
    x=1
    while N>=fat:
        x+=1
        fat*=x
    fat=int(fat/x)
    lista.append(x-1)
    conttermos+=1
    N=N-fat
    soma+=fat
    
print(lista)
print(conttermos)

