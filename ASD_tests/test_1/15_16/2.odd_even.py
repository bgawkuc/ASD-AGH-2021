#  Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
# Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
# rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
# dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
# zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
# powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.


def oddEven(A):
    odd = []
    even = []
    n = len(A)

    for i in range(n):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])

    even.sort()
    new = []
    o,e = 0,0

    while o < len(odd) and e < len(even):
        if odd[o] < even[e]:
            new.append(odd[o])
            o += 1
        else:
            new.append(even[e])
            e += 1

    while o < len(odd):
        new.append(odd[o])
        o += 1
    while e < len(even):
        new.append(even[e])
        e += 1

    return new

A  = [1,3,5,5,8,0,7,9,11,4,17,21,2]
print(oddEven(A))