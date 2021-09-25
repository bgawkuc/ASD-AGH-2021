#mam podany zbior kosztow - A
#A[0] - cena wybudowana key 0
#A[1] - cena wybudowana key 1 itd
#chce z nich zbudowac drzewo BST
#tak aby sumaryczny koszt budowy był mozliwie jak najmniejszy
#koszt budowy danego węzła to iloczyn:
#poziom na jakim znajduje sie klucz * wartosc klucza
#poziom roota -> 1

#rozwazam kazdy z kluczy jak początek i rekurencyjnie tworz drzewa
#z wszystkich takicg drzew szukaj tego o min koszcie

#czyli majac tablice [25,10,20] to klucze wierzchołkow to bedzie 0,1,2
#mozeliwe drzewa jakie sie da zbudować:
#  1
# / \
#0   2      koszt:1*10+25*2+20*2=100

#    2
#   /
#  1
# /
#0          koszt:1*20+2*10+3*25=105

# 0
#  \
#   1
#    \
#     2     koszt:1*25+2*10+3*20=105

# 0
#  \
#   2
#  /
# 1         koszt:1*25+2*20+3*10=95


def findConstructCost(A,i,j,level=1,cost=float("inf")):
    #gdy przejde całą tablice
    if i > j:
        return 0

    for k in range(i,j+1): #k- klucz ktory dodaje do drzewa
        # koszt lewy to wszystkie indeksy na lewo ,bo tam klucze sa mniejsze
        leftCost = findConstructCost(A,i,k-1,level+1)
        #koszt prawy to wszystkie indeksy na prawo ,bo tam klucze są wieksze
        rightCost = findConstructCost(A,k+1,j,level+1)

        cost = min(cost, A[k] * level + leftCost + rightCost)

    return cost

#trzoszke inna implementacja
def constructCost2(A):
    n = len(A)

    def func(l,r,level = 1,cost=float('inf')):
        if l > r:
            return 0
        for k in range(l,r+1):
            leftCost = func(l,k-1,level+1)
            rightCost = func(k+1,r,level+1)
            cost = min(cost,A[k]*level+leftCost+rightCost)
        return cost

    return func(0,n-1)

#klucz 0 -> 25; klucz 1 -> 10; klucz 2 -> 20
print(findConstructCost([25,10,20],0,2))

