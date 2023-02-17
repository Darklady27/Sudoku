N = 4


import random

def createMatrix(N):
    firstRow = random.sample(range(1,N+1),(N))
    permutes = random.sample(range(N),N)
    return list(firstRow[i:]+firstRow[:i] for i in permutes)


m = createMatrix(N)
for i in m:
    print(i)