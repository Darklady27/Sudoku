def create_space_across():
    N = sudoku
    print(N*" -")

def create_space_down():
    N = sudoku
    print(N*"-\n")


for i in range(k):
    r = random.choice(list_sudoku)
    if r not in first_sguare:
        first_sguare.append(r)

print(first_sguare)




    