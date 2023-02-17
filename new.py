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

# for i in range (N):
#     print(f"Oto wartosci z kolumn {i}:{kolumny[i]}")
#     print(kolumny)


