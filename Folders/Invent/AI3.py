#Reversegam: a clone of Othello/Reversi		
import random		
import sys		
WIDTH = 8  	
HEIGHT = 8 	
def drawBoard(board):				
    print('  12345678')		
    print(' +--------+')		
    for y in range(HEIGHT):		
        print('%s|' % (y+1), end='')		
        for x in range(WIDTH):		
            print(board[x][y], end='')		
            print('|%s' % (y+1))		
    print(' +--------+')		
    print('  12345678')		
			
def getNewBoard():		
    
    board = []		
    for i in range(WIDTH):		
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])		
    return board		
        
def isValidMove(board, tile, xstart, ystart):		
    
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):		
        return False		
        
    if tile == 'X':		
        otherTile = 'O'		
    else:		
        otherTile = 'X'		
        
    tilesToFlip = []		
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:		
        x, y = xstart, ystart		
        x += xdirection 	
        y += ydirection 	
        while isOnBoard(x, y) and board[x][y] == otherTile:		
            x += xdirection		
            y += ydirection		
            if isOnBoard(x, y) and board[x][y] == tile:		
                
                while True:		
                    x -= xdirection		
                    y -= ydirection		
                    if x == xstart and y == ystart:		
                        break		
                    tilesToFlip.append([x, y])		
        
    if len(tilesToFlip) == 0: 
        return False		
    return tilesToFlip		
        
def isOnBoard(x, y):		
    	
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1		
        
def getBoardWithValidMoves(board, tile):		
    
    boardCopy = getBoardCopy(board)		
        
    for x, y in getValidMoves(boardCopy, tile):		
        boardCopy[x][y] = '.'		
    return boardCopy		
        
def getValidMoves(board, tile):		
    
    validMoves = []		
    for x in range(WIDTH):		
        for y in range(HEIGHT):		
            if isValidMove(board, tile, x, y) != False:		
                validMoves.append([x, y])		
    return validMoves		
        
def getScoreOfBoard(board):		
    
    xscore = 0		
    oscore = 0		
    for x in range(WIDTH):		
        for y in range(HEIGHT):		
            if board[x][y] == 'X':		
                xscore += 1		
            if board[x][y] == 'O':		
                oscore += 1		
    return {'X':xscore, 'O':oscore}		
        
def enterPlayerTile():		
    
    tile = ''		
    while not (tile == 'X' or tile == 'O'):		
        print('Do you want to be X or O?')		
        tile = input().upper()		
        
    
    if tile == 'X':		
        return ['X', 'O']		
    else:		
        return ['O', 'X']		
        
def whoGoesFirst():			
    if random.randint(0, 1) == 0:		
        return 'computer'		
    else:		
        return 'player'		
        
def makeMove(board, tile, xstart, ystart):			
    tilesToFlip = isValidMove(board, tile, xstart, ystart)		
        
    if tilesToFlip == False:		
        return False		
        
    board[xstart][ystart] = tile		
    for x, y in tilesToFlip:		
        board[x][y] = tile		
    return True		
        
def getBoardCopy(board):			
    boardCopy = getNewBoard()		
        
    for x in range(WIDTH):		
        for y in range(HEIGHT):		
            boardCopy[x][y] = board[x][y]		
        
    return boardCopy		
        
def isOnCorner(x, y):			
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)		
        
        
def getCornerBestMove(board, computerTile):				
    possibleMoves = getValidMoves(board, computerTile)		
    random.shuffle(possibleMoves) 
    for x, y in possibleMoves:		
        if isOnCorner(x, y):		
            return [x, y]		
        	
    bestScore = -1		
    for x, y in possibleMoves:		
        boardCopy = getBoardCopy(board)		
        makeMove(boardCopy, computerTile, x, y)		
        score = getScoreOfBoard(boardCopy)[computerTile]		
        if score > bestScore:		
            bestMove = [x, y]		
            bestScore = score		
    return bestMove		
        
def getWorstMove(board, tile):		
    possibleMoves = getValidMoves(board, tile)		
    random.shuffle(possibleMoves) 	
    worstScore = 64		
    for x, y in possibleMoves:		
        boardCopy = getBoardCopy(board)		
        makeMove(boardCopy, tile, x, y)		
        score = getScoreOfBoard(boardCopy)[tile]		
        if score < worstScore:		
            worstMove = [x, y]		
            worstScore = score		
        
    return worstMove		
        
def getRandomMove(board, tile):		
    possibleMoves = getValidMoves(board, tile)		
    return random.choice(possibleMoves)		
        
def isOnSide(x, y):		
    return x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1		
        
def getCornerSideBestMove(board, tile):				
    possibleMoves = getValidMoves(board, tile)		
    random.shuffle(possibleMoves) 		
        		
    for x, y in possibleMoves:		
        if isOnCorner(x, y):		
            return [x, y]		
        		
    for x, y in possibleMoves:		
        if isOnSide(x, y):		
            return [x, y]		
        
    return getCornerBestMove(board, tile)	
        
def printScore(board, computer2, computerTile):		
    scores = getScoreOfBoard(board)		
    print('You: %s points. Computer: %s points.' % (scores[computer2], scores[computerTile]))		
        
def playGame(computer2, computerTile):		
    turn = whoGoesFirst()				
    board = getNewBoard()		
    board[3][3] = 'X'		
    board[3][4] = 'O'		
    board[4][3] = 'O'		
    board[4][4] = 'X'		
        
    while True:		
        playerValidMoves = getValidMoves(board, computer2)		
        computerValidMoves = getValidMoves(board, computerTile)		
        
        if playerValidMoves == [] and computerValidMoves == []:		
            return board 		
        
        elif turn == 'player': 		
            if playerValidMoves != []:		
                	
        
                move = getCornerSideBestMove(board, computer2)		
                		
                makeMove(board, computer2, move[0], move[1])		
            turn = 'computer'		
        
        elif turn == 'computer': 	
            if computerValidMoves != []:				
                move = getCornerBestMove(board, computerTile)		
                makeMove(board, computerTile, move[0], move[1])		
            turn = 'player'		
        
NUM_GAMES = 150
xWins = oWins = ties = 0		
print('Welcome to Reversegam!')		
        
computer2, computerTile = ['X', 'O'] 		
        
for i in range(NUM_GAMES):	
    finalBoard = playGame(computer2, computerTile)		
        
    		
    
    scores = getScoreOfBoard(finalBoard)		
    print('#%s: X scored %s points. O scored %s points.' % (i + 1, scores['X'], scores['O']))		
    if scores[computer2] > scores[computerTile]:		
        xWins += 1 
    elif scores[computer2] < scores[computerTile]:		
        oWins += 1 
    else:		
        ties += 1 
print('X wins: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))		
print('O wins: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))		
print('Ties:   %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))