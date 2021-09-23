#mamy ciag przedzialow
#przedzialy da sie skleic gdy sie dotykaja ale nie zachodza na siebie
#mamy podaną liczbe k
#prosze podac algorytm ktory oblicza dlg najdluzszego przedzialu
#jaki mozna osiagnac przez sklejenie k przedziałów

#trzeba ponumerowac,przemapowac 1 do 2n, (dla n przedziałow)
#np dla [2,6],[3,8],[4,5]
#mapuje to na [1,5],[2,6],[3,4]
#f(i,j) minimalna liczba przedzialow ktore tzreba skleic by powstal przedzial
#od pkt i do pkt j -> i,j wybieram z przedzialu 1,..,2n
#f(i,j) = min {f(i,k)+f(k,j)+1}; minimum po k


