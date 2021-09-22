#mamy dany ciag napisow(słow) S = [s1,s2,..,sn]
#oraz napis t
##wiadomo ze t mozna zapisac jako pewna ilosc napisów z S(z powtorzeniami)
##wybor napisow z S nazywamy reprezentaca
#a szerokosc reprezentacji to dlg najkrotszego napisu w niej zawartego
#zaimplementuj algorytm ktory majac S oraz t znajdzie maksymalna szerokosc reprezentacji
#tzn najktotszy jej napis jest mozliwie jak najdluzszy

#f(i) -> maksymalna szerokosc reprezentacji konczaca sie na ind i -1
#f(i) = max(d,f(i)); s nalezy do S, t[i - len(s): i + 1] == s
#dlg reprezentacji: d = min(f[i-len(s)],len(s))
#f(0) = 0
#f(i) od 0 do i włącznie

#czyli dla f(i) sprawdzamy wycinki ze slowa wejsciowego t
#roznej dlg ale gdzie t[... : i] on konczy sie na idx i - 1
#i gdy nie istnieje jakis konczacy sie na tym to zostaje -inf
#a jak nie to szukam max z reprezentacji tego odc i tych co wczesniej tworzyly ten wyraz

#t-napis dlugosci n
#S-tablica napisow mniejszych
#tworze tablice dp rozmiaru n + 1 wypłenioną -inf

#mam 2 pęlte
#i -> wybieram dlg obecnie porownywanego fragmentu t od 0 do n
#s -> wybieram string z S
#probuje wyciac substring z s, zacyznajcy sie w i-len(s) a konczacy w i-1
#dla i-len(s) >= 0 uda sie wyciąć taki niepusty string
#jego dlg == len(s)
#gdy i == len(s) oraz s == substring
#wycinki sie zgadzaja wiec dp[i] to max(dp[i], len(s))
#dla i > len(s) oraz s == substring
#wynicek sie zgadza z fragmentem t czyli
#dp[i] = max(dp[i], min(dp[i-len(s)],len(s)))
#poniewaz szukam minimum z wszystkich reprezentacji
#wiec biore min z dlg mojego stringa s oraz dp[i-len(s)] czyli dlg reprezentacji reszty napisu


def string(S,t):
    f = [-float('inf')] * (len(t) + 1)

    for i in range(len(t)+1):
        for s in S:

            substring = t[i - len(s):i] #wycinek tej samej dlg co substring konczacy sie na ind i - 1
            print(substring)

            #gdy dlugosc danego ciagu znakow jest wieksza od dlg obecnie wybranego substringa
            #tzn ze przed nim jest jeszcze jakis ciag znakow
            #i sprawdzam dlg max reprezentacji dla tego mniejszego ciagu
            #i z tej starej dlg oraz dlg obecnego substringa biore min
            #a potem biore max z tego wybranego min oraz obecnej wartosci f[i]
            if i > len(s):
                if s == substring:
                    f[i] = max(f[i],min(f[i-len(s)],len(s)))

            #gdy dlugosc danego ciągu znakow jest rowna doklanie dlugosci wybranego substringa
            elif i == len(s):
                if s == substring: #gdy sa one rowne
                    f[i] = max(f[i],len(s))  #to max dlg min repr to max z tej dlg napisu i pola wczesniej przypisanego

    return f[-1],f

#INNA IMPLEMENTACJA
def stringMade(S,t):
    n = len(t)
    #dp[i] max dlg reprezentacji (dlg najkrotszegi napisu) koczczacej sie na i-tym idx
    dp = [-float('inf')] * (n)

    for i in range(n): #idx w slowie t
        for s in S: #string z tablicy s
            #wycinek zawsze zaczyna sie na idx 0 i konczy na idx i
            #czyli jego dlg wynosi i+1
            #jesli wycinek slowa t jest >= dlugosci s
            if i + 1 >= len(s):
                #mam fargment napisu t od 0 do idx i
                #wycinam z niego napis dlugosci s
                substring = t[i-(len(s)-1):i+1]

                #gdy wycinek z t i napis s są równej dlg
                if i+1 == len(s):
                    #gdy wycinek z t i string s są równe
                    if s == substring:
                        dp[i] = max(dp[i],len(s))
                #gdy wycinek t jest dluzszy od napisu dlg s
                if i+1 > len(s):
                    if s == substring:
                        dp[i] = max(dp[i],min(len(s),dp[i-len(s)]))

    return dp[-1],dp

S = ['ab','aba','a','bab','bbab']
t = 'abbab'
print(string(S,t))