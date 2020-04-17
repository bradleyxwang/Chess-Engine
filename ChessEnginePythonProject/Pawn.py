class Pawn:
    
    def __init__(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.pieceImage = pieceImage
        self.canvasImage = canvasImage
        self.notMoved = notMoved
    
    def getMoves(self, grid):
        possibleMoves = []
        iterator = 1
        if (self.color == "Black"):
            if (self.ypos == 1):
                while (iterator < 3):
                    if (grid[self.ypos+iterator][self.xpos].piece is None):
                        possibleMoves.append(grid[self.ypos+iterator][self.xpos])
                    iterator += 1
            
            else:
                if (grid[self.ypos+1][self.xpos].piece is None):
                    possibleMoves.append(grid[self.ypos+1][self.xpos])
            
            if (self.xpos-1 > -1 and \
                grid[self.ypos+1][self.xpos-1].piece is not None and \
                grid[self.ypos+1][self.xpos-1].piece.color == "White"):
                possibleMoves.append(grid[self.ypos+1][self.xpos-1])
            
            if (self.xpos+1 < 8 and \
                grid[self.ypos+1][self.xpos+1].piece is not None and \
                grid[self.ypos+1][self.xpos+1].piece.color == "White"):
                possibleMoves.append(grid[self.ypos+1][self.xpos+1])
        
        elif (self.color == "White"):
            if (self.ypos == 6):
                while (iterator < 3):
                    if (grid[self.ypos-iterator][self.xpos].piece is None):
                        possibleMoves.append(grid[self.ypos-iterator][self.xpos])
                    iterator += 1
            
            else:
                if (grid[self.ypos-1][self.xpos].piece is None):
                    possibleMoves.append(grid[self.ypos-1][self.xpos])
            
            if (self.xpos-1 > -1 and \
                grid[self.ypos-1][self.xpos-1].piece is not None and \
                grid[self.ypos-1][self.xpos-1].piece.color == "Black"):
                possibleMoves.append(grid[self.ypos-1][self.xpos-1])
            
            if (self.xpos+1 < 8 and \
                grid[self.ypos-1][self.xpos+1].piece is not None and \
                grid[self.ypos-1][self.xpos+1].piece.color == "Black"):
                possibleMoves.append(grid[self.ypos-1][self.xpos+1])
        return possibleMoves

    def newPosition(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        return Pawn(color, xpos, ypos, pieceImage, canvasImage, notMoved)