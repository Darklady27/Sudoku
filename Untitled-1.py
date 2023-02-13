
sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import math
import random

k = math.sqrt(N)

list = []
for i in range(1,N+1):
    list.append(i)
    
print(list)

dictionaries = {}
for i in range (1,N+1):
    dictionaries["row"+str(i)] = random.sample(list, len(list))

print(dictionaries) 
for v in dictionaries.values():
    print(' '.join([ str(s) for s in v]))

wiersze= dictionaries.values()
print(wiersze)

def sprawdz_plansze(N, wiersze):
    for i in range(N):
        print(f"Oto wartosci z kolumny {i}:")
        kolumna =[]
        for wiersz in wiersze:
            print(wiersz[i])
            kolumna.append(wiersz[i])
        while len(set(kolumna)) == len(kolumna):
            for nr_wiersza, wartosc_w_kolumnie in enumerate(kolumna):
                for k in range(nr_wiersza + 1, N):  
                    if  kolumna[k] == wartosc_w_kolumnie:
                        while kolumna[k] == wartosc_w_kolumnie or kolumna[k] not in kolumna:
                            kolumna[k] = random.choice(list)
        print(kolumna)

    return "jest super"
     

print(sprawdz_plansze(N, wiersze))

                    

#sprawdzenie
#dziury
#wpisywanie do dziurek 