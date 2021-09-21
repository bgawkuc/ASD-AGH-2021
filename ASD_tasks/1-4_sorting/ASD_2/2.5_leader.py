#(Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
#O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A
#na ponad połowie pozycji

#tworze zmienne idx_leader(indeks lidera) oraz cnt(ilosc wystapien)
#przechodze liniowo tablice
#jesli cnt wynosi 0 to obecny idx ustawiam na idx leader i cnt zwiekszam o 1
#jesli wartosc pola na ktorym jestem odpowiada T[idx_leader] czyli tyle ile pole lidera to cnt zwiekszam o 1
#w pozostłaych przypadakch cnt zmniejszma o 1
#na koniec tablica mi zwroci idx POTENCJALNEGO lidera
#i potem jeszcze raz liniowo przechodze tablice i sprawdzam ile razy on wystąpił
#jesli liczba jego wystąpień jest >= dlg polowy tablicy to jest on liderem


def leader(T):
    cnt = 0 #ilosc wystapien
    ind_leader = 0 #idx lidera

    for i in range(len(T)):
        if cnt == 0:
            ind_leader = i
            cnt += 1
        elif T[i] == T[ind_leader]:
            cnt += 1
        else:
            cnt -= 1

    return ind_leader


def more_than_half(T):
    ind = leader(T)
    cnt = 0
    for i in range(len(T)):
        if T[i] == T[ind]:
            cnt += 1
    if cnt > len(T) // 2:
        return True
    return False

T = [1,1,2,2,2]
print(more_than_half(T))