#Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
#liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].

def func(A):
    cnt = 0

    def cntInversion(A):
        if len(A) > 1:
            nonlocal cnt
            mid = len(A) // 2

            L = A[:mid]
            R = A[mid:]

            cntInversion(L)
            cntInversion(R)

            l = r = a = 0

            while l < len(L) and r < len(R):
                if L[l] > R[r]:
                    cnt += len(L) - l
                    A[a] = R[r]
                    r += 1
                else:
                    A[a] = L[l]
                    l += 1
                a += 1

            while l < len(L):
                A[a] = L[l]
                l += 1
                a += 1

            while r < len(R):
                cnt += len(L) - l
                A[a] = R[r]
                r += 1
                a += 1

    cntInversion(A)
    return cnt
