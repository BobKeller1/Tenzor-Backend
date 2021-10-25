def readFile(filename):
    with open(filename) as inf:
        sudoku = [
            [0 if el == '.' else int(el) for el in line if el.strip()]
            for line in inf]
        return sudoku

def Write(task):
    with open("solve.txt", "w") as file:
        for line in task:
            file.write(str(line) + '\n')

def nextCell(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def Valid(grid, i, j, e):
    row = all([e != grid[i][x] for x in range(9)])
    if row:
        column = all([e != grid[x][j] for x in range(9)])
        if column:
            topX, topY = 3 * (i // 3), 3 * (j // 3)
            for x in range(topX, topX + 3):
                for y in range(topY, topY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

def solveSudoku(grid, i=0, j=0):
    i, j = nextCell(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if Valid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            grid[i][j] = 0
    return False

task = readFile('task1.txt')
solveSudoku(task)
Write(task)

for line in task:
    print(*(str(symbol).rjust(3) for symbol in line), sep='')

