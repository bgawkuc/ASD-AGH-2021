# Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
# możliwa sekwencja ruchów spełniająca:
# - każdy ruch kończy się zbiciem skoczka
# - sekwencja kończy się gdy zostanie jeden skoczek.

def knight(A):
    n = len(A)
    G = [[] for _ in range(n)]
    moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    for i in range(n):
        for j in range(n):
            for k in range(8):

                if i != j:
                    x = A[i][0] + moves[k][0]
                    y = A[i][1] + moves[k][1]

                    if x >= 0 and x < n and y >= 0 and y < n:
                        if x == A[j][0] and y == A[j][1]:
                            G[i].append(j)

    visited = [False] * n

    def DFS_visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    DFS_visit(0)

    for i in range(n):
        if visited[i] == False:
            return False

    return True


A = [[0, 0], [1, 1], [1, 2], [2, 3], [3, 0]]
print(knight(A))
