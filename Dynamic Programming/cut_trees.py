#mam tablice n drzew stojacych w jednej linii
#wyciecie kazdego dzrewa ma okreslony zysk
#okresl ktore drzewa nalezy wyciac by zysk był jak najwiekszy
#nie mozna wyciac 2 dzrew pod rząd
#dp(i) max zysk gdy wycinamy do i-tego drzewa

#dp[i] = max(dp[i-1],dp[i-2]+A[i]);
#A-tablica z zarobkami za sciecie i-tego drzewa
#za pomocą tej funkcji oblicza zysk oraz dalej wupisuje idx drzew które nalezy wyciac

def forest(A):
    n = len(A)
    dp =[0] * n

    dp[0] = A[0]
    dp[1] = max(A[0],A[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+A[i])

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
    print()

    return 'profit:',dp[n-1]



A = [5, 10, 20, 1, 40, 3, 80, 20, 1, 2, 50, 100, 4]
print(forest(A))
