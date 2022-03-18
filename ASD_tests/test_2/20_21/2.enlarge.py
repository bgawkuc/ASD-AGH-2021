# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
# zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję:
# def enlarge(G, s, t):
# ...
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
# warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
# sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
# Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
# krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
# nie było ścieżki z s do t to funkcja powinna zwrócić None.


from queue import Queue


def bfs(G, s):
    n = len(G)
    visited = [False] * n
    dist = [float('inf')] * n
    q = Queue()

    q.put(s)
    dist[s] = 0
    visited[s] = True

    while not q.empty():
        u = q.get()

        for v in G[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.put(v)

    return dist


def bridge(G):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    d = [-1] * n
    l = [-1] * n
    time = 0

    def dfVisit(u):
        nonlocal time
        visited[u] = True
        time += 1
        d[u] = l[u] = time

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfVisit(v)

                l[u] = min(l[u], l[v])

            elif visited[v] and parent[u] != v:
                l[u] = min(l[u], d[v])

    for u in range(n):
        if not visited[u]:
            dfVisit(u)

    for u in range(n):
        if d[u] == l[u] and parent[u] is not None:
            return parent[u], u
    return None


def enlarge(G, s, t):
    n = len(G)
    fromS = bfs(G, s)
    fromT = bfs(G, t)

    mini = fromS[t]

    # buduje graf najkrótszych ściezek
    newG = [[] for _ in range(n)]

    # jesli odleglosc od s do u i od u do t wynosi tyle co dlg min sciezki
    # jesli odleglosc od s do v i od v do t wynosi tyle co dlg min sciezki
    # to krawedz u-v nalezy do grafu najkrótszych sciezek
    for u in range(n):
        for v in G[u]:
            if fromS[u] + fromT[u] == mini and fromS[v] + fromT[v] == mini:
                newG[u].append(v)

    # szukam w nim mostów
    return bridge(newG)

#(0,2)
G = [
    [1, 2],
    [0, 2],
    [0, 1],
]
s = 0
t = 2

#None
G2 = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]  # 5
s2 = 0
t2 = 3
print(enlarge(G,s,t))