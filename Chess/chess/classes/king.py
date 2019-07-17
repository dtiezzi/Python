from classes.piece import Piece
from functions.pieces import Pieces

class King(Piece):

    def __init__(self):
        super().__init__('KK')
        self.player = ''
        self.id = ''
        self.position = ''
    
    def move(self, King):
        self.moves = Pieces.moves(King)
        return self.moves
