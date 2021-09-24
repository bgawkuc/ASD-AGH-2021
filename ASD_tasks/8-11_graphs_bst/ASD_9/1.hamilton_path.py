
# Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz. 
# W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi
# czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym (DAG).

#sprawdza czy w grafie G jest krawedz z wierzcholka u do v
def isEdge(G,u,v):
    for z in G[u]:
        if z == v:
            return True
    return False

flag = True

def path(G):
    global flag
    res = []
    visited = [False] * (len(G))


    def DFSvisit(u):
        global flag
        visited[u] = True

        for v in G[u]:

            if not visited[v]: 
                DFSvisit(v)

        res.append(u) 

        #sprawdzam czy od ostatniego do przedostaniego wierzcholka jest krawedz
        if len(res) > 1:
            if not isEdge(G,res[len(res)-1],res[len(res) - 2]):
                flag = False 



    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(u)
            #nie istnieje ścieżka hamiltona
            if not flag: 
                return False
    
    #zwraca ścieżkę hamiltona
    return res[::-1] 
