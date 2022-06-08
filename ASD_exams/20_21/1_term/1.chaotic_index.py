# Mówimy, że tablica T ma współczynnik nieuporządkowania równy k (jest k-Chaotyczna), jeśli spełnione są łącznie dwa warunki:
# 1. tablicę można posortować niemalejąco przenosząc każdy element A[i] o co najwyżej k pozycji
# (po posortowaniu znajduje się on na pozycji różniącej się od i co najwyżej o k),
# 2. tablicy nie da się posortować niemalejąco przenosząc każdy element o mniej niż k pozycji.
# Proszę zaproponować i zaimplementować algorytm, który otrzymuje na wejściu tablicę liczb rzeczywistych T i zwraca jej
# współczynnik nieuporządkowania. Algorytm powinien być jak najszybszy
# oraz używać jak najmniej pamięci. Proszę uzasadnić jego poprawność i oszacować złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
# def chaos_index( T ):
# ...
# przyjmującą tablicę T i zwracającą liczbę całkowitą będącą wyznaczonym współczynnikiem nieuporządkowania.


def partition(A, l, r):
    piv = A[r][0]
    pivIdx = A[r][1]
    i = l

    for j in range(l, r):
        if A[j][0] < piv:
            A[i], A[j] = A[j], A[i]
            i += 1

        elif A[j][0] == piv:
            if A[j][1] < pivIdx:
                A[i], A[j] = A[j], A[i]
                i += 1

    A[i], A[r] = A[r], A[i]
    return i


def quickosort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        quickosort(A, l, q - 1)
        quickosort(A, q + 1, r)
    return A


def chaoticIndex(A):
    n = len(A)

    for i in range(n):
        A[i] = [A[i], i]

    sortedA = quickosort(A, 0, n - 1)
    maxiDif = -float('inf')

    for i in range(n):
        maxiDif = max(maxiDif, abs(i - sortedA[i][1]))

    return maxiDif


# 1
T = [0, 2, 1.1, 2]
print(chaoticIndex(T))
