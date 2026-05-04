def nQueens(n):
    #... board initial
    board = [["." for x in range(n)]for x in range(n)]

    #initialize sets
    cols=set()
    diag1=set()
    diag2=set()

    #backtracking function
    def backtrack(row):
        # if last row , print all the rows and return
        if row == n:
            for r in board:
                print(" ".join(r))
            print()
            return
        
        #if not last row , then traverse each column
        for col in range(n):
            #cols , diag1,diag2 contains all the columns and diagonals that have queen in them , 
            # so if not present in those sets means no queen and is safe to place queen
            # if condition met it skips rest of the part of the loop and goes to next value of col in iteration
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue

            board[row][col]="Q"
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            
            backtrack(row+1)

            board[row][col]="."
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

    backtrack(0)

nQueens(4)


            




    