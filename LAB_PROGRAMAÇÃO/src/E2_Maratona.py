'''
Created on 16/10/2017

@author: Rodrigo
'''
E1=input("")
vetor1=E1.split(" ")
E2=input("")
vetor2=E2.split(" ")
teste=True
for x in range(int(vetor1[0])):
    if (int(vetor2[x])-int(vetor2[x-1]))>int(vetor1[1]):
        teste*=False
if teste==False:
    print("N")
else:
    print("S")
        