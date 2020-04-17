class Bishop:
    
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
        while (i <= min(self.xpos, self.ypos)): #top-left movement
            square = grid[self.ypos - i][self.xpos - i]
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
        while (i <= min((7-self.xpos), self.ypos)): #top-right movement
            square = grid[self.ypos - i][self.xpos + i]
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
        while (i <= min((7-self.xpos), (7-self.ypos))): #bottom-right movement
            square = grid[self.ypos + i][self.xpos + i]
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
        while (i <= min(self.xpos, (7-self.ypos))): #bottom-left movement
            square = grid[self.ypos + i][self.xpos - i]
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
        return Bishop(color, xpos, ypos, pieceImage, canvasImage, notMoved)