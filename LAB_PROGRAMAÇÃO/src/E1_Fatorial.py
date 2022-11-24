'''
Created on 07/10/2017 por Rodrigo Lopes

@author: Rodrigo
'''
while True:
    Nfixo= int(input(""))
    if Nfixo>=1 and Nfixo<=100000:
        break   
soma=0
conttermos=0    
N=Nfixo

while soma<Nfixo:
    fat=1
    x=1
    while N>=fat:
        x+=1
        fat*=x
    conttermos+=1
    N=N-int(fat/x)
    soma+=int(fat/x)
print(conttermos)

            
            
        
