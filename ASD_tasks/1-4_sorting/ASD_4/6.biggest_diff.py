# Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
# znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
# że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
# których A[i + 1] − A[i] jest największe).

def maxRange(A):
    n = len(A)
    mini, maxi = A[0], A[0]

    for i in range(n):
        mini = min(A[i],mini)
        maxi = max(A[i],maxi)

    bucket = [[] for _ in range(n)]
    rang = (maxi - mini) / n

    for i in range(n):
        diff = ((A[i] - mini) / rang) - int((A[i] - mini) / rang)

        if diff == 0 and A[i] != mini:
            idx = (int((A[i] - mini) / rang)) - 1
        else:
            idx = int((A[i] - mini) / rang)

        bucket[idx].append(A[i])

    result = 0
    prev_max = max(bucket[0])

    for i in range(1,n):
        if len(bucket[i]) != 0:
            act_min = min(bucket[i])
            result = max(result,act_min - prev_max)
            prev_max = max(bucket[i])

    return result