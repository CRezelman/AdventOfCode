def day25():
    row = 1
    col = 1
    diag = 1
    code = 20151125
    mul = 252533
    div = 33554393
    next = 0

    while not (row == 2981 and col == 3075):
        next = (code*mul) % div
        code = next
        if (row + col) == (diag + 1) and col == diag:
            diag += 1
            row = col + 1
            col = 1
            continue
        row -= 1
        col += 1
    
    return code

print(day25())

# row, col
#1 1,1 -> 
#2 2,1 -> 1,2 -> 
#3 3,1 -> 2,2 -> 1,3 -> 
#4 4,1 -> 3,2 -> 2,3 -> 1,4 -> 
#5 5,1 -> 4,2 -> 3,3 -> 2,4 -> 1,5 ->
#