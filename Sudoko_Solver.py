def check(number,row,column,matrix):
    for i in range(0,len(matrix[row])):
        if(matrix[row][i] == number and i != column):
            return False
    for i in range(0,len(matrix)):
        if(matrix[i][column] == number and i != row):
            return False
    for i in range(0 + row - (row % 3),3 + row - (row % 3)):
        for j in range(0 + column - (column % 3), 3 + column - (column % 3)):
            if(matrix[i][j] == number and i != row and j != column):
                return False
    return True
def show_case_matrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            print(matrix[i][j]," ",end="")
            if(j%3 == 2):
                print("|"," ",end="")
        if(i%3 == 2):
            print("\n","-"*(11*len(matrix[0])//3),end="",sep="")
        print()
def empty_check(matrix):
    global l
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if(matrix[i][j] == 0):
                l = [i,j]
                return True
    return False
l = [0,0]
def sudoko_solver(matrix):
    if(not empty_check(matrix)):
        return True
    row,column = l[0],l[1]
    for _ in range(1,10):
        if(check(_,row,column,matrix)):
            matrix[row][column] = _
            if(sudoko_solver(matrix)):
                return True
            matrix[row][column]=0
    return False

matrix=[  [3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]
     ]


if(sudoko_solver(matrix)):
    show_case_matrix(matrix)
else:
    print("No solution")