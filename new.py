N =4
import random 
lista = [1,2,3,4]
kolumny =[]
wiersze_od_kolumn =[]

for i in range (N):
    kolumny.append(random.sample(set(lista), len(lista)))

for i in range(N):
    s = []
    for listy in kolumny:
        s_w = s.append(listy[i])
    wiersze_od_kolumn.append(s)


print(kolumny)

print(wiersze_od_kolumn)

while len(set(wiersze_od_kolumn)) != len(lista):
    for nr_wiersza, wartosc_w_wierszu in enumerate(wiersze_od_kolumn):
        print(nr_wiersza)
        print(wartosc_w_wierszu)
        for k in range(nr_wiersza+1,N):
            if wiersze_od_kolumn == wartosc_w_wierszu:
                tmp = wiersze_od_kolumn[k]
                while tmp in wiersze_od_kolumn:
                    tmp = random.choice(set(lista))
                    wiersze_od_kolumn[k] = tmp
        print(wiersze_od_kolumn)


# for i in range (N):
#     print(f"Oto wartosci z kolumn {i}:{kolumny[i]}")
#     print(kolumny)


