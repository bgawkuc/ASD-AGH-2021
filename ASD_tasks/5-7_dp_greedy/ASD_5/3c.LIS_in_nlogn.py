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
    
    #przechodze liniowo po A
    for i in range(1,n): 
        
        #gdy znaleziony element jest mniejszy od najmniejszego to najmniejszy nim zastępuje
        if A[i] < tail[0]: 
            tail[0] = A[i]
        
        #gdy jest wiekszy od największego do daje go za największy i zwiekszam dlugość
        elif A[i] > tail[length-1]: 
            tail[length] = A[i]
            length += 1
        
        #gdy jest pomiedzy to znajduje miejsce za pomocą binary search, w którym trzeba go wpisać
        else:
            tail[binSearch(tail, -1, length-1, A[i])] = A[i]


    return length 
