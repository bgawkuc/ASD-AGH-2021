#sprawdz czy graf jest dwudzielny
#rownowazne kolorowaniu grafu 2 kolorami
#tak by zadne 2 sasiednie wierzcholki nie były tego samego koloru
#kolruje wiezrcholki na dwa kolor: 0 i 1
#gdy zdarza sie ze rodzic i dzieci mają ten sam kolor tzn ze nie jest dwudzielny
#gdy taka sytuacja nigdy nie nastąpi tzn ze jest on dwudzielny

from queue import Queue
def BFS(G,s):
    q = Queue()
    visited = [False] * len(G)
    color = [-1] * len(G)

    q.put(s)
    visited[s] = True
    color[s] = 1 #1 kolor

    while not q.empty():
        u = q.get()

        for v in G[u]:

            if not visited[v]:
                visited[v] = True
                color[v] = 1 - color[u] #jego dziecko koloruje na kolor inny
                q.put(v)

            if color[u] == color[v]: #gdy kolor dziecka i rodzica jest ten sam
                return False

    return True



#dwudzielny
G = [
    [1,3],
    [0,5,4],
    [5],
    [0],
    [1,6],
    [2,6,1],
    [4,5],
]
#nie jest dwudzielny przez krawędź 4-5
G1 = [
    [1,3],
    [0,5,4],
    [5],
    [0],
    [1,6,5],
    [2,6,1,4],
    [4,5],
]


print(BFS(G,0))


#implementacja macierzowa
def BFS2(G,s):
    q = Queue()
    visited = [False] * len(G)
    color = [-1] * len(G)

    q.put(s)
    visited[s] = True
    color[s] = 1  # 1 kolor

    while not q.empty():
        u = q.get()

        for v in range(len(G)):
            if u != v and G[u][v] == 1 and not visited[v]:
                visited[v] = True
                color[v] = 1 - color[u]  # jego dziecko koloruje na kolor inny
                q.put(v)

            if G[u][v] == 1 and u != v and color[u] == color[v]:  # gdy kolor dziecka i rodzica jest ten sam
                return False

    return True

#taki sam jak G
G2 = [
    [0,1,0,1,0,0,0],
    [1,0,0,0,1,1,0],
    [0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,0,1],
    [0,1,1,0,0,0,1],
    [0,0,0,0,1,1,0],
    ]
#taki sam jak G1
G3 = [
    [0,1,0,1,0,0,0],
    [1,0,0,0,1,1,0],
    [0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,1,1],
    [0,1,1,0,1,0,1],
    [0,0,0,0,1,1,0],
    ]

# print(BFS2(G3,0))