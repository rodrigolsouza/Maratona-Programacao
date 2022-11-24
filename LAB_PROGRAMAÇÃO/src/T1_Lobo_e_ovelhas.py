Ovelhas = 0
Lobos = 0
TotalLobos = 0
TotalOvelhas = 0
def Contadores(x,y,Pastotal,linhas,colunas):
    try:
        global Ovelhas
        global Lobos
        if x<0 or y<0:
            return
        if x>linhas or y>linhas:
            return
        if x>colunas or y>colunas:
            return

        if Pastotal[x][y]== ".":
            Pastotal[x][y]="x"
            Contadores(x,y+1,Pastotal,linhas,colunas)
            Contadores(x,y-1,Pastotal,linhas,colunas)
            Contadores(x+1,y,Pastotal,linhas,colunas)
            Contadores(x-1,y,Pastotal,linhas,colunas)

        if Pastotal[x][y]=="#":
            return

        if Pastotal[x][y]=='k':
            Ovelhas+=1
            Pastotal[x][y]="x"
            Contadores(x,y+1,Pastotal,linhas,colunas)
            Contadores(x,y-1,Pastotal,linhas,colunas)
            Contadores(x+1,y,Pastotal,linhas,colunas)
            Contadores(x-1,y,Pastotal,linhas,colunas)
            
        if Pastotal[x][y]=='v':
            Lobos+=1
            Pastotal[x][y]= "x"
            Contadores(x,y+1,Pastotal,linhas,colunas)
            Contadores(x,y-1,Pastotal,linhas,colunas)
            Contadores(x+1,y,Pastotal,linhas,colunas)
            Contadores(x-1,y,Pastotal,linhas,colunas)
    except:
        IndexError




Comandos = input().split(" ")
Pastotal = []


for x in range (int(Comandos[0])):
  Building = [None]*(int(Comandos[-1]))
  Pastotal.append(Building)

for x in range(int(Comandos[0])):
    Caracteres = input("")
    for z in range(len(Caracteres)):
        for y in range (int(Comandos[-1])):
            Pastotal[x][y]= Caracteres[y]


for x in range(int(Comandos[0])-1):
    for y in range(int(Comandos[-1])-1):
        Contadores(x,y,Pastotal,int(Comandos[0]),int(Comandos[-1]))
        for z in Pastotal:
            print(" ".join(z))
        if Lobos >= Ovelhas:
            Ovelhas = 0
        else:
            Lobos = 0
        TotalLobos += Lobos
        TotalOvelhas += Ovelhas
        Lobos = 0
        Ovelhas = 0

print(TotalOvelhas,TotalLobos)
    

            


