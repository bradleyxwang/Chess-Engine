class ChessSquare:

    def __init__(self, piece, xpos, ypos):
        self.piece = piece
        self.xpos = xpos
        self.ypos = ypos

    def newPosition(self, piece, xpos, ypos):
        if (piece is None):
            return ChessSquare(piece, xpos, ypos)
        else:
            return ChessSquare(piece.newPosition(
                piece.color,
                piece.xpos,
                piece.ypos,
                piece.pieceImage,
                piece.canvasImage,
                piece.notMoved
            ), xpos, ypos)