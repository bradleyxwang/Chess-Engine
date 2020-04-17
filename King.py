from ChessSquare import *
from Pawn import *
from Rook import *
from Knight import *
from Bishop import *
from Queen import *

class King:
    
    def __init__(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.pieceImage = pieceImage
        self.canvasImage = canvasImage
        self.notMoved = notMoved
    
    def getMoves(self, grid):
        possibleMoves = []
        #top left
        if (self.xpos-1>-1) and (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos-1].piece is None or \
            grid[self.ypos-1][self.xpos-1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-1][self.xpos-1])
        
        #top
        if (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos].piece is None or \
            grid[self.ypos-1][self.xpos].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-1][self.xpos])
        
        #top right
        if (self.xpos+1<8) and (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos+1].piece is None or \
            grid[self.ypos-1][self.xpos+1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-1][self.xpos+1])

        #left
        if (self.xpos-1>-1) and (grid[self.ypos][self.xpos-1].piece is None or \
            grid[self.ypos][self.xpos-1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos][self.xpos-1])

        #right
        if (self.xpos+1<8) and (grid[self.ypos][self.xpos+1].piece is None or \
            grid[self.ypos][self.xpos+1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos][self.xpos+1])
        
        #bottom left
        if (self.xpos-1>-1) and (self.ypos+1<8) and (grid[self.ypos+1][self.xpos-1].piece is None or \
            grid[self.ypos+1][self.xpos-1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+1][self.xpos-1])
        
        #bottom
        if (self.ypos+1<8) and (grid[self.ypos+1][self.xpos].piece is None or \
            grid[self.ypos+1][self.xpos].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+1][self.xpos])
        
        #bottom right
        if (self.xpos+1<8) and (self.ypos+1<8) and (grid[self.ypos+1][self.xpos+1].piece is None or \
            grid[self.ypos+1][self.xpos+1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+1][self.xpos+1])

        #black castle king side
        if (self.color == "Black"):
            if (self.xpos == 4) and (self.ypos == 0) and (grid[0][5].piece is None) and \
                (grid[0][6].piece is None) and ((type(grid[0][7].piece) == Rook) and \
                    (grid[0][7].piece.color == "Black")) and self.notMoved and grid[0][7].piece.notMoved:
                        possibleMoves.append(grid[0][6])
        
        #white castle king side
        if (self.color == "White"):
            if (self.xpos == 4) and (self.ypos == 7) and (grid[7][5].piece is None) and \
                (grid[7][6].piece is None) and ((type(grid[7][7].piece) == Rook) and \
                    (grid[7][7].piece.color == "White")) and self.notMoved and grid[7][7].piece.notMoved:
                        possibleMoves.append(grid[7][6])

        #black castle queen side
        if (self.color == "Black"):
            if (self.xpos == 4) and (self.ypos == 0) and (grid[0][3].piece is None) and \
                (grid[0][2].piece is None) and (grid[0][1].piece is None) and ((type(grid[0][0].piece) == Rook) and \
                    (grid[0][0].piece.color == "Black")) and self.notMoved and grid[0][0].piece.notMoved:
                        possibleMoves.append(grid[0][2])
        
        #white castle queen side
        if (self.color == "White"):
            if (self.xpos == 4) and (self.ypos == 7) and (grid[7][3].piece is None) and \
                (grid[7][2].piece is None) and (grid[7][1].piece is None) and ((type(grid[7][0].piece) == Rook) and \
                    (grid[7][0].piece.color == "White")) and self.notMoved and grid[7][0].piece.notMoved:
                        possibleMoves.append(grid[7][2])
        
        return possibleMoves
    
    def newPosition(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        return King(color, xpos, ypos, pieceImage, canvasImage, notMoved)
    
    def yesCheck(self, grid):
        i = 1

        while (i <= self.xpos): #left moves
            square = grid[self.ypos][self.xpos - i]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Rook or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1

        i = 1
        while(i <= 7-self.xpos): #right moves
            square = grid[self.ypos][self.xpos + i]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Rook or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1
        
        i = 1
        while (i <= self.ypos): #up moves
            square = grid[self.ypos - i][self.xpos]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Rook or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1
        
        i = 1
        while(i <= 7-self.ypos): #down moves
            square = grid[self.ypos + i][self.xpos]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Rook or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1

        i = 1
        while (i <= min(self.xpos, self.ypos)): #top-left movement
            square = grid[self.ypos - i][self.xpos - i]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Bishop or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color == "White" and type(square.piece) == Pawn \
                    and square.piece.color == "Black"):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1
        
        i = 1
        while (i <= min((7-self.xpos), self.ypos)): #top-right movement
            square = grid[self.ypos - i][self.xpos + i]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Bishop or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color == "White" and type(square.piece) == Pawn \
                    and square.piece.color == "Black"):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1
        
        i = 1
        while (i <= min((7-self.xpos), (7-self.ypos))): #bottom-right movement
            square = grid[self.ypos + i][self.xpos + i]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Bishop or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color == "Black" and type(square.piece) == Pawn \
                    and square.piece.color == "White"):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1
        
        i = 1
        while (i <= min(self.xpos, (7-self.ypos))): #bottom-left movement
            square = grid[self.ypos + i][self.xpos - i]
            if (square.piece is not None):
                if (square.piece.color != self.color and (type(square.piece) == Bishop or \
                    type(square.piece) == Queen)):
                    return True
                elif (i == 1 and self.color == "Black" and type(square.piece) == Pawn \
                    and square.piece.color == "White"):
                    return True
                elif (i == 1 and self.color != square.piece.color and type(square.piece) == King):
                    return True
                else:
                    break
            else:
                i += 1
        

        #hard coded cases for knight check
        #up 2 right 1
        if (self.xpos+1<8) and (self.ypos-2>-1) and (grid[self.ypos-2][self.xpos+1].piece is not None and \
            grid[self.ypos-2][self.xpos+1].piece.color != self.color and \
                type(grid[self.ypos-2][self.xpos+1].piece) == Knight):
            return True
        
        #up 1 right 2
        if (self.xpos+2<8) and (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos+2].piece is not None and \
            grid[self.ypos-1][self.xpos+2].piece.color != self.color and \
                type(grid[self.ypos-1][self.xpos+2].piece) == Knight):
            return True
        
        #down 1 right 2
        if (self.xpos+2<8) and (self.ypos+1<8) and (grid[self.ypos+1][self.xpos+2].piece is not None and \
            grid[self.ypos+1][self.xpos+2].piece.color != self.color and \
                type(grid[self.ypos+1][self.xpos+2].piece) == Knight):
            return True
        
        #down 2 right 1
        if (self.xpos+1<8) and (self.ypos+2<8) and (grid[self.ypos+2][self.xpos+1].piece is not None and \
            grid[self.ypos+2][self.xpos+1].piece.color != self.color and \
                type(grid[self.ypos+2][self.xpos+1].piece) == Knight):
            return True

        #down 2 left 1
        if (self.xpos-1>-1) and (self.ypos+2<8) and (grid[self.ypos+2][self.xpos-1].piece is not None and \
            grid[self.ypos+2][self.xpos-1].piece.color != self.color and \
                type(grid[self.ypos+2][self.xpos-1].piece) == Knight):
            return True

        #down 1 left 2
        if (self.xpos-2>-1) and (self.ypos+1<8) and (grid[self.ypos+1][self.xpos-2].piece is not None and \
            grid[self.ypos+1][self.xpos-2].piece.color != self.color and \
                type(grid[self.ypos+1][self.xpos-2].piece) == Knight):
            return True

        #up 1 left 2
        if (self.xpos-2>-1) and (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos-2].piece is not None and \
            grid[self.ypos-1][self.xpos-2].piece.color != self.color and \
                type(grid[self.ypos-1][self.xpos-2].piece) == Knight):
            return True

        #up 2 left 1
        if (self.xpos-1>-1) and (self.ypos-2>-1) and (grid[self.ypos-2][self.xpos-1].piece is not None and \
            grid[self.ypos-2][self.xpos-1].piece.color != self.color and \
                type(grid[self.ypos-2][self.xpos-1].piece )== Knight):
            return True
        
        return False