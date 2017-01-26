def print_boarder(width, char1, char2):
    return(char1 + char2*width)
    
def print_grid(boxes, width):
    boarder = ''
    midle = ''
    for i in range(boxes):
        boarder = boarder + print_boarder(width, '+', '-')
        midle = midle + print_boarder(width, '|', ' ')
    boarder = boarder + '+'
    midle = midle + '|'
    for j in range(boxes):
        print(boarder)
        for k in range(width):
            print(midle)
    print(boarder)

print_grid(5,3)    
