# Mamy dany ciąg napisów S = (s1, ..., sn) oraz pewien napis t. Wiadomo, że t można zapisać jako
# złączenie pewnej ilości napisów z S (z powtórzeniami). Na przykład dla S = (s1, s2, s3, s4, s5)
# gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, napis t = ababbab można zapisać, między
# innymi, jako s2s4 lub jako s1s1s3s5. Pierwsza reprezentacja ma ”szerokość” 3 (przez szerokość
# rozumiemy długość najkrótszego si użytego w reprezentacji) a druga 1. Proszę opisać algorytm,
# który mając na wejściu S oraz t znajdzie maksymalną szerokość reprezentacji t.


from math import inf

def string(S, t):
    f = [-inf] * (len(t) + 1)

    for i in range(len(t) + 1): #na jakim idx i koncze wycinek t
        for s in S: #wybrany substring z tablicy s

            segment = t[i - len(s): i] #tworze wycinek z t konczacy sie na idx i - 1 takiej dlg jak s

            if i == len(s):
                if s == segment:
                    f[i] = max(f[i], len(s))

            elif i > len(s):
                if s == segment:
                    smaller = min(f[i-len(s)], len(s))
                    f[i] = max(f[i], smaller)

    return f[len(t)]

#wynik 3
S = ['ab', 'abab', 'ba', 'bab', 'b']
t = 'ababbab'
#t = (abab + bab) lub (ab + abab + b)
#max(3,1) = 3

#wynik 2
S1 = ['ab','aba','a','bab','bbab']
t1 = 'abbab'
#t1 = (a + bbab) lub (ab + bab)
#max(1,2) = 2

print(string(S1,t1))
