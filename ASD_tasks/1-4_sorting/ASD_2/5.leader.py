#(Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
#O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A
#na ponad połowie pozycji

# szuka potencjalnego indeksu lidera
def leader(A):
    cnt = 0  # ilosc wystapien
    idx = 0  # indeks lidera

    for i in range(len(A)):
        if cnt == 0:
            idx = i
            cnt += 1
        elif A[i] == A[idx]:
            cnt += 1
        else:
            cnt -= 1

    return idx


def more_than_half(A):
    idx = leader(A)
    cnt = 0
    for i in range(len(A)):
        if A[i] == A[idx]:
            cnt += 1
    return cnt > len(A) // 2
