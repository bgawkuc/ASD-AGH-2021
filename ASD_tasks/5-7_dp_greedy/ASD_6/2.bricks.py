#mamy liste klockow kazdy o wysokosci jednostkowej
#mamy podane wspolrzedna x-start oraz x-koniec kazdego klocka
#mamy liste krotek z takimi wartosciami
#napisz algorytm ktory oblicza ktore klocki nalezy usunac
#aby liczba usuneietych klockow byla mozliwie jak najmniejsza
#a kolejne klocki zawieraly sie w sobie nawzajem
#czyli dla klocka x1, x2 to kolejne klocek z1,z2 musi:
#miec wspolrzedne: z1 >= x1 i z2 <= x2,
#tworzą nierozszerzającą się wieżę
#kazdy kolejny ma sie zawierac w poprzednim

#dp[i] - max wysokosc wiezy jaką sie da uzysakc gdzie ostatnim klockiem jest i-ty klocek
#wszystkie wartosci w dp ustawiam na 1
#mam 2 pętlw
#przechodze po i od 1 do n
#przechodze po j od 0 do i-1
#sprawdzam czy i-ty klocek zawiera sie w j-tym
#oraz czy wybranie j-tego klocka pozowli mi zwiekszyc wysokosc wiezy
#czyli czy dp[j] + 1 > dp[i]
#wynik czyli minimalna ilosc klockow do usuniecia to
#dlg tablicy z klockami - max wys wiezy


def bricks(A):
    n = len(A)
    #jaka max wieze da sie uzyskac biorac i-ty klocek
    dp = [1] * n #wys kazdej wiezy na starcie to 1

    for i in range(1,n): #wybieram klocek i
        for j in range(i):
            #sprawdzam czy i-ty klocek zawiera sie w j-tym
            #oraz czy biorac j-ty klocek wydluze wysokosc i-tej wiezy
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    #wynik to ilosc do usuniecia =  ilosc klockow - max wys wiezy
    return n - max(dp)

#spadnie [1,5] -> [3,4] -> [3,3] tworzą wieze, reszte klockow trzeba usunac
A = [[1,5],[2,7],[3,4],[1,10],[3,3]]
print(bricks(A))


