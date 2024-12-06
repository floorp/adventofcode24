import inputfile as input

crossword_array = input.realfile
total = 0
def masFind(row_in,col_in):
    global total
    if col_in != len(crossword_array)-1 and row_in != len(crossword_array[0])-1:    
        # remaining_len = (len(crossword_array)-1) -row_in
        # if remaining_len >=0:
        if crossword_array[row_in-1][col_in-1] == "M" and crossword_array[row_in-1][col_in+1] == "S" and crossword_array[row_in+1][col_in-1] == "M" and crossword_array[row_in+1][col_in+1] == "S":
            # print(f"sit 1 A at {row_in,col_in}")
            total = total+1            
        if crossword_array[row_in-1][col_in-1] == "S" and crossword_array[row_in-1][col_in+1] == "M" and crossword_array[row_in+1][col_in-1] == "S" and crossword_array[row_in+1][col_in+1] == "M":
            # print(f"sit 2 A at {row_in,col_in}")
            total = total+1
        if crossword_array[row_in-1][col_in-1] == "S" and crossword_array[row_in-1][col_in+1] == "S" and crossword_array[row_in+1][col_in-1] == "M" and crossword_array[row_in+1][col_in+1] == "M":
            # print(f"sit 3 A at {row_in,col_in}")
            total = total+1
        if crossword_array[row_in-1][col_in-1] == "M" and crossword_array[row_in-1][col_in+1] == "M" and crossword_array[row_in+1][col_in-1] == "S" and crossword_array[row_in+1][col_in+1] == "S":
            # print(f"sit 4 A at {row_in,col_in}")
            total = total+1


def firstLetterLoc():
    print("firstletterloc")
    row_in = 0
    col_in = 0
    for row in crossword_array:
        # print(row)
        for col in row:
            if col == "A":
                # print(f"A at {row_in,col_in}")
                masFind(row_in,col_in)
            col_in = col_in+1
        col_in = 0
        row_in = row_in+1
    row_in =0
    print(total)


firstLetterLoc()