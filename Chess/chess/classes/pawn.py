from classes.piece import Piece
from functions.pieces import Pieces

class Pawn(Piece):

    def __init__(self):
        super().__init__('P')
        self.player = ''
        self.id = ''
        self.position = ''

    def move(self, Pawn):
        self.moves = Pieces.moves(Pawn)
        return self.moves
            