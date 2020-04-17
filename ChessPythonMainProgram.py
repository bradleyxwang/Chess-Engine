from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
from ChessSquare import *
from Pawn import *
from Rook import *
from Knight import *
from Bishop import *
from Queen import *
from King import *

class ChessGame:

    def __init__(self, master):
        self.board = Canvas(master, width = 602, height = 602)
        self.grid = []
        self.whitePieces = []
        self.blackPieces = []
        self.turn = "White"
        self.isCheck = False
        self.selectPiece = True #true = we are selecting a piece, false = we are selecting a position to move the piece
        self.pieceToMove = None
        self.selectedRectangle = None
        self.possibleMoves = []

        self.board.pack()
        self.create_board(self.board)
        self.initialize_pieces(self.board)
        self.board.bind("<Button-1>", self.movePiece)
        self.master = master
    
    def create_board(self, canvas):
        for i in range(8):
            row = []
            for j in range(8):
                row.append(ChessSquare(None, j, i))
                if ((i+j) % 2 == 0): #light square
                    canvas.create_rectangle(2+j*75, 2+i*75, 2+j*75+75, 2+i*75+75, fill="whitesmoke")
                else: #dark square
                    canvas.create_rectangle(2+j*75, 2+i*75, 2+j*75+75, 2+i*75+75, fill="gray")
            self.grid.append(row)
    
    def initialize_pieces(self, canvas):

        self.bpPhoto = PhotoImage(file="blackpawn.png")
        self.wpPhoto = PhotoImage(file="whitepawn.png")
        self.brPhoto = PhotoImage(file="blackrook.png")
        self.wrPhoto = PhotoImage(file="whiterook.png")
        self.bnPhoto = PhotoImage(file="blackknight.png")
        self.wnPhoto = PhotoImage(file="whiteknight.png")
        self.bbPhoto = PhotoImage(file="blackbishop.png")
        self.wbPhoto = PhotoImage(file="whitebishop.png")
        self.bqPhoto = PhotoImage(file="blackqueen.png")
        self.wqPhoto = PhotoImage(file="whitequeen.png")
        self.bkPhoto = PhotoImage(file="blackking.png")
        self.wkPhoto = PhotoImage(file="whiteking.png")

        for i in range(8):
            c = canvas.create_image(39.5 + i*75, 114.5, image=self.bpPhoto) #Initializes black pawns
            self.grid[1][i].piece = Pawn("Black", i, 1, self.bpPhoto, c, True)
            self.blackPieces.append(self.grid[1][i].piece)

        for i in range(8):
            c = canvas.create_image(39.5 + i*75, 487.5, image=self.wpPhoto) #Initializes white pawns
            self.grid[6][i].piece = Pawn("White", i, 6, self.wpPhoto, c, True)
            self.whitePieces.append(self.grid[6][i].piece)
        
        c = canvas.create_image(39.5, 39.5, image=self.brPhoto) #Initializes black rooks
        self.grid[0][0].piece = Rook("Black", 0, 0, self.brPhoto, c, True)
        self.blackPieces.append(self.grid[0][0].piece)
        c = canvas.create_image(564.5, 39.5, image=self.brPhoto)
        self.grid[0][7].piece = Rook("Black", 7, 0, self.brPhoto, c, True)
        self.blackPieces.append(self.grid[0][7].piece)


        c = canvas.create_image(39.5, 564.5, image=self.wrPhoto) #Initializes white rooks
        self.grid[7][0].piece = Rook("White", 0, 7, self.wrPhoto, c, True)
        self.whitePieces.append(self.grid[7][0].piece)
        c = canvas.create_image(564.5, 564.5, image=self.wrPhoto)
        self.grid[7][7].piece = Rook("White", 7, 7, self.wrPhoto, c, True)
        self.whitePieces.append(self.grid[7][7].piece)
        
        c = canvas.create_image(114.5, 39.5, image=self.bnPhoto) #Initializes black knights
        self.grid[0][1].piece = Knight("Black", 1, 0, self.bnPhoto, c, True)
        self.blackPieces.append(self.grid[0][1].piece)
        c = canvas.create_image(489.5, 39.5, image=self.bnPhoto)
        self.grid[0][6].piece = Knight("Black", 6, 0, self.bnPhoto, c, True)
        self.blackPieces.append(self.grid[0][6].piece)

        
        c = canvas.create_image(114.5, 564.5, image=self.wnPhoto) #Initializes white knights
        self.grid[7][1].piece = Knight("White", 1, 7, self.wnPhoto, c, True)
        self.whitePieces.append(self.grid[7][1].piece)
        c = canvas.create_image(489.5, 564.5, image=self.wnPhoto)
        self.grid[7][6].piece = Knight("White", 6, 7, self.wnPhoto, c, True)
        self.whitePieces.append(self.grid[7][6].piece)

        
        c = canvas.create_image(189.5, 39.5, image=self.bbPhoto) #Initializes black bishops
        self.grid[0][2].piece = Bishop("Black", 2, 0, self.bbPhoto, c, True)
        self.blackPieces.append(self.grid[0][2].piece)
        c = canvas.create_image(414.5, 39.5, image=self.bbPhoto)
        self.grid[0][5].piece = Bishop("Black", 5, 0, self.bbPhoto, c, True)
        self.blackPieces.append(self.grid[0][5].piece)

        c = canvas.create_image(189.5, 564.5, image=self.wbPhoto) #Initializes white bishops
        self.grid[7][2].piece = Bishop("White", 2, 7, self.wbPhoto, c, True)
        self.whitePieces.append(self.grid[7][2].piece)
        c = canvas.create_image(414.5, 564.5, image=self.wbPhoto)
        self.grid[7][5].piece = Bishop("White", 5, 7, self.wbPhoto, c, True)
        self.whitePieces.append(self.grid[7][5].piece)

        
        c = canvas.create_image(264.5, 39.5, image=self.bqPhoto) #Initializes black queen
        self.grid[0][3].piece = Queen("Black", 3, 0, self.bqPhoto, c, True)
        self.blackPieces.append(self.grid[0][3].piece)
        c = canvas.create_image(264.5, 564.5, image=self.wqPhoto) #Initializes white queen
        self.grid[7][3].piece = Queen("White", 3, 7, self.wqPhoto, c, True)
        self.whitePieces.append(self.grid[7][3].piece)

        c = canvas.create_image(339.5, 39.5, image=self.bkPhoto) #Initializes black king
        self.grid[0][4].piece = King("Black", 4, 0, self.bkPhoto, c, True)
        self.blackPieces.append(self.grid[0][4].piece)
        c = canvas.create_image(339.5, 564.5, image=self.wkPhoto) #Initializes white king
        self.grid[7][4].piece = King("White", 4, 7, self.wkPhoto, c, True)
        self.whitePieces.append(self.grid[7][4].piece)
    
    def movePiece(self, event):
        x = (event.x - 2) // 75
        y = (event.y - 2) // 75
        selectedSquare = self.grid[y][x]
        selectedPiece = selectedSquare.piece


        if (self.selectPiece == True and selectedPiece is not None and selectedPiece.color == self.turn): #If we click on a valid piece
            self.board.delete(selectedPiece.canvasImage)
            selectedPiece.canvasImage = None
            self.selectedRectangle = self.board.create_rectangle(2+x*75, 2+y*75, 2+x*75+75, 2+y*75+75, fill="red") 
            #Fill the background square red and redraw piece image
            c = self.board.create_image(39.5+x*75, 39.5+y*75, image=selectedPiece.pieceImage)
            selectedPiece.canvasImage = c
            self.selectPiece = False
            self.pieceToMove = selectedPiece

            #get the piece's possible moves
            self.possibleMoves = self.removeCheckMoves(self.pieceToMove.getMoves(self.grid), self.pieceToMove, self.grid,
                self.whitePieces, self.blackPieces)

        elif (self.selectPiece == False and selectedSquare in self.possibleMoves):

            self.makeMove(self.pieceToMove, selectedSquare)
            self.postMove()
            AIMove = self.minimax(
                self.copyGrid(self.grid),
                self.copyList(self.whitePieces),
                self.copyList(self.blackPieces),
                [], #Piece list
                [], #Move list
                3, #depth
                -10000, #alpha
                10000, #beta
                True #If we want to maximize the current player
            )

            self.makeMove(AIMove[2][0], AIMove[1][0])
            self.postMove()
            
        #If we made an illegal move, do nothing
        else:
            self.selectPiece = True
            self.pieceToMove = None
            self.board.delete(self.selectedRectangle)
            self.selectedRectangle = None
    
    #Removes all moves that result in the current player being in check
    def removeCheckMoves(self, moveList, piece, grid, whitePieces, blackPieces):
        result = []
        whiteKing = self.getKing(whitePieces)
        blackKing = self.getKing(blackPieces)
        for move in moveList:
            originalPiece = grid[move.ypos][move.xpos].piece 
            grid[piece.ypos][piece.xpos].piece = None
            grid[move.ypos][move.xpos].piece = piece.newPosition(
                piece.color,
                move.xpos,
                move.ypos,
                piece.pieceImage,
                piece.canvasImage,
                False
            )
            if (type(piece) == King and piece.color == "White"): #If we are trying to move the white king
                whiteKing = grid[move.ypos][move.xpos].piece
            elif (type(piece) == King and piece.color == "Black"): #If we are trying to move the black king
                blackKing = grid[move.ypos][move.xpos].piece

            if (piece.color == "White" and not whiteKing.yesCheck(grid)):
                result.append(move)
            elif (piece.color == "Black" and not blackKing.yesCheck(grid)):
                result.append(move)
            #reset
            grid[move.ypos][move.xpos].piece = originalPiece
            grid[piece.ypos][piece.xpos].piece = piece
        return result

    def getKing(self, pieceList):
        for piece in pieceList:
            if (type(piece) == King):
                return piece
        
    
    #Checks if there are no more moves left
    def noMoreMoves(self):
        if (self.turn == "White"):
            for piece in self.whitePieces:
                if (len(self.removeCheckMoves(piece.getMoves(self.grid), piece, self.grid,
                self.whitePieces, self.blackPieces)) > 0):
                    return False
        else:
            for piece in self.blackPieces:
                if (len(self.removeCheckMoves(piece.getMoves(self.grid), piece, self.grid,
                self.whitePieces, self.blackPieces)) > 0):
                    return False
        return True

    def makeMove(self, selectedPiece, selectedSquare):
        #Delete the piece to move from canvas and grid
        self.board.delete(selectedPiece.canvasImage)
        self.grid[selectedPiece.ypos][selectedPiece.xpos].piece = None

        #Checks if we just captured a piece
        if (selectedSquare.piece is not None):
            self.board.delete(selectedSquare.piece.canvasImage)
            if (selectedSquare.piece.color == "White"):
                self.remove(self.whitePieces, selectedSquare.piece)
            else:
                self.remove(self.blackPieces, selectedSquare.piece)

        #Create new image on new position
        newx = 39.5 + selectedSquare.xpos * 75
        newy = 39.5 + selectedSquare.ypos * 75
        c = self.board.create_image(newx, newy, image=selectedPiece.pieceImage)
        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = selectedPiece.newPosition(
            selectedPiece.color,
            selectedSquare.xpos,
            selectedSquare.ypos,
            selectedPiece.pieceImage,
            c,
            False
        )
            
        #change the position of piece in white or black pieces list
        if (selectedPiece.color == "White"):
            self.remove(self.whitePieces, selectedPiece)
            self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
            
        else:
            self.remove(self.blackPieces, selectedPiece)
            self.blackPieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)

        #Checks if we just castled king-side, if so we want to move the rook as well
        if type(selectedPiece) == King and selectedPiece.xpos == 4 and selectedSquare.xpos == 6:
            #Create new image on new position
            newx = 39.5 + 5 * 75
            newy = 39.5 + selectedPiece.ypos * 75
            castleRook = self.grid[selectedPiece.ypos][7].piece
            c = self.board.create_image(newx, newy, image=castleRook.pieceImage)
            self.grid[selectedPiece.ypos][5].piece = castleRook.newPosition(
                selectedPiece.color,
                5,
                selectedPiece.ypos,
                castleRook.pieceImage,
                c,
                False
            )

            self.board.delete(self.grid[selectedPiece.ypos][7].piece.canvasImage)
            self.grid[selectedPiece.ypos][7].piece = None

            if (castleRook.color == "White"):
                self.remove(self.whitePieces, castleRook)
                self.whitePieces.append(self.grid[selectedPiece.ypos][5].piece)
            else:
                self.remove(self.blackPieces, castleRook)
                self.blackPieces.append(self.grid[selectedPiece.ypos][5].piece)
            
        #Checks if we just castled queen-side, if so we want to move the rook as well
        if type(selectedPiece) == King and selectedPiece.xpos == 4 and selectedSquare.xpos == 2:
            #Create new image on new position
            newx = 39.5 + 3 * 75
            newy = 39.5 + selectedPiece.ypos * 75
            castleRook = self.grid[selectedPiece.ypos][0].piece
            c = self.board.create_image(newx, newy, image=castleRook.pieceImage)
            self.grid[selectedPiece.ypos][3].piece = castleRook.newPosition(
                selectedPiece.color,
                3,
                selectedPiece.ypos,
                castleRook.pieceImage,
                c,
                False
            )

            self.board.delete(self.grid[selectedPiece.ypos][0].piece.canvasImage)
            self.grid[selectedPiece.ypos][0].piece = None

            if (castleRook.color == "White"):
                self.remove(self.whitePieces, castleRook)
                self.whitePieces.append(self.grid[selectedPiece.ypos][3].piece)
            else:
                self.remove(self.blackPieces, castleRook)
                self.blackPieces.append(self.grid[selectedPiece.ypos][3].piece)

        #Checks if we just promoted a pawn
        if (type(selectedPiece) == Pawn and (selectedSquare.ypos == 0 or selectedSquare.ypos == 7)):
            promote = simpledialog.askstring(title="Test", prompt="What do you want to promote to?")
            if (promote == "Knight"):
                if (selectedSquare.ypos == 7):
                    self.remove(self.blackPieces, self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                    self.board.delete(c)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                    c = self.board.create_image(newx, newy, image=self.bnPhoto)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Knight(
                        selectedPiece.color,
                        selectedSquare.xpos,
                        selectedSquare.ypos,
                        self.bnPhoto,
                        c,
                        False
                    )
                    self.blackPieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)

                else:
                    self.remove(self.whitePieces, self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                    self.board.delete(c)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                    c = self.board.create_image(newx, newy, image=self.wnPhoto)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Knight(
                        selectedPiece.color,
                        selectedSquare.xpos,
                        selectedSquare.ypos,
                        self.wnPhoto,
                        c,
                        False
                    )
                    self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
            else:
                if (selectedSquare.ypos == 7):
                    self.remove(self.blackPieces, self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                    self.board.delete(c)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                    c = self.board.create_image(newx, newy, image=self.bqPhoto)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Queen(
                        selectedPiece.color,
                        selectedSquare.xpos,
                        selectedSquare.ypos,
                        self.bqPhoto,
                        c,
                        False
                    )
                    self.blackPieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                else:
                    self.remove(self.whitePieces, self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                    self.board.delete(c)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                    c = self.board.create_image(newx, newy, image=self.wqPhoto)
                    self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Queen(
                        selectedPiece.color,
                        selectedSquare.xpos,
                        selectedSquare.ypos,
                        self.wqPhoto,
                        c,
                        False
                    )
                    self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
    
    def postMove(self):

        #Checks if someone is in check

        if self.getKing(self.blackPieces).yesCheck(self.grid) or \
            self.getKing(self.whitePieces).yesCheck(self.grid):
            self.isCheck = True
        else:
            self.isCheck = False

        #Reset everything else
        self.selectPiece = True
        self.pieceToMove = None
        self.board.delete(self.selectedRectangle)
        self.selectedRectangle = None
        self.possibleMoves = []
            
        #Changes the turn to the opposing person's turn
        if (self.turn == "White"):
            self.turn = "Black"
        else:
            self.turn = "White"

        #Checks if we have a draw
        if (self.noMoreMoves() and not self.isCheck):
            tkinter.messagebox.showinfo("Game Over", "Draw!")
            self.master.quit()

        #Checks if we have a win
        if (self.noMoreMoves() and self.isCheck):
            tkinter.messagebox.showinfo("Game Over", "Check Mate!")
            self.master.quit()

    def minimax(self, grid, whitePieces, blackPieces, thePieceList, theMoveList, depth, a, b, maximizingSide):
        if depth == 0:
            return self.evaluate(grid, whitePieces, blackPieces), theMoveList, thePieceList
        
        if maximizingSide:
            maxEval = -9999
            goodMoveList = None
            goodPieceList = None
            childrenMoves = {}
            for bpiece in blackPieces: #Gets all possible black moves
                moves = self.removeCheckMoves(bpiece.getMoves(grid), bpiece, grid,
                whitePieces, blackPieces)
                childrenMoves[bpiece] = moves
            noMoreMoves = True
            for bpiece in blackPieces:
                for move in childrenMoves[bpiece]:
                    noMoreMoves = False
                    newPosition, newWhitePieces, newBlackPieces = self.makeAIMove(bpiece, move,
                    self.copyGrid(grid), self.copyList(whitePieces), self.copyList(blackPieces))

                    thePieceList2 = thePieceList + [bpiece]
                    theMoveList2 = theMoveList + [move]

                    evalPos, newMoveList, newPieceList = self.minimax(newPosition, newWhitePieces, 
                    newBlackPieces, thePieceList2, theMoveList2, depth-1, a, b, False)

                    if (maxEval < evalPos):
                        goodMoveList = newMoveList
                        goodPieceList = newPieceList

                    maxEval = max(maxEval, evalPos)
                    a = max(a, evalPos)
                    if b <= a:
                        print("Pruned black")
                        break
            if noMoreMoves:
                return maxEval, theMoveList, thePieceList
            return maxEval, goodMoveList, goodPieceList
        
        else:
            minEval = 9999
            goodMoveList = None
            goodPieceList = None
            childrenMoves = {}
            for wpiece in whitePieces: #Gets all possible white moves
                moves = self.removeCheckMoves(wpiece.getMoves(grid), wpiece, grid,
                whitePieces, blackPieces)
                childrenMoves[wpiece] = moves
            noMoreMoves = True
            for wpiece in whitePieces:
                for move in childrenMoves[wpiece]:
                    noMoreMoves = False
                    newPosition, newWhitePieces, newBlackPieces = self.makeAIMove(wpiece, move,
                    self.copyGrid(grid), self.copyList(whitePieces), self.copyList(blackPieces))

                    thePieceList2 = thePieceList + [wpiece]
                    theMoveList2 = theMoveList + [move]

                    evalPos, newMoveList, newPieceList = self.minimax(newPosition, newWhitePieces, 
                    newBlackPieces, thePieceList2, theMoveList2, depth-1, a, b, True)

                    if (minEval > evalPos):
                        goodMoveList = newMoveList
                        goodPieceList = newPieceList

                    minEval = min(minEval, evalPos)
                    b = max(b, evalPos)
                    if b <= a:
                        print("Pruned White")
                        break
            if noMoreMoves:
                return minEval, theMoveList, thePieceList
            return minEval, goodMoveList, goodPieceList

    def makeAIMove(self, selectedPiece, selectedSquare, grid, whitePieces, blackPieces):
        #Delete the piece to move from grid
        grid[selectedPiece.ypos][selectedPiece.xpos].piece = None

        #Checks if we just captured a piece
        if (selectedSquare.piece is not None):
            if (selectedSquare.piece.color == "White"):
                self.remove(whitePieces, selectedSquare.piece)
            else:
                self.remove(blackPieces, selectedSquare.piece)

        grid[selectedSquare.ypos][selectedSquare.xpos].piece = selectedPiece.newPosition(
            selectedPiece.color,
            selectedSquare.xpos,
            selectedSquare.ypos,
            selectedPiece.pieceImage,
            selectedPiece.canvasImage,
            False
        )
            
        #change the position of piece in white or black pieces list
        if (selectedPiece.color == "White"):
            self.remove(whitePieces, selectedPiece)
            whitePieces.append(grid[selectedSquare.ypos][selectedSquare.xpos].piece)
            
        else:
            self.remove(blackPieces, selectedPiece)
            blackPieces.append(grid[selectedSquare.ypos][selectedSquare.xpos].piece)

        #Checks if we just castled king-side, if so we want to move the rook as well
        if type(selectedPiece) == King and selectedPiece.xpos == 4 and selectedSquare.xpos == 6:
            castleRook = grid[selectedPiece.ypos][7].piece
            grid[selectedPiece.ypos][5].piece = castleRook.newPosition(
                selectedPiece.color,
                5,
                selectedPiece.ypos,
                castleRook.pieceImage,
                castleRook.canvasImage,
                False
            )

            grid[selectedPiece.ypos][7].piece = None

            if (castleRook.color == "White"):
                self.remove(whitePieces, castleRook)
                whitePieces.append(grid[selectedPiece.ypos][5].piece)
            else:
                self.remove(blackPieces, castleRook)
                blackPieces.append(grid[selectedPiece.ypos][5].piece)
            
        #Checks if we just castled queen-side, if so we want to move the rook as well
        if type(selectedPiece) == King and selectedPiece.xpos == 4 and selectedSquare.xpos == 2:
            castleRook = self.grid[selectedPiece.ypos][0].piece
            grid[selectedPiece.ypos][3].piece = castleRook.newPosition(
                selectedPiece.color,
                3,
                selectedPiece.ypos,
                castleRook.pieceImage,
                castleRook.canvasImage,
                False
            )

            grid[selectedPiece.ypos][0].piece = None

            if (castleRook.color == "White"):
                self.remove(whitePieces, castleRook)
                whitePieces.append(grid[selectedPiece.ypos][3].piece)
            else:
                self.remove(blackPieces, castleRook)
                blackPieces.append(grid[selectedPiece.ypos][3].piece)

        #Checks if we just promoted a pawn
        if (type(selectedPiece) == Pawn and (selectedSquare.ypos == 0 or selectedSquare.ypos == 7)):
            if (selectedSquare.ypos == 7):
                self.remove(blackPieces, grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                grid[selectedSquare.ypos][selectedSquare.xpos].piece = Queen(
                    selectedPiece.color,
                    selectedSquare.xpos,
                    selectedSquare.ypos,
                    self.bqPhoto,
                    None,
                    False
                )
                blackPieces.append(grid[selectedSquare.ypos][selectedSquare.xpos].piece)
            else:
                self.remove(whitePieces, grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                grid[selectedSquare.ypos][selectedSquare.xpos].piece = Queen(
                    selectedPiece.color,
                    selectedSquare.xpos,
                    selectedSquare.ypos,
                    self.wqPhoto,
                    None,
                    False
                )
                self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)

        return grid, whitePieces, blackPieces

    def evaluate(self, position, whitePieces, blackPieces):
        whiteScore = 0
        blackScore = 0

        for piece in whitePieces:
            if (type(piece) == Pawn):
                whiteScore += 1
                if (piece.xpos == 2 or piece.xpos == 5) and (piece.ypos <= 4):
                    whiteScore += 0.1
                elif (piece.xpos == 3 or piece.xpos == 4) and (piece.ypos <= 4):
                    whiteScore += 0.4
            elif (type(piece) == Knight):
                whiteScore += 3
                if (piece.xpos >= 2 and piece.xpos <= 5) and (piece.ypos <= 5):
                    whiteScore += .2
            elif (type(piece) == Bishop):
                whiteScore += 3
                if (piece.xpos >= 2 and piece.xpos <= 5) and (piece.ypos <= 5):
                    whiteScore += .2
            elif (type(piece) == Rook):
                whiteScore += 5
            elif (type(piece) == Queen):
                whiteScore += 9
            elif (type(piece) == King):
                if piece.yesCheck(position):
                    whiteScore -= 0.5
        for piece in blackPieces:
            if (type(piece) == Pawn):
                blackScore += 1
                if (piece.xpos == 2 or piece.xpos == 5) and (piece.ypos >= 3):
                    blackScore += 0.1
                elif (piece.xpos == 3 or piece.xpos == 4) and (piece.ypos >= 3):
                    blackScore += 0.4
            elif (type(piece) == Knight):
                blackScore += 3
                if (piece.xpos >= 2 and piece.xpos <= 5) and (piece.ypos >= 2):
                    blackScore += .2
            elif (type(piece) == Bishop):
                blackScore += 3
                if (piece.xpos >= 2 and piece.xpos <= 5) and (piece.ypos >= 2):
                    blackScore += .2
            elif (type(piece) == Rook):
                blackScore += 5
            elif (type(piece) == Queen):
                blackScore += 9
            elif (type(piece) == King):
                if piece.yesCheck(position):
                    blackScore -= 0.5
        
        return blackScore - whiteScore


    def copyList(self, list1):
        result = []
        for e in list1:
            result.append(e.newPosition(
                e.color,
                e.xpos,
                e.ypos,
                e.pieceImage,
                e.canvasImage,
                e.notMoved
            ))
        return result

    def copyGrid(self, grid):
        result = []
        for e in grid:
            row = []
            for i in e:
                row.append(i.newPosition(i.piece, i.xpos, i.ypos))
            result.append(row)
        return result
    
    def remove(self, list, piece):
        for l in list:
            if (type(piece) == type(l) and piece.xpos == l.xpos and piece.ypos == l.ypos):
                list.remove(l)
    


root = Tk()
game = ChessGame(root)
root.mainloop()