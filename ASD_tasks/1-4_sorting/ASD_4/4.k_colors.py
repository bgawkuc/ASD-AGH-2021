# Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
# A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
# szukamy najkrótszego przedziału z wszystkimi kolorami).

def insertion_sort(A):
    for i in range(1, len(A)):
        new = A[i]
        j = i - 1
        while j >= 0 and A[j] > new:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = new
    return A


def binarySeach(T, l, r, el):
    if l <= r:
        mid = (l + r) // 2
        if T[mid] == el:
            return mid
        elif el < T[mid]:
            return binarySeach(T, l, mid - 1, el)
        else:
            return binarySeach(T, mid + 1, r, el)
    return False


def uniqTab(T, k):
    uniq = []
    for i in range(len(T)):
        if len(uniq) == k:
            break
        if binarySeach(T, 0, len(uniq) - 1, T[i]) is False:
            uniq.append(T[i])
    return uniq


def kColors(T, k):
    n = len(T)
    uniq = insertion_sort(uniqTab(T, k))  #tablica z k kolorami
    cntUniq = [0] * k  #ilosc wystapien danego koloru
    length, minLenght = 0, 1000
    cnt = 0  #ilosc kolorow ktore juz wystapily
    i, j = 0, 0  # i-lewy indeks,j-prawy indeks

    for j in range(n):

        indJ = binarySeach(uniq, 0, len(uniq) - 1, T[j])

        if cntUniq[indJ] == 0:
            cnt += 1

        cntUniq[indJ] += 1

        # gdy wystapily wszystkie kolory
        if cnt == k:

            indI = binarySeach(uniq, 0, len(uniq) - 1, T[i])
            length = j - i + 1

            while cntUniq[indI] > 1:
                cntUniq[indI] -= 1
                length -= 1
                i += 1
                indI = binarySeach(uniq, 0, len(uniq) - 1, T[i])

            if length < minLenght:
                minLenght = length

            indI = binarySeach(uniq, 0, len(uniq) - 1, T[i])
            while cnt == k:

                cntUniq[indI] -= 1

                if cntUniq[indI] == 0:
                    cnt -= 1

                i += 1
                indI = binarySeach(uniq, 0, len(uniq) - 1, T[i])

    return minLenght

A = [1, 100, 1, 1, 5, 100, 5, 1, 5, 5, 100]
print(kColors(A, 3))