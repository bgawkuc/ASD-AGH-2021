# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w Polsce. Jednym z głównych elementów
# całej procedury jest wyłaczenie wszystkich stacji nadawczych (które tworza spójny graf połaczen). Ze wzgledów
# technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo zalezy na tym, by podczas całego procesu 
# wszyscy abonenci znajdujacy sie w zasiegu działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). 
# Proszę zaproponować algorytm podający kolejność wyłączania stacji.

#Należy określić kolejność usuwania wierzchołków tak, by graf na każdym etapie pozostał spójny. 
#Za pomocą DFS zapamiętuje czas odwiedzenia każdego wierzchołka. 
#Aby spełnić warunki zadania należy usuwać wierzchołki zaczynając od tych o największym czasie odwiedzenia. 

def DFS(G, s):
    time = 0
    visited = [False] * len(G)
    order = [0] * len(G)

    def DFS_visit(u):
        nonlocal time
        time += 1
        visited[u] = True
        order[u] = time

        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    DFS_visit(s)
    res = []

    for i in range(len(order)):
        res.append((i, order[i]))

    res.sort(key=lambda x: x[1], reverse=True)

    # kolejnosc usuwania - od najwiekszych czasow wejscia
    for i in range(len(order)):
        print(res[i][0], end=" ")

    return
