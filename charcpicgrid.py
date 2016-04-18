grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# i will need to print[1,0], [2,0],[3,0]...[8,0]
# then[1,1],[2,1],[3,1]...[8,1]
#then [1,2],[2,2]...[8,2]
#...[8,5]
# increase x value by one keep y constant until x reaches max then increase y by one
x=0
y=0
def base():
    global x
    global y
    x+=1
    if x==(len(grid)-1):
                y+=1
                x=0
try:
    while x<=len(grid):
            if x<len(grid)-2:
                print(grid[x][y],end='')
                base()
            else:
                print(grid[x][y])
                base()
except IndexError:
    import sys
    sys.exit


