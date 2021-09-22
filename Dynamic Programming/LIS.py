#Znajdź LIS (longest increasing subsequence), czyli najdłuższy podciąg rosnący.
#Złożoność O(n^2)

#Tworzę liste dp rozmiaru listy wejściowej.
#dp[i] - rozmiar lis, kończącego się w i-tym indeksie

def lis(T):
    n = len(T)
    dp = [1] * n 
    p = [-1] * n  
    
    #wypełniam liste dp
    for i in range(1,n):
        for j in range(i):
            if T[j] < T[i] and dp[j] + 1 > dp[i]: 
                dp[i] = dp[j] + 1 
                p[i] = j
    
    #szukam indeksu, w którym konczy sie najdluszy ciąg
    maxi = 0
    for i in range(1,len(cnt)): 
        if cnt[i] > cnt[maxi]:
            maxi = i
    
    #odwtarzam lis
    def printSolution(i): 
    if p[i] != -1:
        printSolution(p[i])
    print(A[i],end=" ")

    printSolution(maxi)
