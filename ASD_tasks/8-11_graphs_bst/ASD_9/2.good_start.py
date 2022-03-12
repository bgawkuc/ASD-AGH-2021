# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można 
# osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf zawiera dobry początek.

# Wywołuje DFS dla grafu i zapisuje czas przetworzenia każdego wierzchołka.
# szukam wierzchołka, dla którego czas przetworzenia wynosi tyle co rozmiar grafu - jest od potencjalny dobry początek.
# Dla takiego wierzchołka wywołuje DFS i sprawdzam czy zostaną odwiedzone wszystkie wierzchołki.

def goodStart(G):
    n = len(G)
    finish = [-1] * n
    visited = [False] * n
    time = 0

    def dfsVisit(u):
        nonlocal time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfsVisit(v)

        time += 1
        finish[u] = time

    for u in range(n):
        if not visited[u]:
            dfsVisit(u)

    for u in range(n):
        if finish[u] == n:
            visited = [False] * n
            dfsVisit(u)

            for i in range(n):
                if visited[i] == False:
                    return False
            return True, u

    return False
