#mam ciąg sekwencji DNA
#kazda sie składa z liter: G, A, T, C
#opisz algorytm który stwierdza czy wszystkie sekwencje są parami różne

#tworze drzewo gdzie root ma 4 dzieci: G,A,T,C
#od kazdej z liter mogą wychodzic kolejne G,A,T,C  i tak dalej w dół
#do kazdego pola dodaje węzeł end = False
#tzn ze dokladnie w tym miejscu nie skonczyla sie zadna sekwencja
#"dodaje" sekwencje do dzrewa tzn np gdzie dodac GGAC
# -> od G tworze dziecko G, od nowego G tworze dziecko A, od A tworze dziecko C
#skoro na C konczy sie sekwencja GGAC to na koniec sciezki(dla tego C) daje wartosc True(w tym miejscu skonczyła sie sekwencja)
#gdyby wystąpiła jeszcze raz sekwencja taka sama to dotzre ona do konca(pola end= True dla tego C)
#i nie bedzie nigdy musiała utworzyc nowego węzła
#czyli wystapil duplikat
#warunek na duplikat: konczy sie na polu end = True i nie utworzyłam zadnego nowego węzła
#gdyby nie był to duplikat to choć raz tzreba by było dodac jakis wezeł albo skonczyc na polu end=False

#tu dodałam sekwencje GGAC oraz GGCT; ostatnue pola C, T mają wartosc end = True
#     root
# /  /   \  \
#G   A   T   C
#|
#G
#| \
#A  C
#|  |
#C  T
