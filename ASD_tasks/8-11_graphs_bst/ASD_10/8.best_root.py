#mam drzewo z WAŻONYMI krawędziami, wagi to liczby naturalne
#drzewo to graf spójny, acykliczny, nieskierowany
#muszę znaleźć taki wierzchołek dla ktorego
#odleglosc(w sensie suma wag krawędzi) do najdalszego wierzcholka jest minimalna

#czyli najpierw nalezy znaleźć najdłuższą ścieżkę w grafie(w sensie największą wagowo)
#za pomocą BFS z fałszywymi wierzchołkami
#raz puszczam go od 0
#znajduje wierzch najdalszu od 0 -> u
#dla u znowu puszczam BFS z falszywymi wierzchołkami
#znajduje najdalszy wierzchołek od u -> v
#u-v to końce ścieżki o max wadze
#a potem na tej ścieżce szukam takiego wierzchołka,
#który ją dzieli na dwie części najbardziej mozliwie równe (np podział na 6 i 8 jest lepszy od podziału na 10 i 4)
#i taki wierzchołek będzie najlepszym korzeniem
#UWAGA-ZŁOŻONOŚĆ O(MAX KRAWĘDŹ*(V+E)) -> moze byc potencjalnie bardzo duza (to zlozonosc BFS ze sztucznymi wierzcholkami)
#trzeba znaleźć lepszy sposób na szukanie max sciezki



#NAJLEPSZA ZLOZONOSC
#BO DFS TO O(V+E) BO JEST TO DRZEWO - ISTNIEJE TYLKO 1 SCIEZKA MIEDZY 2 DOWOLNYMI WIERZCHOŁKAMI
def dfs(G, s):
    n = len(G)
    visited = [False] * n
    dist = [-1] * n
    dist[s] = 0
    parent = [None] * n

    def dfsVisit(u):
        visited[u] = True

        for v, edge in G[u]:
            if not visited[v]:
                dist[v] = dist[u] + edge
                parent[v] = u
                dfsVisit(v)

    dfsVisit(s)
    return dist, parent


def bestRoot(G):
    n = len(G)
    d1, _ = dfs(G, 0)

    # szukam wierzcholka u - najbardziej oddalonego od 0
    u = 0
    for i in range(1, n):
        if d1[i] > d1[u]:
            u = i

    # dla u odpalam dfs
    d2, parent = dfs(G, u)
    print(d2)

    # szukam wierzcholka v - najbardziej oddalonego od u
    v = u
    for i in range(n):
        if d2[i] > d2[v]:
            v = i

    # sciezka od u do v to srednica dlugosci length
    # odtwarzam ją
    length = d2[v]
    path = []
    curr = v
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]

    # najlepszy wierzchloek i min roznica
    root = u
    diff = length

    # szukam najlepszego wierzcholka
    # czyli takiego wierzchołka który dzieli srednice na 2 czesci o min roznicy
    for u in path:
        left = d2[u]
        right = length - left
        if abs(left - right) < diff:
            diff = abs(left - right)
            root = u

    return diff, root


#ZŁOŻONOŚĆ O(MAX KRAWĘDŹ*(V+E)) -> potencjalnie BARDZO DUŻA
from queue import Queue

def bfsFalseVertex(G, s):
    n = len(G)
    q = Queue()
    visited = [False] * n
    parent = [None] * n
    dist = [0] * n

    # wierzcholek,ilosc sztucznych,rodzic,oryginalna dlg krawedzi
    q.put((s, 0, None, 0))

    while not q.empty():
        u, cntFalse, par, edge = q.get()
        if q.empty():
            q = Queue()

        if cntFalse > 0:
            q.put((u, cntFalse - 1, par, edge))

        else:

            if not visited[u]:
                visited[u] = True
                if par is None:
                    dist[u] = edge
                else:
                    dist[u] = dist[par] + edge
                    parent[u] = par

            for v, edge in G[u]:
                if not visited[v]:
                    q.put((v, edge - 1, u, edge))

    return dist, parent


def longestPath(G):
    n = len(G)
    # puszczam bfs od 0 i szukam najdalej oddalone wierzcholka od niego
    d1, _ = bfsFalseVertex(G, 0)
    u = 0
    for i in range(n):
        if d1[i] > d1[u]:
            u = i

    # puszczam bfs od u i szukam najdalej oddalonego wierzchołka od niego
    d2, parent = bfsFalseVertex(G, u)
    v = u
    for i in range(n):
        if d2[i] > d2[v]:
            v = i

    # u,v - krance
    path = []
    curr = v
    length = d2[v]

    # odtwarzam sciezke
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]

    root = None
    diff = float('inf')

    # szukam takiego wierzcholka dla ktorego roznica lewej i prawej 'polowy' jest minimalna
    for i in range(1, len(path)):
        left = d2[path[i]]
        right = length - left

        if abs(right - left) < diff:
            diff = abs(right - left)
            root = path[i]

    return root, path


#[vertex,edge]
G = [
    [[2,1]],
    [[2,10]],
    [[0,1],[1,10],[3,1]],
    [[2,1],[4,2]],
    [[3,2],[5,1],[6,1]],
    [[4,1]],
    [[4,1]],
]
#sciezka maxi: 1-2-3-4-5
#best root - 2: dzieli na 10 i 4

G1 = [
    [[2,1]],
    [[2,3]],
    [[0,1],[1,3],[3,4]],
    [[2,4],[4,3]],
    [[3,3],[5,1],[6,5]],
    [[4,1]],
    [[4,5]],
]
#sciezka maxi: 1-2-3-4-5
#best rootm - 3: dzieli na 7 i 8
# print(longestPath(G))


#inny spsoob na znalezienie dlg max sciezki;
#tylko nie umiem jej odtwarzac
#dobrze wyznacza dłuogość
#źle wyznacz start i end
def longestPath2(G):
    maxVal = 0
    bestS = None
    bestE = None
    visited = [False] * len(G)

    def path(G,u):
        nonlocal maxVal,bestS,bestE
        visited[u] = True

        max1, max2 = 0, 0 #najdłuzsza i prawie najdluzsza sciezka
        s1, s2, e1, e2 = None, None, None, None

        for i in range(len(G[u])):
            if not visited[G[u][i][0]]:
                maxi, s, e = path(G,G[u][i][0])
                currMax = maxi + G[u][i][1]

                if currMax > max1:
                    max1, max2 = currMax, max1
                    s1, s2, e1, e2 = G[u][i][0], s1, u, e1
                    # print("1:",max1,s1,e1)

                elif currMax > max2:
                    max2 = currMax
                    s2, e2 = G[u][i][0], u
                    # print("2:", max2,s2,e2)

        if max1 + max2 > maxVal:
            maxVal = max1 + max2
            bestS = s1
            bestE = e2


        return max1, s1, e1

    path(G,0)
    return maxVal, bestS, bestE

G2 = [
    [[2,1]],
    [[2,10]],
    [[0,1],[1,10],[3,1]],
    [[2,1],[4,2]],
    [[3,2],[5,1],[6,1]],
    [[4,1]],
    [[4,1]],
]
print(longestPath(G2))