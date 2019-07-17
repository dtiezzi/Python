from classes.createboard import Board

class Pieces:

    def __init__(self):
        pass

    def swap(startpos, finalpos, poslistplayer1, poslistplayer2, turn):
        if turn == 1:
            piecename = (poslistplayer1[startpos]).lower()
        else:
            piecename = (poslistplayer2[startpos]).lower()
        
        return piecename

    def rmpiece(k, instance, turn):
        instance[turn].pop(k)
        return instance

    def moves(piece):
        b = Board()
        row = ord(piece.position[0])
        col = int(piece.position[1])
        possiblepos = []

        if piece.name == 'P':
            if piece.player == '1':
                if piece.position[0] == 'B':
                    possiblepos.extend([chr(row+1) + str(col), chr(row+2) + str(col), chr(row+1) + str(col+1), chr(row+1) + str(col-1)])
                else:
                    possiblepos.extend([chr(row+1) + str(col), chr(row+1) + str(col+1), chr(row+1) + str(col-1)])
            else:
                if piece.position[0] == 'G':
                    possiblepos.extend([chr(row-1) + str(col), chr(row-2) + str(col),chr(row-1) + str(col-1) , chr(row-1) + str(col+1)])
                else:
                    possiblepos.extend([chr(row-1) + str(col), chr(row-1) + str(col-1) , chr(row-1) + str(col+1)])

        if piece.name == 'KK':
            kkp = [chr(row+1) + str(col), chr(row-1) + str(col), 
                chr(row) + str(col-1), chr(row) + str(col+1),
                chr(row+1) + str(col+1), chr(row+1) + str(col-1),
                chr(row-1) + str(col+1), chr(row-1) + str(col-1)]
            for spot in kkp:
                if spot in b.positions:
                    possiblepos.append(spot)

        

        if piece.name == 'H':
            for l in range(65, 73):
                if chr(l) + str(col) == piece.position:
                    continue
                possiblepos.append(chr(l) + str(col))
            for t in range(8):
                if chr(row) + str(t) == piece.position:
                    continue
                possiblepos.append(chr(row) + str(t))

        if piece.name == 'B':
            bp = [[chr(row+i) + str(col+i), chr(row+i) + str(col-i)] for i in range(1, 8)] + [[chr(row-i) + str(col+i), chr(row-i) + str(col-i)] for i in range(1, 8)] 
            for l in bp:
                for spot in l:
                    if spot in b.positions:
                        possiblepos.append(spot)

        if piece.name == 'Q':
            bp = [[chr(row+i) + str(col+i), chr(row+i) + str(col-i)] for i in range(1, 8)] + [[chr(row-i) + str(col+i), chr(row-i) + str(col-i)] for i in range(1, 8)] 
            for l in bp:
                for spot in l:
                    if spot in b.positions:
                        possiblepos.append(spot)
            for l in range(65, 73):
                if chr(l) + str(col) == piece.position:
                    continue
                possiblepos.append(chr(l) + str(col))
            for t in range(8):
                if chr(row) + str(t) == piece.position:
                    continue
                possiblepos.append(chr(row) + str(t))

        if piece.name == 'K':
            kp = [chr(row-2) + str(col-1), chr(row-2) + str(col+1),
                chr(row-1) + str(col-2), chr(row-1) + str(col+2),
                chr(row+1) + str(col-2), chr(row+1) + str(col+2),
                chr(row+2) + str(col-1), chr(row+2) + str(col+1)]
            for spot in kp:
                if spot in b.positions:
                    possiblepos.append(spot)         

        pp = possiblepos
        for spot in pp:
            if spot not in b.positions:
                possiblepos.remove(spot)
                
        return possiblepos