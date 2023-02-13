sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku
list = []
for i in range(1,N+1):
    list.append(i)
    
import random
    
print(list)
dictionaries = {}
for i in range (1,N+1):
    dictionaries["row"+str(i)] = random.sample(list, len(list))

print(dictionaries) 
for v in dictionaries.values():
    print(' '.join([ str(s) for s in v]))

wartosci = dictionaries.values()
wiersze = list(wartosci)

lista_kolumn =[]
nowe_wiersze =[]

def sprawdz_kolumny(N,kolumna):
    while len(set(kolumna)) != len(list):
        for nr_wiersza, wartosc_w_kolumnie in enumerate(kolumna):
            for k in range(nr_wiersza + 1, N):  
                if  kolumna[k] == wartosc_w_kolumnie:
                    tmp = kolumna[k]
                    while tmp in kolumna:
                        tmp = random.choice(list)

                    kolumna[k] = tmp
    print(kolumna)
    lista_kolumn.append(kolumna)
    return "super kolumna"

def sprawdz_wiersze(N, lista_do_wierszy):
    while len(set(lista_do_wierszy)) != len(list):
        for numer, wartosc_w_wierszu in enumerate(lista_do_wierszy):
            for j in range(numer + 1, N):  
                if  lista_do_wierszy[j] == wartosc_w_wierszu:
                    stg = lista_do_wierszy[j]
                    while stg in lista_do_wierszy:
                        stg = random.choice(list)

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
        while len(set(kolumna)) != len(list) or  len(set(lista_do_wierszy)) != len(list): 
            print(len(set(kolumna)), len(set(lista_do_wierszy)), len(set(kolumna)) and len(set(lista_do_wierszy)))
            print(sprawdz_kolumny(N,kolumna))
            print(sprawdz_wiersze(N, lista_do_wierszy))
        nowe_wiersze.append(lista_do_wierszy)
        lista_kolumn.append(kolumna)


print(sprawdz_plansze(N, wiersze))
print(lista_kolumn)
print(nowe_wiersze)
