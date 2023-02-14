sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku
moja_lista = []
for i in range(1,N+1):
    moja_lista.append(i)
    
import random

print(moja_lista)
dictionaries = {}
for i in range (1,N+1):
    dictionaries["row"+str(i)] = random.sample(moja_lista, len(moja_lista))

print(dictionaries) 
for v in dictionaries.values():
    print(' '.join([ str(s) for s in v]))

wartosci = dictionaries.values()
wiersze = list(wartosci)

lista_kolumn =[]
nowe_wiersze =[]

def sprawdz_kolumny(N,kolumna):
    while len(set(kolumna)) != len(moja_lista):
        for nr_wiersza, wartosc_w_kolumnie in enumerate(kolumna):
            for k in range(nr_wiersza + 1, N):  
                if  kolumna[k] == wartosc_w_kolumnie:
                    tmp = kolumna[k]
                    while tmp in kolumna:
                        tmp = random.choice(moja_lista)

                    kolumna[k] = tmp
    print(kolumna)
    lista_kolumn.append(kolumna)
    return "super kolumna"

def sprawdz_wiersze(N, lista_do_wierszy):
    # wszystkich wierszy na raz zmieniajac na set nie sprawdzimy, bo jest to kolekcja list, musimy
    # to robic pewnie pojedynczo, albo zrobic sobie funkcje pomocnicza w ktrej bedziemy sprawdzac pojedynczo
    # anyway set(tuple(lista)) dziala jesli tylko w liscie nie ma kolejnych niehashowalnych obiektow,
    # czyli set(tuple([1, 2, 3]))  jest ok, set(tuple([[1] [2], [3]])) nie bedzie ok
    while len(set(lista_do_wierszy)) != len(moja_lista):
        for numer, wartosc_w_wierszu in enumerate(lista_do_wierszy):
            for j in range(numer + 1, N):  
                if  lista_do_wierszy[j] == wartosc_w_wierszu:
                    stg = lista_do_wierszy[j]
                    while stg in lista_do_wierszy:
                        stg = random.choice(moja_lista)

                    lista_do_wierszy[j] = stg
    print(nowe_wiersze)
    
    return "super wiersze"

def sprawdz_plansze(N, wiersze):
    for i in range(N):
        print(f"Oto wartosci z kolumny {i}:")
        kolumna = []
        lista_do_wierszy =[]
        for wiersz in wiersze:
            print(wiersz[i])
            kolumna.append(wiersz[i])
        new_wiersz = wiersze[i]
        lista_do_wierszy.append(new_wiersz)
        print(lista_do_wierszy)
        print("While")
        ity_wiersz = lista_do_wierszy[i]
        while len(set(tuple(kolumna))) != len(moja_lista) or  len(set(tuple(ity_wiersz))) != len(moja_lista): 
            print(kolumna, lista_do_wierszy, kolumna)
            print(sprawdz_kolumny(N,kolumna))
            print(sprawdz_wiersze(N, lista_do_wierszy))
        nowe_wiersze.append(lista_do_wierszy)
        lista_kolumn.append(kolumna)


print(sprawdz_plansze(N, wiersze))
print(lista_kolumn)
print(nowe_wiersze)
