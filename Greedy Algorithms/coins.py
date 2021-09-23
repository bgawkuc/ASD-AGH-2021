#mam tablice z monetami
#oblicz min ilosc monet potrzebna by wydac dana kwote

#sortuje monety rosnaca
#przechodze on najw monety
#gdy jej wartosc jest <= brakujacej sumy to dodaje taka monete
#i robie to do momentu gdy kwota nie bedzie mniejsza od wart monety
#wtedy ide w dol

#to dziala gdyz moje monety sa wielokrotnosciami jakies liczby
#dziala bo kazda moneta jest przynajmniej dwukrotnie wieksza

def minCoins(A,x):
    n = len(A)
    A.sort() # sortuje tablice A rosnaca
    cnt = 0 #licznik ilosci monet
    res = [0] * n #mowi ile jakich monet
    idx = n - 1 #zaczynam od idx najwiekszej monety

    while x > 0 and idx >= 0:
        while x >= A[idx]:  #x/A[idx] >= 1
            cnt += 1
            res[idx] += 1
            x -= A[idx]
        idx -= 1
    print(res)
    return cnt

t = [1,5,10,25,100]
print(minCoins(t,176))