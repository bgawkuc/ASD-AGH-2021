# Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj algorytm, który stwierdza
# czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że graf reprezentowany jest przez macierz sasiedztwa A

def cycleOfLength4(G):
    n = len(G)
    res = [-1] * 4 

    def DFSvisit(G,u,parent,cnt=3):
        nonlocal start
        res[cnt] = u 
        
        #gdy jeszcze cykl ma szanse powstac
        if cnt >= 0: 
            for v in range(n): 
                if G[u][v] != 0:

                    # gdy szukam sciezki
                    if i != start and i != parent and cnt != 0:
                        DFSvisit(G,i,x,cnt-1)

                    #gdy mam juz sciezke dlg 4, a start i koniec sa rowne
                    elif i == start and cnt == 0:
                        print(res)
                        exit(0)

    for u in range(n): 
        start = u
        DFSvisit(G,u,u)
