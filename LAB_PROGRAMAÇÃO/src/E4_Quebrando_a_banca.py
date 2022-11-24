'''
criar um programa que consegue selecionar quais numeros devem sair
para que o numeral restante fique equivalente ao maior valor possivel.
Para tal usou-se a ideia de verificar quem vai ficar, nesse caso (A-B) 
vai indicar qual o grau dos numeros que ficarão(ex:centena,dezena,unidade)
a partir de então deve-se procurar qual o maior numero até a primiera posição obrigatoriamente vai ficar,
depois deve-se ir do numero seguinte até ((A-B)-1) para encontrar o segundo maior valor e 
assim sucessivamente (Nmaior+1 até (A-B)-1) até chegar no grau de unidade e escolher-se o maior.
@author: Rodrigo
'''
while True:
    Entrada=input("")
    lista_Entrada=Entrada.split(" ")
    if len(lista_Entrada)==2:
        A=int(lista_Entrada[0])
        B=int(lista_Entrada[1])
        if A>B and B>=1 and A<=10000 and A>=1:
            break
    
while True:
    valor_saldo=input("")
    if len(valor_saldo)!=A:
        continue
    else:
        break
    
lista=[]
for x in range(len(valor_saldo)):
    lista.append(valor_saldo[x])
    
w=(A-B)
Li=0
lista_final=[]
indice=0

while w>0:
    for i in range(Li,len(lista)+1-w):
        if i==Li:
            maior=lista[Li]
        if lista[i]>maior:
            maior=lista[i]
            indice=i
             
    w-=1
    lista_final.append(maior)
    Li=indice+1
    
ch=""
for j in lista_final:
    ch+=str(j)
print(ch)
   
    
        