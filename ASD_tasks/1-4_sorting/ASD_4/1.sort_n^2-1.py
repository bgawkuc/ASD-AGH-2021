# Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb
# ze zbioru 0, . . . , n2 − 1

#zlozonosc O(n)

#przedstawia liczbę w systemie n
def el_in_n_sys(el,n,x):
    d = (el // x) % n
    return d

def countsort(T,x):
    n = len(T)
    new = [0] * n
    cnt = [0] * n

    for i in range(n):
        d = el_in_n_sys(T[i], n, x)
        cnt[d] += 1

    for i in range(1,n):
        cnt[i] += cnt[i - 1]

    for i in range(n-1,-1,-1):
        d = el_in_n_sys(T[i],n,x)
        cnt[d] -= 1
        new[cnt[d]] = T[i]

    T[:] = new

def sort(T):
    n = len(T)
    countsort(T,1)
    countsort(T,n)
    return T