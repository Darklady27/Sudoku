sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import math
import random

import numpy as np
import pandas as pd

n = math.sqrt(N)

def createMatrix(N):
    firstRow = random.sample(range(1,N+1),(N))
    permutes = random.sample(range(1,N+1),N)
    return list(firstRow[i:]+firstRow[:i] for i in permutes)

m = createMatrix(N)
c = []
for i in m:
    print(i)
    c.append(i)

print(c)
d =[]

for i in c:
    t =[]
    splits = np.array_split(i,n)
    print(splits)
    for array in splits:
        t.append(list(array))
    zbior_array = np.vstack(t)
    d.append(zbior_array)

print(d)

data = pd.DataFrame(np.row_stack(d))

print(data)

