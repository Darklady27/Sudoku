sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import random

import math

k = math.sqrt(N)

list = []
for i in range(1,N+1):
    list.append(i)
    if len(list) % k ==0:
        print('\n')
print(list)

dictionaries = {}
for i in range (1,N+1):
    dictionaries["column"+str(i)] = random.sample(list, len(list))

print(dictionaries)

