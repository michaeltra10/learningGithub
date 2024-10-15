#creates a chessboard in the form of a list
def chessboard():
    global chessBoard
    chessBoard = [[" ","H","G","F","E","D","C","B","A"],
                  ["1","r","n","b","q","k","b","n","r"],
                  ["2","p","p","p","p","p","p","p","p"],
                  ["3",".",".",".",".",".",".",".","."],
                  ["4",".",".",".",".",".",".",".","."],
                  ["5",".",".",".",".",".",".",".","."],
                  ["6",".",".",".",".",".",".",".","."],
                  ["7","P","P","P","P","P","P","P","P"],
                  ["8","R","N","B","Q","K","B","N","R"]]
    
#prints the current chessboard
def printChessboard():
    global chessBoard
    for i in range(9):
        for t in range(9):
            print(chessBoard[i][t], end=" ")
        print()    

#receives the players move and returns it
def userInput():
    userInput = input("make your move, i.e H2 H3\n")
    return userInput

#making sure syntax was put in properly
def validNotation():
    global computerMove
    while True:
        chessMove = userInput()
        if len(chessMove) != 5:
            print("that is not valid notation. Try again.1")
            continue
        move = chessMove.split()
        row1 = move[0][0].lower()
        column1 = move[0][1]
        row2 = move[1][0].lower()
        column2 = move[1][1]
       
        if (row1 == 'h' or row1 == 'g' or row1 == 'f' or row1 == 'e' or row1 == 'd' or row1 == 'c' or row1 == 'b' or row1 == 'a') and \
           (row2 == 'h' or row2 == 'g' or row2 == 'f' or row2 == 'e' or row2 == 'd' or row2 == 'c' or row2 == 'b' or row2 == 'a') and \
           (column1 == '1' or column1 == '2' or column1 == '3' or column1 == '4' or column1 == '5' or column1 == '6' or column1 == '7' or column1 == '8') and \
           (column2 == '1' or column2 == '2' or column2 == '3' or column2 == '4' or column2 == '5' or column2 == '6' or column2 == '7' or column2 == '8'):
            computerMove = [row1, column1, row2, column2]
            return False
        else:
            print("that is not valid notation2. Try again.2")
            continue

def updateChessBoard():
    #changing current row position to an int
    if computerMove[0] == 'h':
        computerMove[0] = 1
    elif computerMove[0] == 'g':
        computerMove[0] = 2
    elif computerMove[0] == 'f':
        computerMove[0] = 3
    elif computerMove[0] == 'e':
        computerMove[0] = 4    
    elif computerMove[0] == 'd':
        computerMove[0] = 5
    elif computerMove[0] == 'c':
        computerMove[0] = 6
    elif computerMove[0] == 'b':
        computerMove[0] = 7
    elif computerMove[0] == 'a':
        computerMove[0] = 8
    #changing the row to be moved to into an int
    if computerMove[2] == 'h':
        computerMove[2] = 1
    elif computerMove[2] == 'g':
        computerMove[2] = 2
    elif computerMove[2] == 'f':
        computerMove[2] = 3
    elif computerMove[2] == 'e':
        computerMove[2] = 4    
    elif computerMove[2] == 'd':
        computerMove[2] = 5
    elif computerMove[2] == 'c':
        computerMove[2] = 6
    elif computerMove[2] == 'b':
        computerMove[2] = 7
    elif computerMove[2] == 'a':
        computerMove[2] = 8

    x1 = computerMove[0]
    y1 = int(computerMove[1])

    x2 = computerMove[2]
    y2 = int(computerMove[3])
    global chessBoard

    #updating chess board with move
    chessBoard[y2][x2] = chessBoard[y1][x1]
    chessBoard[y1][x1] = '.'
    # h = 1 g = 2 f = 3 e = 4 d = 5 c = 6 b = 7 a = 8
    #[[00,01,02,03,04,05,06,07,08],
    # [10,11,12,13,14,15,16,17,18],
    # [20,21,22,23,24,25,26,27,28],
    # [30,31,32,33,34,35,36,37,38],]
    # [40,41,42,43,44,45,46,47,48]
    
def playGame():
        chessboard()
        printChessboard()
        validNotation()
        updateChessBoard()
        printChessboard()

playGame()