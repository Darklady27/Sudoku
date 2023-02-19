sudoku = int(input("Enter numbers from 2 to N:")) #czy da sie inaczej, zeby 0 i nieparyste zawsze bylo error??
print("Rozmiar planszy:", str(sudoku), "x", str(sudoku))
N = sudoku

import math
import random

import numpy as np
import pandas as pd

n = int(math.sqrt(N))

def createMatrix(N):
    firstRow = random.sample(range(1,N+1),(N))
    permutes = random.sample(range(1,N+1),N)
    return list(firstRow[i:]+firstRow[:i] for i in permutes)

m = createMatrix(N)
print(m)
lista_1 = m[0]
print(lista_1)

A = np.array(lista_1)
B = np.reshape(A,(-1,2))

print(B)

data = pd.DataFrame(np.row_stack(B))

data.columns =["c"+str(i) for i in range(1,n+1)]
data.index = ["r"+str(i) for i in range(1,n+1)]

print(data)