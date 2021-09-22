#chce znalezc najdluzszy podciag rosnacy w tablicy (niekoniecznue spojny!!)

#tworze tablice z cnt dlg wejsciowej tablicy, gdzie wartosc ustawiam na 1
#tworze tablice p w ktorej bede zapamietywac indeksy sciezki, wtedy gdy wartosc cnt[i] >= 2
#przechodze po tab wejsciowej 2 petlami
#j ustawiam na 1 element, i na 2 element
#jesli t[j] < t[i] to wartosc cnt[i] = max(cnt[i], cnt[j]+1)
#j przechodzi od 0 az do indeksu i - 1
#i tak az nie przejde calej tablicy z i
#f(n) = max{F(i): i < n; A[i] < A[n]} + 1

#tworze tablice cnt[i] w ktorej zliczam lis konczacy sie na i
#sprawdzam wszystkie el na lewo od i
#gdy el T[j] jest < T[i] oraz
#cnt[j] + 1 > cnt[i] (zeby przypadkiem nie zamienic na krotszy ciąg)
#to wtedy aktualizuje wartosc cnt[i]
#tablica p pomaga mi odwtarzac rozw
#w 1 sposobie zapamietuje idx przedostaniego elementu tworzacego lis
#w 2 sposobie dla kazdego i zapamietuje wyglad calej sciezki konczowej sie na i
#O(n^2)


#1 spsosob gdy rozwiazanie odtwarzam na sam koniec
def lis(T):
    n = len(T)
    cnt = [1] * n #szuka ile elementow tworzy z danym el lis
    p = [-1] * n  #zapamietuje sciezke rozwiazania -zapisuje indeksy, jaki ostatnio idx tworzył z nim lis

    for i in range(1,n):
        for j in range(i):
            if T[j] < T[i] and cnt[j] + 1 > cnt[i]: #jesli spełnia warunek lis i wartosc jego ind + 1 jest wieksza od obecnego ind
                cnt[i] = cnt[j] + 1 #to zmieniam wartosc max dlg lis
                p[i] = j #idx przedostatniego el w lis

    maxi = 0
    for i in range(1,len(cnt)): #szukam dla jakiego idx konczy sie najdluszy ciąg
        if cnt[i] > cnt[maxi]:
            maxi = i

    return max(cnt), cnt, p, maxi #max(cnt)-dlg najdluzszego podciagu, cnt-tab z ilosciami el wiekszych, p-tab z sciekzami


def printsolurion(T,p,i): #wypisuje rozw, i - indeks najw elementu z p, p-tab zapamietanych poprzednich idx
    if p[i] != -1: #dopoki p[i] != -1, dopoki w tej sciezce jest zapisany indeks
        printsolurion(T,p,p[i])
    print(T[i],end=" ")


t = [8,1,4,2,6,5,8,0]
t1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
t2 = [2,1,4,3]
a = [1,0,9,8,7,2,0,1,4,8,6]


value, cnt, p, maxi = lis(a)
# print(value,cnt,p,maxi)
# printsolurion(a,p,maxi)
print(lis(t))

#2 sposob gdy na biezaco odtwrzam rozwiazania
def lis2(T):
    n = len(T)
    cnt = [1] * n  # szuka ile elementow tworzy z danym el lis
    p = [[] for _ in range(n)] # zapamietuje sciezke roziwazania dla kazdego i


    for i in range(1, n):
        for j in range(i):
            if T[j] < T[i] and cnt[j] + 1 > cnt[i]:  # jesli spełnia warunek lis i wartosc jego ind + 1 jest wieksza od obecnego ind
                cnt[i] = cnt[j] + 1  # to zmieniam wartosc max dlg lis
                p[i].append(T[j])  #dodaje taki element do sciezki

    #szukam dla jakiego idx mam lis czyli dla jakiego idx cnt ma max wartosc
    maxi = 0
    for i in range(n):
        if cnt[i] > cnt[maxi]:
            maxi = i
    # kazda sciezka konczaca sie na i musi sie skladac z el T[i] więc go dodaje na koniec bo musi byc najwiekszy
    p[maxi].append(T[maxi])

    return cnt[maxi], p[maxi]


# t = [8,1,4,2,6,5,8,0]
t11 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
t22 = [2,1,4,3]
# print(lis2(t11))




