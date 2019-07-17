from classes.piece import Piece
from functions.pieces import Pieces

class Bishop(Piece):

    def __init__(self):
        super().__init__('B')
        self.player = ''
        self.id = ''
        self.position = ''
    
    def move(self, Bishop):
        self.moves = Pieces.moves(Bishop)
        return self.moves