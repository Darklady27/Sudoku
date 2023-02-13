N = 4
list = [1,2,3,4]
import random    

dictionaries = {}
for i in range (1,N+1):
    dictionaries["row"+str(i)] = random.sample(list, len(list))

print(dictionaries.values) 

wartosci = list(dictionaries.values())[0]
print(wartosci)



print(wartosci)

# dictionary1 = {
#     'name': "Bob",
#     'dict1': {'adm': 44},
# }
 
# print(dictionary1.values())
 
# # cast it into list then we can access values by indexing
# value = list(dictionary1.values())[0]
# print(value)