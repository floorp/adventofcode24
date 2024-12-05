import inputfile as input

crossword_array = input.samplefile

total  = 0
def findHorzontalWord(row_in,col_in):
    global total
    if col_in != len(crossword_array)-1:
        next_let = col_in+1
        if crossword_array[row_in][next_let] == "M" and next_let <len(crossword_array[0]):
            next_let = next_let+1
            # print(row_in,next_let)
            if crossword_array[row_in][next_let] == "A"and next_let <len(crossword_array[0]):
                next_let = next_let+1
                if crossword_array[row_in][next_let] == "S" and next_let <len(crossword_array[0]):
                    total = total+1
    if col_in !=0:
        next_let = col_in-1
        if crossword_array[row_in][next_let] == "M" and next_let <len(crossword_array[0]):
            next_let = next_let-1
            if crossword_array[row_in][next_let] == "A"and next_let <len(crossword_array[0]):
                next_let = next_let-1
                if crossword_array[row_in][next_let] == "S":
                    total = total+1
def findVerticalWord(row_in,col_in):
    global total
    if row_in != len(crossword_array)-1:
        next_let = row_in+1
        if crossword_array[next_let][col_in] == "M" and next_let <len(crossword_array):
            next_let = next_let+1
            if crossword_array[next_let][col_in] == "A"and next_let <len(crossword_array):
                next_let = next_let+1
                if crossword_array[next_let][col_in] == "S":
                    total = total+1
    if row_in != 0:
        next_let = row_in-1
        if crossword_array[next_let][col_in] == "M" and next_let <len(crossword_array):
            next_let = next_let-1
            if crossword_array[next_let][col_in] == "A"and next_let <len(crossword_array):
                next_let = next_let-1
                if crossword_array[next_let][col_in] == "S":
                    total = total+1

def findDiagWord(row_in,col_in):
    global total
    if row_in != len(crossword_array)-1 and col_in != 0:
        down = row_in+1
        left = col_in -1
        if crossword_array[down][left] == "M" and down != len(crossword_array)-1 and left != 0:
            down = down+1
            left = left -1
            if crossword_array[down][left] == "A"and down != len(crossword_array)-1 and left != 0:
                down = down+1
                left = left -1
                if crossword_array[down][left] == "S":   
                    total = total+1
    if row_in != len(crossword_array)-1 and col_in != len(crossword_array)-1:
        down = row_in+1
        right = col_in +1
        if crossword_array[down][right] == "M" and down != len(crossword_array)-1 and right != len(crossword_array)-1:
            down = down+1
            right = right +1
            if crossword_array[down][right] == "A"and down != len(crossword_array)-1 and right != len(crossword_array)-1:
                down = down+1
                right = right +1
                if crossword_array[down][right] == "S":
                    total = total+1  
    if row_in != 0 and col_in != len(crossword_array)-1:
        up = row_in-1
        right = col_in +1
        if crossword_array[up][right] == "M" and up != 0 and right != len(crossword_array)-1:
            up = up-1
            right = right +1
            if crossword_array[up][right] == "A"and up != 0 and right != len(crossword_array)-1:
                up = up-1
                right = right +1
                if crossword_array[up][right] == "S":

                    total = total+1  
    if row_in != 0 and col_in != 0:
        up = row_in-1
        left = col_in -1
        if crossword_array[up][left] == "M" and up != 0 and left != 0:
            up = up-1
            left = left -1
            if crossword_array[up][left] == "A"and up != 0 and left != 0:
                up = up-1
                left = left -1
                if crossword_array[up][left] == "S":   
                    total = total+1

def firstLetterLoc():
    print("firstletterloc")
    row_in = 0
    col_in = 0
    for row in crossword_array:
        # print(row)
        for col in row:
            # print(col)
            if col == "X":
                # print(f"x found {row_in,col_in}")
                findHorzontalWord(row_in,col_in)
                findVerticalWord(row_in,col_in)
                findDiagWord(row_in,col_in)
                
            col_in = col_in+1
        col_in = 0
        row_in = row_in+1
    row_in =0
    print(total)


firstLetterLoc()