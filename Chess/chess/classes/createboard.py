
class Board:

    def __init__(self):
        self.board = [[chr(65+i) + str(j) for j in range(8)] for i in range(8)]
        self.positions = [chr(65+i) + str(j) for j in range(8) for i in range(8)]

    def __str__(self):
        return self.board
