# Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków
# o wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków
# wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i
# uzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
# (ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się
# np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając
# jednego ładunku, to lepsze jest to pierwsze rozwiązanie).

#Sortuje pudełka po wagach rosnąco. Wybieram pudełka od najcięższych.
#Po każdym wybraniu pudełka zmniejszam wartość k o jego wagę oraz zwiększam licznik wybranych pudełek.
#Powtarzam dopóki nie skończą mi sie pudełka lub nie będę w stanie wybrać danego.

def loading(A,k):
    n = len(A)
    # =sortuje tablice A rosnaca
    A.sort()
    cnt = 0 
    #zaczynam od najciezszego pudelka
    idx = n - 1

    while k > 0 and idx >= 0:
        
        #gdy waga pudelka nie przekracza pojemnosci
        if k >= A[idx]:
            cnt += 1
            k -= A[idx]
        idx -= 1

    return cnt
