#mam macierz m na n która symbolizuj graf
#chce sprawdzic czy da sie dostac z pola 0,0 do pola m-1,n-1
#z pola x,y moge sie poruszyc jedynie w pionie lub poziomie gdy jego wartosc > val
#dla pola (x,y) jego wartosc == G[x][y]

#uruchamiam BFS
#tworze tablice miejsc gdzie byłam
#mam zawsze 4 kierunki
#sprawdzam czy:
#a) dane pole jest w tablicy
#b) nie bylo odwiedzone
#c) ma wartosc wieksza od val
#jesli tak to dodaje je do kolejki


def isInGraph(x,y,n,m): #sprawdza czy pole o wspolrzednych x,y jest w garfie
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    return False

def BFS(G,n,m,val):
    visited = [[False] * m for _ in range(n)]#n-il wierszy, m-il kolumn
    q = []
    q.append((0,0)) #dodaje 1 element
    visited[0][0] = True

    while q:
        el = q.pop(0) #sciagam 1 pare x,y
        x = el[0]
        y = el[1]

        if x == n - 1 and y == m - 1: #gdy znajde sie na ostatnim polu
            return True

        #dla 4 mozliwych pol sprawdzam czy spelniaja warunki a,b,c - jesli tak to trafiaja do kolejki
        if isInGraph(x-1,y,n,m) and G[x-1][y] > val:
            if not visited[x-1][y]:
                visited[x-1][y] = True
                q.append((x-1,y))

        if isInGraph(x+1,y,n,m) and G[x+1][y] > val:
            if not visited[x+1][y]:
                visited[x+1][y] = True
                q.append((x+1,y))

        if isInGraph(x,y-1,n,m) and G[x][y-1] > val:
            if not visited[x][y-1]:
                visited[x][y-1] = True
                q.append((x,y-1))

        if isInGraph(x,y+1,n,m) and G[x][y+1] > val:
            if not visited[x][y+1]:
                visited[x][y+1] = True
                q.append((x,y+1))

    return False #gdy kolejka bedzie pusta a ja nie trafie na ostatnie pole

G = [
    [3,3,3,1],
    [1,1,3,1],
    [1,1,3,3],
]
print(BFS(G,3,4,2)) #czyli moge sie poruszac po pola o wart > 2