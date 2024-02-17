
import math
import random
import numpy as np

sudoku = int(input("Enter numbers from 2 to N:")) 
print("Board size:", str(sudoku), "x", str(sudoku))
N = sudoku

n = math.sqrt(N)

def print_sudoku(data: np.ndarray): 
    print('\t\t', end='')
    for i in range(N):
        print(f"n{i}", end ='\t')
    dashes = '-' * (8 * N + 11)
    print(f"\n{dashes}")
    for index,row in enumerate(data):
        print(f"Row nr {index}",end='    |')
        print('\t', end='')
        for cell in row:      
            if cell == 0:
                cell = " "
                print(cell, end='   |\t')
                
            else:
                print(cell, end='   |\t')
        print(f"\n{dashes}")

def sudoku_solving(data: np.ndarray):
    modifiable_data = data == 0
    ending = False
    while not ending:
        try:
            which_row = int(input("Enter row number:"))
            if which_row not in range(0,N):
                print(f"Enter only numbers from 0 to {N-1}")
                continue
            else:
                i = which_row
        except:
            print(f"(Enter only numbers from 0 to {N-1})")
            continue
        try:
            which_column = int(input("Enter column number:"))
            if which_column not in range(0,N):
                print(f"Enter only numbers from 0 to {N-1}")
                continue
            else:
                j = which_column
        except:
            print(f"(Enter only numbers from 0 to {N-1})")
            continue
        try:
            if modifiable_data[i, j]:
                user_value = int(input(f"Enter a value in the blank space of the board from 1 to {N}:"))
                if user_value in range(0,N+1):
                    data[i][j] = user_value
                    print_sudoku(data)
                else:
                    print(f"You can only enter numbers from {1} to {N}")
            else:
                print("You can only change empty fields")
            if not 0 in data:
                sudoku_completed =(input("Do you want to check sudoku (enter Yes or No):"))
                if sudoku_completed == "Yes":
                    ending == True
                else:
                    continue
        except:
            print(f"You can only enter number from {1} to {N}")

        if ending:
            sudoku_ok = check_sudoku(data)
            if sudoku_ok:
                print("Good job")
                ending = True
            else:
                print("Sudoku incorrect")

def check_sudoku(data: np.ndarray):
    """
       1. Let's go through all the columns and check them
         2. Let's go through all the lines and check them
         3. Let's go through all the squares and check them

       if any of them is not ok, we say that the sudoku is not ok. If all the checks have passed, our sudoku is correct
    """
    for nr_row in range(N):
        if not check_row(data,nr_row):
            return (False, nr_row, None)
    for nr_column in range(N):
        if not check_column(data, nr_column):
            return (False, None, nr_column)
          
    n = int(math.sqrt(data.shape[0]))

    for nr_row in range(0,N,n):
        for nr_column in range(0,N,n):
            
            if not check_square(data,nr_column, nr_row):

                return (False, nr_row, nr_column)
              
    return (True, None, None)
    
def check_column(data: np.ndarray, nr_column):
    """
        It accepts a Sudoku representation and checks whether a specific column is correct
    """
    examined_column = data[:,nr_column]
    if len(set(examined_column)) == N:
        return True
    else: 
        return False

def check_square(data: np.ndarray, nr_column, nr_row):
    """
    Assumption: the column number and row number always correspond to the first row and column from which the square begins
    """
    n = int(math.sqrt(data.shape[0]))
    square = data[nr_row:nr_row+n,nr_column:nr_column+n]
 
    square = square.reshape((-1,)) 
    
    if len(set(square)) == N:
        return True
    else:
        return False

def check_row(data: np.ndarray, nr_row: int):
    """
        It accepts a Sudoku representation and checks whether a specific row is correct
    """
    examined_row = data[nr_row,:]
    if len(set(examined_row)) == N:
        return True
    else: 
        return False

class MyException(Exception):
    ...

def board():
    n = int(math.sqrt(N))
    count_from_new = True
    while count_from_new:
        try:
            data = np.zeros((N, N), dtype=int)
            set_ = {i for i in range(1, N+1)}
            for i in range(N):
                for j in range(N):
                    column = set(data[:, j]) 
                    row = set(data[i,:])
                    a = i % n
                    b =j % n
                    square = set(data[i-a:(i-a)+n,j-b:(j-b)+n].reshape((-1,)))
                    allowed = set_ - column - row - square
                    if len(allowed) == 0:
                        raise MyException("empty set")                    
                    selected_value = random.choice(list(allowed))
                    data[i,j] = selected_value
            count_from_new = False
        except MyException as e:
            pass 

    return data

def create_sudoku():
    
    data = board()
    if_ok, wrong_row, wrong_column = check_sudoku(data)

    while not if_ok:
        replace_appropriate_part(data, wrong_row, wrong_column)
        if_ok, wrong_row, wrong_column = check_sudoku(data)

    return data 

def replace_appropriate_part(data, wrong_row, wrong_column):
    list_ = [i for i in range(1, N+1)]
    n = int(math.sqrt(N))
    if wrong_row is not None and wrong_column is not None:
        new_numbers = random.sample(list_,len(list_))
        data[wrong_row:wrong_row+n,wrong_column:wrong_column+n] = np.array(new_numbers).reshape((n,n))
    elif wrong_row is not None:
        data[wrong_row, :] = random.sample(list_,len(list_))
    elif wrong_column is not None:
        data[:,wrong_column] = random.sample(list_,len(list_))

y = np.array(create_sudoku())

nr_of_empty_places = int((N*N)/2) 

print(nr_of_empty_places)

one_D_array = y.flatten()
list_to_empty_places = [i for i in range(N*N)]

empty_places = np.random.choice(list_to_empty_places, nr_of_empty_places, replace=False)
one_D_array[empty_places] = 0

two_D_array = np.reshape(one_D_array,(N,N))
print_sudoku(two_D_array)
sudoku_solving(two_D_array)