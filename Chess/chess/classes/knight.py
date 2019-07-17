from classes.piece import Piece
from functions.pieces import Pieces

class Knight(Piece):

    def __init__(self):
        super().__init__('K')
        self.player = ''
        self.id = ''
        self.position = ''

    def move(self, Knight):
        self.moves = Pieces.moves(Knight)
        return self.moves
