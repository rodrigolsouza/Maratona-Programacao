'''
Created on 16/10/2017

@author: Rodrigo
'''
arquivo=open("C:\Users\Rodrigo\workspace\LAB_PROG\src\maratona.txt","r")
E1=arquivo.readline()
E2=arquivo.readline()
arquivo.close()
vetor1=E1.split(" ")
vetor2=E2.split(" ")
teste=True
for x in range(int(vetor1[0])):
    if (int(vetor2[x])-int(vetor2[x-1]))>int(vetor1[1]):
        teste*=False
if teste==False:
    print("N")
else:
    print("S")