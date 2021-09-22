# Proszę zaimplementować funkcję partition z algorytmu QuickSort
# według pomysłu Hoare’a (tj. mamy dwa indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka
# i zamieniamy elementy tablicy pod nimi jeśli mniejszy indeks wskazuje na wartość większą od piwota, a
# większy na mniejszą).

def partition(A,l,r):
    piv = A[l]
    i = l - 1
    j = r + 1
    
    while True:
        i += 1
        while A[i] < piv:
            i += 1

        j -= 1
        while A[j] > piv: 
            j -= 1

        if i >= j: 
            return j

        A[i], A[j] = A[j], A[i]
