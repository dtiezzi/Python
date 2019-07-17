
class Player:

    def __init__(self):
        pass

    def pnum(turn):
        if turn == 1:
            return 2
        else:
            return 1

    def option(turn):
        print('Player' + str(turn))
        startpos = input('FROM: ').upper()
        finalpos = input('TO: ').upper()

        return startpos, finalpos

    def pieceposition(instance):
        poslistplayer1 = {}
        poslistplayer2 = {}
        for key in instance[0]:
            poslistplayer1[instance[0][key].position] = instance[0][key].id
        for key in instance[1]:
            poslistplayer2[instance[1][key].position] = instance[1][key].id
        
        return poslistplayer1, poslistplayer2

    def switch(turn):
        if turn == 1:
                turn+=1
        else:
            turn-=1
        return turn