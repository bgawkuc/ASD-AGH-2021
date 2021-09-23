#mam tablice 1D z miastami
#kazde miasto ma wartosc 0 lub 1
#w miastach oznaczonych 1 jest mozliwe zbudowanie maszyny chroniacej
#mam tez wartosc k ktora mowi ze jesli w i postawimy maszyne
#to miasta abs(i-j) < k sa chronione
#napisz algorytm ktory mowi ile najmniej maszyn mozna zbudowac
#by wszystkie miasta byly chronione

#last - miejsca w ktorych wybudowano maszyne
#notprotected-patrze do przodu szukajac mozliwie najdalszego miejsca(idx) by zbudowac maszyne
#od notprotected w dol szukam 1 miejsca na ktorym jest 1
#tam stawiam maszyne
#wiec last dostaje wartosc notprotected
#a not protected zwiekszam o 2k-1(najdalsze miejsce by ustawic nową maszyne)
#bo ta daleka maszyna chroni k - 1 miast w tył a ta inna k - 1 miast w przód
#i tak dopoki miejsce ustawienia ostatniej maszyny jest < n - k


def machines(A,k):
    n = len(A)
    lastMach = -1 #idx gdzie ostatnio wybudowalam maszyne
    cnt = 0
    machine = k - 1 # najdalszy idx na ktorym moge probowac ustawic maszyne

    while lastMach < n - k: #dopoki ostatnie k miast nie jest chronionych

        if machine >= n: #gdy wyjde poza zakres z miejscem dla maszyny
            machine = n - 1

        while A[machine] != 1 and machine != lastMach:#probujemy mozliwie jak najdalej umiescic maszyne
            #drugi warunek-po to by nie pokryła sie ona z moja obecną maszyną
            #gdy nie da sie na miejscu ustawic maszyny(bo ma wart 0) to przesuwam sie w lewo
            machine -= 1

        #gdy przeszłam wszystkie 2k - 1/ k - 1(przy 1 maszynie) pól z przodu i nie znazłam miejsca tzn ze nie jest to możliwe
        if machine == lastMach: #moment gdy nie ma pola 1 w wybranym obszarze tzn nie bedzie dalo sie spelnic warunkow
            return -1

        lastMach = machine #miejsce w ktorym umieszczam maszyne
        machine += 2 * k - 1 #najdalszy idx miasta w ktorym mozna probowac wybudowac maszyne
        cnt += 1

    return cnt

#CZYTELNIEJSZA IMPLEMENTACJA
def machines2(A,k):
    n = len(A)

    #szukam miejsca dla 1 maszyny
    first = None
    for i in range(k-1,-1,-1):
        if A[i] == 1:
            first = i
            break

    if first is None:
        return False
    mach = [first]

    #do jakiego indeksu mam chronione
    protected = first + k - 1

    #dopoki nie wszystkie pola są chronione
    while protected < n-1:

        new = None
        #szukam jak najdalszego miejsca na maszyne
        for i in range(protected+k-1,protected,-1):
            if i < n and A[i] == 1:
                new = i
                mach.append(i)
                break

        #jesli nie ma takiego miejsca
        if new is None:
            return False
        else:
            protected = new + k - 1

    return mach

arr=[1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0]
a = [1,1,0,1,0,1,0]
print(machines(arr,3))


