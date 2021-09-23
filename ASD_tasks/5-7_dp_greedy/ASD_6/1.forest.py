# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

#dp[i] - maksymalny zysk gdy do wyboru mam drzewa od indeksu 0 do i

def forest(A):
    n = len(A)
    dp =[0] * n

    dp[0] = A[0]
    dp[1] = max(A[0],A[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+A[i])
    
    #cut[i] - określa czy drzewo o indeksie i należy ścinać
    cut = [False] * n
    if dp[n-1] == dp[n-3] + A[n-1]:
        cut[n-1] = True

    for i in range(n-2,1,-1):
        if dp[i] == dp[i-2] + A[i] and cut[i+1] == False:
            cut[i] = True

    if cut[2]:
        cut[0] = True
    else:
        if A[1] > A[0]: cut[1] = True
        else: cut[0] = True

    for i in range(n):
        if cut[i]:
            print(i,end=" ")
    return
