from classes.piece import Piece
from functions.pieces import Pieces

class Queen(Piece):

    def __init__(self):
        super().__init__('Q')
        self.player = ''
        self.id = ''
        self.position = ''

    def move(self, Queen):
        self.moves = Pieces.moves(Queen)
        return self.moves
