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
            #Delete the piece to move from canvas and grid
            self.board.delete(self.pieceToMove.canvasImage)
            self.grid[self.pieceToMove.ypos][self.pieceToMove.xpos].piece = None

            #Checks if we just captured a piece
            if (selectedPiece is not None):
                self.board.delete(selectedPiece.canvasImage)
                if (selectedPiece.color == "White"):
                    self.whitePieces.remove(selectedPiece)
                else:
                    self.blackPieces.remove(selectedPiece)

            #Create new image on new position
            newx = 39.5 + selectedSquare.xpos * 75
            newy = 39.5 + selectedSquare.ypos * 75
            c = self.board.create_image(newx, newy, image=self.pieceToMove.pieceImage)
            self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = self.pieceToMove.newPosition(
                self.pieceToMove.color,
                selectedSquare.xpos,
                selectedSquare.ypos,
                self.pieceToMove.pieceImage,
                c,
                False
            )
            
            #change the position of piece in white or black pieces list
            if (self.pieceToMove.color == "White"):
                self.whitePieces.remove(self.pieceToMove)
                self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
            
            else:
                self.blackPieces.remove(self.pieceToMove)
                self.blackPieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)

            #Checks if we just castled king-side, if so we want to move the rook as well
            if type(self.pieceToMove) == King and self.pieceToMove.xpos == 4 and selectedSquare.xpos == 6:
                #Create new image on new position
                newx = 39.5 + 5 * 75
                newy = 39.5 + self.pieceToMove.ypos * 75
                castleRook = self.grid[self.pieceToMove.ypos][7].piece
                c = self.board.create_image(newx, newy, image=castleRook.pieceImage)
                self.grid[self.pieceToMove.ypos][5].piece = castleRook.newPosition(
                    self.pieceToMove.color,
                    5,
                    self.pieceToMove.ypos,
                    castleRook.pieceImage,
                    c,
                    False
                )

                self.board.delete(self.grid[self.pieceToMove.ypos][7].piece.canvasImage)
                self.grid[self.pieceToMove.ypos][7].piece = None

                if (castleRook.color == "White"):
                    self.whitePieces.remove(castleRook)
                    self.whitePieces.append(self.grid[self.pieceToMove.ypos][5].piece)
                else:
                    self.blackPieces.remove(castleRook)
                    self.blackPieces.append(self.grid[self.pieceToMove.ypos][5].piece)
            
            #Checks if we just castled queen-side, if so we want to move the rook as well
            if type(self.pieceToMove) == King and self.pieceToMove.xpos == 4 and selectedSquare.xpos == 2:
                #Create new image on new position
                newx = 39.5 + 3 * 75
                newy = 39.5 + self.pieceToMove.ypos * 75
                castleRook = self.grid[self.pieceToMove.ypos][0].piece
                c = self.board.create_image(newx, newy, image=castleRook.pieceImage)
                self.grid[self.pieceToMove.ypos][3].piece = castleRook.newPosition(
                    self.pieceToMove.color,
                    3,
                    self.pieceToMove.ypos,
                    castleRook.pieceImage,
                    c,
                    False
                )

                self.board.delete(self.grid[self.pieceToMove.ypos][0].piece.canvasImage)
                self.grid[self.pieceToMove.ypos][0].piece = None

                if (castleRook.color == "White"):
                    self.whitePieces.remove(castleRook)
                    self.whitePieces.append(self.grid[self.pieceToMove.ypos][3].piece)
                else:
                    self.blackPieces.remove(castleRook)
                    self.blackPieces.append(self.grid[self.pieceToMove.ypos][3].piece)

            #Checks if we just promoted a pawn
            if (type(self.pieceToMove) == Pawn and (selectedSquare.ypos == 0 or selectedSquare.ypos == 7)):
                promote = simpledialog.askstring(title="Test", prompt="What do you want to promote to?")
                if (promote == "Knight"):
                    if (selectedSquare.ypos == 7):
                        self.blackPieces.remove(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                        self.board.delete(c)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                        c = self.board.create_image(newx, newy, image=self.bnPhoto)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Knight(
                            self.pieceToMove.color,
                            selectedSquare.xpos,
                            selectedSquare.ypos,
                            self.bnPhoto,
                            c,
                            False
                        )
                        self.blackPieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)

                    else:
                        self.whitePieces.remove(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                        self.board.delete(c)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                        c = self.board.create_image(newx, newy, image=self.wnPhoto)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Knight(
                            self.pieceToMove.color,
                            selectedSquare.xpos,
                            selectedSquare.ypos,
                            self.wnPhoto,
                            c,
                            False
                        )
                        self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                else:
                    if (selectedSquare.ypos == 7):
                        self.blackPieces.remove(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                        self.board.delete(c)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                        c = self.board.create_image(newx, newy, image=self.bqPhoto)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Queen(
                            self.pieceToMove.color,
                            selectedSquare.xpos,
                            selectedSquare.ypos,
                            self.bqPhoto,
                            c,
                            False
                        )
                        self.blackPieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                    else:
                        self.whitePieces.remove(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)
                        self.board.delete(c)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = None
                        c = self.board.create_image(newx, newy, image=self.wqPhoto)
                        self.grid[selectedSquare.ypos][selectedSquare.xpos].piece = Queen(
                            self.pieceToMove.color,
                            selectedSquare.xpos,
                            selectedSquare.ypos,
                            self.wqPhoto,
                            c,
                            False
                        )
                        self.whitePieces.append(self.grid[selectedSquare.ypos][selectedSquare.xpos].piece)

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

    def evaluate(self, position, whitePieces, blackPieces):
        whiteScore = 0
        blackScore = 0

        for piece in whitePieces:
            if (type(piece) == Pawn):
                whiteScore += 1
            elif (type(piece) == Knight):
                whiteScore += 3
            elif (type(piece) == Bishop):
                whiteScore += 3
            elif (type(piece) == Rook):
                whiteScore += 5
            elif (type(piece) == Queen):
                whiteScore += 9
        for piece in blackPieces:
            if (type(piece) == Pawn):
                blackScore += 1
            elif (type(piece) == Knight):
                blackScore += 3
            elif (type(piece) == Bishop):
                blackScore += 3
            elif (type(piece) == Rook):
                blackScore += 5
            elif (type(piece) == Queen):
                blackScore += 9
        
        return whiteScore - blackScore


    def copyList(self, list1):
        result = []
        for e in list1:
            result.append(e)
        return result

    def copyListList(self, list1):
        result = []
        for e in list1:
            row = []
            for i in e:
                row.append(i)
            result.append(row)
        return result
    


root = Tk()
game = ChessGame(root)
root.mainloop()