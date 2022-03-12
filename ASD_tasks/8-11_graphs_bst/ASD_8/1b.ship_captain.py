# Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.


def BFS(G, val):
    n = len(G)
    m = len(G[0])
    visited = [[False] * m for _ in range(n)]
    q = []
    q.append((0, 0))
    visited[0][0] = True

    def isIn(x, y):
        return n > x >= 0 and m > y >= 0

    while q:
        x, y = q.pop()

        if x == n - 1 and y == m - 1:
            return True

        if isIn(x - 1, y) and G[x - 1][y] > val:
            if not visited[x - 1][y]:
                visited[x - 1][y] = True
                q.append((x - 1, y))

        if isIn(x + 1, y) and G[x + 1][y] > val:
            if not visited[x + 1][y]:
                visited[x + 1][y] = True
                q.append((x + 1, y))

        if isIn(x, y - 1) and G[x][y - 1] > val:
            if not visited[x][y - 1]:
                visited[x][y - 1] = True
                q.append((x, y - 1))

        if isIn(x, y + 1) and G[x][y + 1] > val:
            if not visited[x][y + 1]:
                visited[x][y + 1] = True
                q.append((x, y + 1))

    return False
