import copy

#Simple bruteforcing Sudoku solver with backtracking 

sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
]

def get_possible_values(puzzle, row, column):
    possible_values = []
    tmp_possible = []
    column_array = []

    #check for missing numbers in row

    for i in range(9):
        if (i+1) not in puzzle[row]:
            possible_values.append(i+1)

        column_array.append(puzzle[i][column])

    #check for missing numbers in column
    for i in possible_values:
        if (i) not in column_array:
             tmp_possible.append(i)
    possible_values = copy.copy(tmp_possible)
    tmp_possible = []

    cluster = ClusterCheck(puzzle, row, column)
    for i in possible_values:
        if (i) not in cluster:
             tmp_possible.append(i)
    possible_values = copy.copy(tmp_possible)
        
    return possible_values

def ClusterCheck(puzzle, row, column):
    x = []
    y = []
    missing = []
    if row <= 2:
        x = [0,1,2]
    elif row >= 6:
        x = [6,7,8]
    else:
        x = [3,4,5]

    if column <= 2:
        y = [0,1,2]
    elif column >= 6:
        y = [6,7,8]
    else:
        y = [3,4,5]
    
    for i in x:
        for j in y:
            missing.append(puzzle[i][j])
    
    return missing

def check_if_solved(puzzle):

    for i in range(9):
        for value in range(1,10):
            if value not in puzzle[i]:
                return False

            for row in range(9):
                if puzzle[row][i] == value:
                    break
                elif row == 8:
                    return False
            
            #ClusterCheck 3*3 +2
            for cluster_x in range(3):
                for cluster_y in range(3):
                    tmp_array = []
                    for k in range(3):
                        for n in range(3):
                            tmp_array.append(puzzle[cluster_x*3+k][cluster_y*3+n])
                    if value not in tmp_array:
                        return False
    return True

def solver(puzzle, counter=None):
    tmp_puzzle = copy.deepcopy(puzzle)
    count = 0
    solved = False
    if counter == None:
        count = 0
    else:
        count = counter
    for row in range(9):
        for column in range(9):
            if tmp_puzzle[row][column] == 0:
                possible_numbers = get_possible_values(tmp_puzzle, row, column)
                if  len(possible_numbers) == 0:
                    if row != 8 or column != 8:
                        return False, puzzle
                    elif row == 8 and column == 8:
                        return check_if_solved(puzzle), puzzle   
                        
                for trynumber in possible_numbers:
                    tmp_puzzle[row][column] = trynumber
                    if check_if_solved(tmp_puzzle):
                        return True, tmp_puzzle                                      
                    else:
                         solved, mod_puzzle = solver(tmp_puzzle, count+1)
                    if solved and count != 0:
                        return True, mod_puzzle
                    elif solved and count == 0:
                        return mod_puzzle
                return False, puzzle
    
#get_possible_values(sudoku,0,0)

printme = solver(sudoku)

for i in range(9):
    print(printme[i])
    
