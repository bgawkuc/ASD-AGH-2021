#struktura find-union

#bedziemy tworzyc rozne operacje dla zbiorów
#union - łączy zbiory
#makeSet - tworzy zbior
#find - znajduje te zbiory ktore znajdują sie w zbiorze większym razem

#implemenacja listowa
#kazdy obiekt moze byc reprezentowany jako zbior set
#kazdy ma opce head ktora wskazuje na kolejny el
#oraz zawiera odsylacz do 1 elementu

#make set -> O(1)
#find - > O(1)
#union -> O(n)


#las zbiorów rozłącznych
#mamy zbiory pojedyncze: 1,2,3,4 (drzewa)
#kazdy ma wskaznik który pokazuje na samego siebie
#operacje:
#union(1,2) 2 -> 1, 3, 4
#union(3,4) 2 - > 1, 4 -> 3
#union(2,3) 2 -> 1 <- 3 <- 4
#reprezentant zbioru - główny parent, ten co jest w korzeniu drzewa
#bedziemy stosowac kompresje sciezki - kazdy node ma wskazanie na root dodatkowo
#po to by latwiej bylo znalezc reprezentanta zbioru(korzen)
#bedziemy przechowywac oszacowania na wysykosc dzrewa
#by dodawac mniejsze dzrewa to wiekszych


class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0 #oszacowanie wysokosci
        self.parent = self #wskazanie na rodzica, na poczatku ja jestem swoim rodzicem

#szukam korzenia zbioru
def findSet(x):
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent

#łącze 2 zbiory w 1 (do większego dodaje mniejszy)
def union(x,y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank: #do wiekszego x dodaje mniejszy y
        y.parent = x

    elif y.rank > x.rank: #to większego y dodaje mniejszy x
        x.parent = y

    else: #gdy są równe to wybieram sobie
        x.parent = y #do y dodaje x
        y.rank += 1 #czyli wysokosc y zwiększam o 1


#jesli wykonam m operacji z czego n to make set
#to zlozonosc wynosi O(mlogn)
#zakladajac łączenie wg rank, bez kompresji sciezki

#drzewo o randze rank ma max 2^rank węzłów

#jesli stosujemy obie heurystyki to ciag m operacji z ktorych
#n to make set ma zlozonosc O(mlogn) ~ O(m*alpha(n))
#alpha(n) odlg funkcji Akermanna











