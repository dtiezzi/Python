
class Controler:

    def __init__(self):
        pass

    def posupdate(startpos, finalpos, p):
        startrow = ord(startpos[0]) - 65
        startcol = int(startpos[1])
        endrow = ord(finalpos[0]) - 65
        endcol = int(finalpos[1])
        p.position[endrow][endcol] = p.position[startrow][startcol]
        p.position[startrow][startcol] = ' -'

        return p

    def ckblock(p, finalplace, instance, turn):
        if self.turn == 1:
            t = 0
        else:
            t = 1
        if self.p[0] != 'k' or self.p[0] != 'p':
            ownpiecepos = []
            pass

    def ckoverlap(finalplace, instance, turn):
        if turn == 1:
                t = 0
        else:
                t = 1
        for k in instance[t]:
                if finalplace == instance[turn-1][k].position:
                        return False
        return True

    def ckovertake(finalplace, instance, turn):
        if turn == 1:
            t = turn
        else:
            t = 0
        for k in instance[t]:
            if finalplace == instance[t][k].position:
                return True, k, t
        k = None
        t = None
        return False, k, t

    def ckpawn(p, startpos, finalpos, turn, instance):
    
        if turn == 1:
            pl = []
            povtake = [chr(ord(startpos[0]) + 1) + str(int(startpos[1]) - 1), chr(ord(startpos[0]) + 1) + str(int(startpos[1]) + 1)]
            frontpos = chr(ord(startpos[0]) + 1) + startpos[1]
            for k in instance[1]:
                if instance[1][k].position in frontpos:
                    instance[0][p].moves.remove(frontpos)

        else:
            pl = []
            povtake = [chr(ord(startpos[0]) - 1) + str(int(startpos[1]) - 1), chr(ord(startpos[0]) - 1) + str(int(startpos[1]) + 1)]
            frontpos = chr(ord(startpos[0]) - 1) + startpos[1]
            for k in instance[0]:
                if instance[0][k].position in frontpos:
                    instance[1][p].moves.remove(frontpos)

    def ckplt(startpos, instance, turn):
    
        if turn == 1:
            for k in instance[0]:
                if startpos in instance[0][k].position:
                    return True
        elif turn == 2:
            for k in instance[1]:
                if startpos in instance[1][k].position:
                    return True
        else:
            return False

    def ckwin(instance):
        if 'kk1' not in instance[0]:
            return 2
        else:
            return 1

    def ckcheck(instance, turn):
        if turn == 1:
            t = 0
            op = 1
        else:
            t = 1
            op = 0
        if 'kk1' in instance[0] and 'kk1' in instance[1]:
            kingpos = instance[op]['kk1'].position
            for k in instance[t]:
                if kingpos in instance[t][k].moves:
                    return True

    def st():
        try:
            input("Press ENTER to continue")
        except SyntaxError:
            pass