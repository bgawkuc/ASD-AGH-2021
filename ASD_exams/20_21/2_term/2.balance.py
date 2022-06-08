# mam zadane ważone drzewo w którym kazda krawędź ma swój numer
# zwroc numer krawędzi której usunięcie podzieli mi to drzewa na 2 o min roznicy wag
# mam np wierzchołek A,
# A.edges - węzły jakie od niego wychodzą
# A.weights - odpowiednie wagi jakie mam do tych innych węzłów
# A.ids - odpowiednie 'nazwy' krawędzi

class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.sum = 0

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)


def balance(T):
    # (rozmiar drzewa jakie jest pod krawędzią edge,edge,numer krawędzi edge)
    A = []

    def find(node, edge, idx):
        treeWeight = 0

        # gdy z node nie wychodzą zadne krawędzie
        if len(node.edges) == 0:
            A.append((treeWeight, edge, idx))
            return treeWeight + edge

        for i in range(len(node.edges)):
            treeWeight += (find(node.edges[i], node.weights[i], node.ids[i]))

        if idx is not None:
            A.append((treeWeight, edge, idx))

        return treeWeight + edge

    totalTree = find(T, 0, None)

    minDiff = float('inf')
    bestId = None

    # szukam numeru krawędzi dla której różnica rozmiarów drzew jest minimalna
    for tree1, edge, idx in A:
        tree2 = totalTree - (tree1 + edge)

        if minDiff > abs(tree1 - tree2):
            minDiff = abs(tree1 - tree2)
            bestId = idx

    return bestId


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.addEdge(B, 6, 1)
A.addEdge(C, 10, 2)
B.addEdge(D, 5, 3)
B.addEdge(E, 4, 4)
print(balance(A))
