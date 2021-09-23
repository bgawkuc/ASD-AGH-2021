#Algorytm do znalezienia silnie spójnych składowych w grafie skierowanym.
#SSS - to taki maksymalny podgraf grafu G (i jednocześnie jego spójna składowa), w którym pomiędzy każdymi 2 wierzchołkami istnieje ścieżka.
#Implementacja dla list sąsiedztwa.

#sortowanie topologiczne, zwraca tablice krotek (czas przetworzenia,wierzchołek)
def DFS(G):
    time = 0
    n = len(G)
    visited = [False] * n
    finish = []

    def DFSvisit(u):
        nonlocal time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSvisit(v)

        time += 1
        finish.append((time,u)) 
        
    for u in range(n):
        if not visited[u]:
            DFSvisit(u)

    return finish

#tworzy graf z odwróconymi krawędziami
def reverse(G):
    n = len(G)
    rev = [[] for _ in range(n)]

    #krawędź u->v zmieniam na v->u
    for u in range(n):
        for v in G[u]:
            rev[v].append(u)

    return rev

def SCC(G):
    n = len(G)
    
    #tablica z sortowania topologicznego posortowana malejąco
    times = sorted(DFS(G))[::-1]

    #graf z odworconymi krawędziami
    rev = reverse(G)

    comp = []
    cnt = 0 #ilosc sss
    visited = [False] * n

    def visit(u): 
        comp[cnt].append(u) #
        visited[u] = True

        for v in rev[u]:
            if not visited[v]:
                visit(v)

    for t in times:
        u = t[1] #wyciagam nr wierzch o maksymalnym czasie przetworzenia
        #jeśli nie był odwiedzony to jest on elementem nowej sss, którą odtwarzam za pomocą pojedyńczego wywołania dfs
        if not visited[u]: 
            comp.append([])
            visit(u)
            cnt += 1
    
    #zwraca ilość sss oraz ich wygląd
    return cnt,comp
