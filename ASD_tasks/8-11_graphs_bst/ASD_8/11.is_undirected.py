#sprawdza czy z kazdego wierzcholka tyle samo krawedzi wychodzi co wchodzi
#czyli czy dla kazdej u -> v istnieje krawedz u <- v
#graf reprezentowany jako listy sąsiedztwa

#dla kazdego wierzcholka sprawdzam ile krawedzi z niego wychodzi
#gdy trafie na jakis wierzcholek to zmniejszam jego wartosc o 1 bo znaczy zejakas krawedz do niego wchodzi
#jak cala tablica res ma wart 0 tzn ze warunek z tresci jest spełniony


#reprezentacja przez listy sąsiedztwa
class Graph:
    def __init__(self,size):
        self.size = size
        self.arr = [[i] for i in range(size)]

    def addEdge(self,v,u):
        self.arr[v].append(u)

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print("\n")


def isUndirected(G):
    res = [0] * len(G.arr)

    for v in G.arr:
        print(v)
        res[v[0]] += (len(v)-1) #zwiekszam o tyle ile wychodzi krawedzi z wierzcholka

        for vertex in v[1:]:
            res[vertex] -= 1 #zmniejszam licznik wierzcholka do  ktorego wchodzi krawedz

    # print(res)
    for el in res:
        if el != 0:
            return False

    return True

#ten jest nie ok
G = [[1, 2], [0], [0, 3, 4], [2, 5], [2], [5]]
#ten jest ok
G1 = [[1, 2], [0], [0, 3, 4], [2, 5], [2], [3]]
G2 = [[1,2],[0],[0,3],[2]]
G3 = [[1,2],[2,0],[0,1]]
#ok
g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(3,2)
g.addEdge(3,5)
g.addEdge(4,2)
g.addEdge(5,3)

#ten nie jest ok
g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
g1.addEdge(1,0)
g1.addEdge(2,0)

print(isUndirected(g))