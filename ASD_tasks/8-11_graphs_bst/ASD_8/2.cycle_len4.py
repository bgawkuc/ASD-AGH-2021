#mamy macierz sasiedztwa reprezentującą graf nieskierowany
#znajdz algorytm ktory znajduje cykl dlg 4
#zakladam ze ma on taki cykl posiada

#wywoluje od kazdego wierzcholka dfs
#jako start zapamietuje 1 wierzcholek
#przechodze po jego sasiadach
#gdy jakis sasiad posiada z nim krawedz a licznik dlg cyklu jeszcze nie wyniosl 0 to
#to ustalam ze on jest kolejną krawędzią i zapisuje jako jego rodzic start
#powtzram tę procedure dopoki dlg cyklu nie wyniesie 0
#i wtedy bede sprawdzac czy znaleziony wierzch ma krawedz z startowym
#jesli tak tzn ze znalazlam cykl

def cycleOfLength4(G):
    n = len(G)
    res = [-1] * 4 #znaleziony cykl

    def DFSvisit(G,x,parent,cnt=3):
        nonlocal n, start
        res[cnt] = x #wierzcholek startowy daje jako ost el cyklu
        if cnt >= 0: #gdy jeszcze cykl ma szanse powstac
            for i in range(n): #patrze na jego sąsiadow

                # gdy szukam sciezki
                if G[x][i] == 1 and i != start and i != parent and cnt != 0:
                    DFSvisit(G,i,x,cnt-1)

                # ostatnia krawedz, gdy mam juz sciezke dlg 4, a start i koniec sa rowne
                elif G[x][i] == 1 and i == start and cnt == 0:
                    print(res)
                    exit(0)

    for u in range(n): #wywoluje dla kazdego wierzcholka
        start = u
        DFSvisit(G,u,u)

G = [
    [0,1,1,0,0,1],
    [1,0,0,1,0,0],
    [1,0,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,0,1],
    [1,0,0,0,1,0],
]
cycleOfLength4(G)