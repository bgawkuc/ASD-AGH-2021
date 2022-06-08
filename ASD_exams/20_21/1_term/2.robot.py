# Robot porusza się po dwuwymiarowym labiryncie i ma dotrzeć z pocycji A = (xa, ya) na pozycję
# B = (xb, yb). Robot może wykonać następujące ruchy:
# 1. ruch do przodu na kolejne pole,
# 2. obrót o 90 stopni zgodnie z ruchem wskazówek zegara,
# 3. obrót o 90 stopni przeciwnie do ruchów wskazówek zegara.
# Obrót zajmuje robotowi 45 sekund. W trakcie ruchu do przodu robot się rozpędza i pokonanie
# pierwszego pola zajmuje 60 sekund, pokonanie drugiego 40 sekund, a kolejnych po 30 sekund na
# pole. Wykonanie obrotu zatrzymuje robota i następujące po nim ruchy do przodu ponownie go
# rozpędzają. Proszę zaimplementować funkcję:
# def robot( L, A, B):
# ...
# która oblicza ile minimalnie sekund robot potrzebuje na dotarcie z punktu A do punktu B (lub
# zwraca None jeśli jest to niemożliwe).
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
# użytego algorytmu.
# Labirynt. Labirynt reprezentowany jest przez tablicę w wierszy, z których każdy jest napisem
# składającym się z k kolumn. Pusty znak oznacza pole po którym robot może się poruszać, a znak
# ’X’ oznacza ścianę labiryntu. Labirynt zawsze otoczony jest ścianami i nie da się opuścić planszy.
# Pozycja robota. Początkowo robot znajduje się na pozycji A = (xa, ya) i jest obrócony w prawo
# (tj. znajduje się w wierszu ya i kolumnie xa, skierowany w stronę rosnących numerów kolumn).

# dp[x][y][i][j] min czas ruchu z (x,y) na (i,j)

from queue import PriorityQueue


def robot(L, A, B):
    dp = [[[[-1 for i in range(3)] for j in range(4)] for x in range(len(L[0]))] for y in range(len(L))]

    # ruchy roznia sie o 90 st kazdy
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # koszty ruchów do przodu
    stepsCost = [60, 40, 30]

    q = PriorityQueue()

    # czas,x,y,kierunek skierowania robota,indeks rozpędzenia
    q.put((0, A[1], A[0], 0, 0))

    while not q.empty():
        # x-wiersz,y-kolumna
        time, x, y, direction, step = q.get()

        if (x, y) == B:
            return time

        if dp[x][y][direction][step] == -1:

            dp[x][y][direction][step] = time

            # dodaje mozliwosc obrotu z niego w lewo lub w prawo do kolejki
            # czas rosnie o 45s
            q.put((time + 45, x, y, (direction + 1) % 4, 0))  # obrót w prawo
            q.put((time + 45, x, y, (direction + 3) % 4, 0))  # obrót w lewo

            # ruch lewo/prawo/góra/dól, zmiana x i y
            x += moves[direction][0]
            y += moves[direction][1]

            # jesli nie trafie na ścianę
            if L[x][y] != 'X':
                # dodaje mozliwosc dojscia do pola od zmienionych wspolrzednych x,y
                # czas rosnie o tyle ile wynosił indeks move w moves(który to był ruch do przodu)
                q.put((time + stepsCost[step], x, y, direction, min(step + 1, 2)))


A = (1, 1)
B = (3, 8)
L = ["XXXXXXXXXX",  # 0
     "X X      X",  # 1
     "X XXXXXX X",  # 2
     "X        X",  # 3
     "XXXXXXXXXX"]  # 4
print(robot(L, A, B))
