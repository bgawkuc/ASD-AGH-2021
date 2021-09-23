# Dany jest zbiór punktów X = {x1, . . . , xn} na prostej. Proszę podać algorytm, który znajduje minimalną 
# liczbę przedziałów jednostkowych domkniętych, potrzebnych do pokrycia wszystkich punktów z X.
# (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
 
#Należy posortować punkty rosnaco i jako start ustawić pierwszy punkt, dopóki punkty są <= od start+1
#to jedynie przechodzę tablicy. Gdy zaczną być większe to aktualizuje start, zwracam ilość róznych wartości start.

def ranges(A):
    n = len(A)
    A.sort()
    idx = 0
    cnt = 0

    while idx < n:
        cnt += 1
        end = A[idx] + 1

        while idx < n and A[idx] <= end:
            idx += 1

    return cnt
