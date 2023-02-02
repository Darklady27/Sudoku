sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import random

list = [i for i in range(1, N+1)]
print(list)

dictionaries = {}
for i in range (1,N+1):
    dictionaries["column"+str(i)] = random.sample(list, len(list))
print(dictionaries)

import math

small_squares = math.sqrt(N)

