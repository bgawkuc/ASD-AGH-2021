#mamy las przedstawiony w tab 1d
#pod kazdym indeksem znajduje sie drzewo ktore ma wartosc
#nie mozna wyciąc 2 drzew pod rzad
#podaj algorytm ktory liczy max mozliwy do uzyskania zysk
#i dodatkowo wypisuje idx wybranych drzew

#g(i) max zysk do i-tego drzewa
#g(i) = max(g(i-2)+c(i), g(i-1))
#g(0) = 0

#gdy wynik odtwarzam na koniec
def forest1(A):
    n = len(A)
    dp = [0] * n
    taken = [False] * n

    dp[0] = A[0] #gdy biore tylko drzewo o idx 0 to jest moj max
    dp[1] = max(A[0],A[1]) #gdy patrze na drzewa do idx 1 włącznie

    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2]+A[i])


    for i in range(n-1,1,-1): #dp[i] wynosi tyle co dp[i-2] + profit[i] i przedzmiot za nim nie był brany
        if dp[i] == dp[i-2] + A[i] and (i == n - 1 or taken[i+1] == False): #czyli gdy brałam i-ty idx
            taken[i] = True

    if taken[2] == True: #jak brałam 2 idx
        taken[0] = True # to został mi tylko 0

    else: #jak nie brałam 2 idx to sprawdzam czy pod 0 czy pod 1 jest większa wartosc
        if A[0] > A[1]:
            taken[0] = True
        else:
            taken[1] = True

    for i in range(n):
        if taken[i]:
            print(i,end=" ")
    print()

    return dp[n-1]

#gdy wynik odtwarzam na biezaco
def forest2(A):
    n = len(A)
    dp = [0] * n
    taken = [[] for _ in range(n)] #indeksy drzew ktore zabrano by osiagnac dp[i]

    dp[0] = A[0]
    taken[0] = [0] #czyli by osiaganc dp[0[] biore dzrewo 0
    dp[1] = max(A[0],A[1])

    #by osiagnac dp[1] biore drzewo 0 lub 1
    if dp[1] == A[1]:
        taken[1] = [1]
    else:
        taken[1] = [0]

    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2] + A[i])

        if dp[i] == dp[i-1]:
            taken[i] = taken[i-1]
        else:
            taken[i] = taken[i-2]
            taken[i].append(i)

    return dp[n-1],taken[n-1]



#2 sposob-blad??
def f(i):
    global V,cnt
    cnt += 1
    print("f ",i)
    if i == 0:
        memoF[i] = V[0]
        return memoF[i]
    memoF[i] = g(i-1) + V[i]
    return memoF[i]


def g(i):
    global V,cnt
    cnt += 1
    print("g ",i)
    if i == 0:
        memoG[i] = 0
        return memoG[i]
    memoG[i] = max(f(i-1),g(i-1))
    return memoG[i]

V = [2,3,5,7,1,11,13,0,0,17]
v = [1,2,3,6,5]
cnt = 0
memoG = {}
memoF = {}
# print(g(len(v)))
print(forest2(v))
# print(cnt)