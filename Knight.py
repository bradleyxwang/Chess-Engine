class Knight:
    
    def __init__(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.pieceImage = pieceImage
        self.canvasImage = canvasImage
        self.notMoved = notMoved
    
    def getMoves(self, grid):
        possibleMoves = []

        #up 2 right 1
        if (self.xpos+1<8) and (self.ypos-2>-1) and (grid[self.ypos-2][self.xpos+1].piece is None or \
            grid[self.ypos-2][self.xpos+1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-2][self.xpos+1])
        
        #up 1 right 2
        if (self.xpos+2<8) and (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos+2].piece is None or \
            grid[self.ypos-1][self.xpos+2].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-1][self.xpos+2])
        
        #down 1 right 2
        if (self.xpos+2<8) and (self.ypos+1<8) and (grid[self.ypos+1][self.xpos+2].piece is None or \
            grid[self.ypos+1][self.xpos+2].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+1][self.xpos+2])
        
        #down 2 right 1
        if (self.xpos+1<8) and (self.ypos+2<8) and (grid[self.ypos+2][self.xpos+1].piece is None or \
            grid[self.ypos+2][self.xpos+1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+2][self.xpos+1])

        #down 2 left 1
        if (self.xpos-1>-1) and (self.ypos+2<8) and (grid[self.ypos+2][self.xpos-1].piece is None or \
            grid[self.ypos+2][self.xpos-1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+2][self.xpos-1])

        #down 1 left 2
        if (self.xpos-2>-1) and (self.ypos+1<8) and (grid[self.ypos+1][self.xpos-2].piece is None or \
            grid[self.ypos+1][self.xpos-2].piece.color != self.color):
            possibleMoves.append(grid[self.ypos+1][self.xpos-2])

        #up 1 left 2
        if (self.xpos-2>-1) and (self.ypos-1>-1) and (grid[self.ypos-1][self.xpos-2].piece is None or \
            grid[self.ypos-1][self.xpos-2].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-1][self.xpos-2])

        #up 2 left 1
        if (self.xpos-1>-1) and (self.ypos-2>-1) and (grid[self.ypos-2][self.xpos-1].piece is None or \
            grid[self.ypos-2][self.xpos-1].piece.color != self.color):
            possibleMoves.append(grid[self.ypos-2][self.xpos-1])
        return possibleMoves
    def newPosition(self, color, xpos, ypos, pieceImage, canvasImage, notMoved):
        return Knight(color, xpos, ypos, pieceImage, canvasImage, notMoved)