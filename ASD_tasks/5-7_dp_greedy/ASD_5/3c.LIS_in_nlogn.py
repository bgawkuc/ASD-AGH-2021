#najwiekszy podciag rosancy ale o zloznonosci nlogn
#chcemy wyszukiwac binarnie by miec nlogn
#T[i] - najmniejsza wartosc konczaca ciag rosnacy dlg i
#dla ciagu 3,5,1,8,2,4,7,6,1,3
#a) jak liczba jest mniejsza od najmniejszej to najmniejsza zastepuje nia
#b) jak liczba jest wieksza od najw to wpisuje za najwwieksza
#c) jak liczba jest pomiedzy to binarnie wyszukuje i zastepuje liczbe jakas nia
#curr = 3
#5 > 3 (b) wiec curr = 3, 5
#1 < 3 (a) wiec curr = 1, 5
#8 > 5 (b) wiec curr = 1 5 8
#2 > 1 i 2 < 5 (c) wiec curr = 1 2 8
#4 > 2 i 4 < 8 (c) wiec curr = 1 2 4
#7 > 4 (b) wiec curr = 1 2 4 7
#6 > 4 i 6 < 7 (c) wiec curr = 1 2 4 6
#1 <= 1 wiec (c) curr = 1 2 4 6
#3 > 2 i 3 < 4 (c) wiec curr = 1 2 3 6

#dlg curr = 4
#czyli LIS to 4
#zlozonosc O(nlogn)
#bo binsearch ktorego uzywam w curr ma zloz O(log(len(curr)) <= O(logn)

#UWAGA POPRAWNIE ZNAJDUJE DŁG ALE CZASEM ZNALEZIONY CIĄG JEST NIEPOPRAWNY!!

#wyszukiwanie binarne O(logn)
def binSearch(A,l,r,val):
    while (r - l) > 1:
        mid = l + (r - l) // 2

        if A[mid] >= val:
            r = mid
        else:
            l = mid
    return r #w jakim powinnam wstawic wartosc val

def LIS(A):
    n = len(A)
    tail = [None] * (n + 1) #moj LIS
    tail[0] = A[0] #1 liczba w LIS to na poczatku 1 liczba w A
    length = 1 #dlg LIS

    for i in range(1,n): #przechodze liniowo po A

        if A[i] < tail[0]: #gdt znaleziony element jest mniejszy od najmniejszego to najmn zastepuje niim
            tail[0] = A[i]

        elif A[i] > tail[length-1]: #gdy jest wiekszy od najw do daje go za najw i zwiekszam dlg
            tail[length] = A[i]
            length += 1

        else: #gdy jest pomiedzy to znajduje miejsce w ktore nalezy to wpisac(zastepuje jakąś liczbe moją A[i])
            tail[binSearch(tail, -1, length-1, A[i])] = A[i]


    return length #zwraca długosc lIS

t = [8,1,4,2,6,5,8,0]
t1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(t))
