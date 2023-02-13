
sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import math
import random

list = []
for i in range(1,N+1):
    list.append(i)
    
print(list)

kolumny = {}
for i in range (1,N+1):
    kolumny.append = random.sample(list, len(list))

print(kolumny) 
