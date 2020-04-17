class Rook:
    
    def __init__(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.pieceImage = pieceImage
        self.canvasImage = canvasImage
        self.notMoved = notMoved
    
    def getMoves(self, grid):
        possibleMoves = []

        i = 1
        while (i <= self.xpos): #Rook's left moves
            square = grid[self.ypos][self.xpos - i]
            if (square.piece is not None):
                if (square.piece.color != self.color):
                    possibleMoves.append(square)
                    break
                else:
                    break
            else:
                possibleMoves.append(square)
                i += 1
        
        i = 1
        while(i <= 7-self.xpos): #Rook's right moves
            square = grid[self.ypos][self.xpos + i]
            if (square.piece is not None):
                if (square.piece.color != self.color):
                    possibleMoves.append(square)
                    break
                else:
                    break
            else:
                possibleMoves.append(square)
                i += 1
        
        i = 1
        while (i <= self.ypos): #Rook's up moves
            square = grid[self.ypos - i][self.xpos]
            if (square.piece is not None):
                if (square.piece.color != self.color):
                    possibleMoves.append(square)
                    break
                else:
                    break
            else:
                possibleMoves.append(square)
                i += 1
        
        i = 1
        while(i <= 7-self.ypos): #Rook's down moves
            square = grid[self.ypos + i][self.xpos]
            if (square.piece is not None):
                if (square.piece.color != self.color):
                    possibleMoves.append(square)
                    break
                else:
                    break
            else:
                possibleMoves.append(square)
                i += 1
        return possibleMoves

    def newPosition(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        return Rook(color, xpos, ypos, pieceImage, canvasImage, notMoved)