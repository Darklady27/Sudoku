import pandas as pd
N =4
import random 
lista = [1,2,3,4]
kolumny =[]


for i in range (N):
    kolumny.append(random.sample(set(lista), len(lista)))

data = pd.DataFrame(kolumny)
print(data)
