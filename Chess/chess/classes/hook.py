from classes.piece import Piece
from functions.pieces import Pieces

class Hook(Piece):

    def __init__(self):
        super().__init__('H')
        self.player = ''
        self.id = ''
        self.position = ''
    
    def move(self, Hook):
        self.moves = Pieces.moves(Hook)
        return self.moves
