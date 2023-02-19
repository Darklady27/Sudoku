


sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import math
import random

import numpy as np
import pandas as pd

n = math.sqrt(N)


def print_sudoku(data: np.ndarray):
    for row in data:
        for cell in row:
            print(cell, end=' ')
        print()

def sprawdz_sudoku(data: np.ndarray):
    """
        1. Przejdzmy sie po wszystkich kolumnach i je sprawdzmy
        2. Przejdzmy sie po wszystkich wierszach i je sprawdzmy
        3. Przejdzmy sie po wszyskich kwadratach i je sprawdzmy

        jesli ktorykolwiek nie jest ok zwracamy ze sudoku nie jest ok
        Jezeli wszystkie sprawdzenia przeszly nasze sudoku jest poprawne
    """

    for nr_wiersza in range(N):
        if not sprawdz_wiersz(data,nr_wiersza):
            return (False, nr_wiersza, None)
    for nr_kolumny in range(N):
        if not sprawdz_kolumne(data, nr_kolumny):
            return (False, None, nr_kolumny)

    n = int(math.sqrt(data.shape[0]))

    for nr_wiersza in range(0,N,n):
        for nr_kolumny in range(0,N,n):
            
            if not sprawdz_kwadracik(data,nr_kolumny, nr_wiersza):


                return (False, nr_wiersza, nr_kolumny)

    return (True, None, None)

    


def sprawdz_kolumne(data: np.ndarray, nr_kolumny):
    """
        Przyjmuje reprezentacje sudoku i sprawdza czy konkretna wskazana kolumna jest poprawna
    """
    badana_kolumna = data[:,nr_kolumny]
    if len(set(badana_kolumna)) == N:
        return True
    else: 
        return False

def sprawdz_kwadracik(data: np.ndarray, nr_kolumny, nr_wiersza):
    """
    Zalozenie: nr_kolumny i nr_wiersza odpowiadaja zawsze pierwszemu wierszowi i kolumnie od ktorej zaczyna sie kwadracik.
    """
    # if nr_kolumny == 1 or nr_wiersza == 1:
    #     raise Exception("zle wywolanie")
    n = int(math.sqrt(data.shape[0]))
    kwadracik = data[nr_wiersza:nr_wiersza+n,nr_kolumny:nr_kolumny+n]
 
    kwadracik = kwadracik.reshape((-1,)) #zeby byl 1 wymiar
    
    if len(set(kwadracik)) == N:
        return True
    else:
        return False

def sprawdz_wiersz(data: np.ndarray, nr_wiersza: int):
    """
        Przyjmuje reprezentacje sudoku i sprawdza czy konkretnie wskazany wiersz jest poprawny
    """
    badany_wiersz = data[nr_wiersza,:]
    if len(set(badany_wiersz)) == N:
        return True
    else: 
        return False


class MyException(Exception):
    ...

def plansza():
    n = int(math.sqrt(N))
    licz_od_nowa = True
    while licz_od_nowa:
        try:
            data = np.zeros((N, N), dtype=int)
            zbior = {i for i in range(1, N+1)}
            data[0,0] = random.choice(list(zbior))
            for i in range(N):
                for j in range(N):
                    kolumna = set(data[:, j]) #ze wszystkich wierszy kolumny j
                    wiersz = set(data[i,:])
                    a = i % n
                    b =j % n
                    kwadracik = set(data[i-a:(i-a)+n,j-b:(j-b)+n].reshape((-1,)))
                    dozwolone = zbior - kolumna - wiersz - kwadracik
                    if len(dozwolone) == 0:
                        raise MyException("empty set")                    
                    wybrana_wartosc = random.choice(list(dozwolone))
                    data[i,j] = wybrana_wartosc
            licz_od_nowa = False
        except MyException as e:
            print(i, j)

    return data


def create_sudoku():
    
    data = plansza()
    czy_ok, bledny_wiersz, bledna_kolmna = sprawdz_sudoku(data)

    while not czy_ok:
        zamien_odpowiednia_czesc(data, bledny_wiersz, bledna_kolmna)
        czy_ok, bledny_wiersz, bledna_kolmna = sprawdz_sudoku(data)

    print(data)  
    return print("Sudoku ok")

def zamien_odpowiednia_czesc(data, bledny_wiersz, bledna_kolmna):
    lista = [i for i in range(1, N+1)]
    n = int(math.sqrt(N))
    if bledny_wiersz is not None and bledna_kolmna is not None:
        nowe_liczby = random.sample(lista,len(lista))

        data[bledny_wiersz:bledny_wiersz+n,bledna_kolmna:bledna_kolmna+n] = np.array(nowe_liczby).reshape((n,n))
    elif bledny_wiersz is not None:
        data[bledny_wiersz, :] = random.sample(lista,len(lista))
    elif bledna_kolmna is not None:
        data[:,bledna_kolmna] = random.sample(lista,len(lista))


d= plansza()
print_sudoku(d)

create_sudoku()



# print_sudoku(data)
# a = np.array([[0, 1, 2, 3],
#               [2, 3, 0, 1],
#               [3, 2, 1, 0],
#               [1, 0, 3, 2]])
# # print_sudoku(a)
# print(sprawdz_sudoku(data))
# print_sudoku(data)



