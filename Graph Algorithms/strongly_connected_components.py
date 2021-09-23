#silnie spójne składowe
#w grafie skierowanym
#niech G= (V,E) bedzie gr skierowanym
#mowimy ze wierzcholki u,v naleza do tej samej silnej spojnej skladowej
#jesli istnieją sciezki skierowane z u do v oraz z v do u

#czyli np 3 cykle trojkaty polaczone ze soba krawędziami
#i kazdy taki cykl bylby silnie spójną składową

#wykonuje sortowanie topologiczne
#i odwracam wszystkie krawędzie
#wtedy zaczynam odcinac po kolei wierzcholki z ktorych nie da sie przejsc dalej
#i przydzielam im jakies numery kolejne

#algorytm
#wykonaj dfs dla grafu wejsciowego zapisujac w wierzcholkach czas przetworzenia
#odwróć kolejność krawędzi
#wykonaj dfs drugi raz w kolejnosci malejacych czasow przetworzenia(petla visited-dziala w tej kolejnosci)
#gdy nie bede miała ruchu tzn ze znalzlam silnie spojną składową


#DFS w ktorym zapisuje czas przetworzenia -> 1 krok
def DFS(G):
    time = 0
    n = len(G)
    visited = [False] * n
    finish = [None] * n

    def DFSvisit(u):
        nonlocal time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSvisit(v)

        time += 1
        finish[u] = (time,u) #czas przetworzenia, wierzcholek

    for u in range(n):
        if not visited[u]:
            DFSvisit(u)

    return finish

#funkcja która odwraca krawędzie
#tworzy nowy graf rozmiaru starego
def reverse(G):
    n = len(G)
    rev = [[] for _ in range(n)]

    #krawędź u->v zmieniam na v->u
    for u in range(n):
        for v in G[u]:
            rev[v].append(u)

    return rev

#znajduje ilosc scc i je wypisuje
def components(G):
    n = len(G)
    #tablica czasow przetworzenia posortowana malejąco
    times = sorted(DFS(G))[::-1]

    #graf z odworconymi krawędziami
    rev = reverse(G)

    comp = [] #tablice z wierzch sss
    cnt = 0 #ilosc sss
    visited = [False] * n

    def visit(u): #zqykly DFSvisit
        comp[cnt].append(u) #dodaje wierzch do i-tej sss
        visited[u] = True

        for v in rev[u]:
            if not visited[v]:
                visit(v)

    for t in times:
        u = t[1] #wyciagam nr wierzch o max czasie przetworzenia
        if not visited[u]: #i jesli nie był on odwiedzony
            comp.append([])
            visit(u)#to dla niego wywoluje dfsvisit i od niego zacznie sie sss
            cnt += 1

    return cnt,comp

G = [
    [2,4],
    [9,0],
    [1],
    [4,6],
    [5],
    [3],
    [5],
    [3,9],
    [7],
    [10],
    [8],
]



print(components(G))





