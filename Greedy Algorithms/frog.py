# Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku większych 
# liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a jej energia nigdy nie może
# spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na niektórych liczbach—także na
# zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki dodaje się do aktualnej energii Zbigniewa). 
# Proszę zaproponować algorytm, który oblicza minimalną liczbę skoków potrzebną na dotarcie z 0 do n − 1 majać daną 
# tablicę A z wartościami energetycznymi przekąsek na każdej z liczb.

from queue import PriorityQueue


def zbigniew(A):
    n = len(A)
    # far - zasięg skoku żaby
    far = A[0]
    # ilosc skoków
    cnt = 1

    if far >= n - 1:
        return cnt

    q = PriorityQueue()
    idx = 1
    while idx < n and idx <= far:
        q.put((-A[idx], idx))
        idx += 1

    while far < n - 1:
        energy, i = q.get()
        far += abs(energy)

        cnt += 1

        while idx < n and idx <= far:
            q.put((-A[idx], idx))
            idx += 1

    return cnt