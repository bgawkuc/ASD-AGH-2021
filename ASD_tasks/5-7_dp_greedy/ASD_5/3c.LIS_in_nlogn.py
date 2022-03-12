#  Proszę podać algorytm na najdłuższy podciąg rosnący o złożoności O(nlog n) 

def binSearch(A,l,r,val):
    while (r - l) > 1:
        mid = l + (r - l) // 2

        if A[mid] >= val:
            r = mid
        else:
            l = mid
    return r 

def LIS(A):
    n = len(A)
    tail = [None] * (n + 1)
    tail[0] = A[0] 
    length = 1 
    
    for i in range(1,n):
        if A[i] < tail[0]:
            tail[0] = A[i]
        elif A[i] > tail[length-1]:
            tail[length] = A[i]
            length += 1
        else:
            tail[binSearch(tail, -1, length-1, A[i])] = A[i]

    return length