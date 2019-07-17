from classes.pawn import Pawn
from classes.hook import Hook
from classes.knight import Knight
from classes.bishop import Bishop
from classes.king import King
from classes.queen import Queen

class Instances:

    def __init__(self):
        pass

    def instanceup(turn, piecename, finalpos, instance):
        t = turn - 1
        instance[t][piecename].position = finalpos
        instance[t][piecename].move(instance[t][piecename])

        return instance

    def instance():
        hp = 0
        kp = 1
        bp = 2
        player1 = {}
        for i in range(8):
            p = Pawn()
            p.player = '1'
            p.id = 'p' + str(i)
            p.position = 'B' + str(i)
            p.move(p)
            player1["p{0}".format(i)] = p
        
        for i in range(2):
            h = Hook()
            h.player = '1'
            h.id = 'h' + str(i)
            h.position = 'A' + str(i+hp)
            hp+=6
            h.move(h)
            player1["h{0}".format(i)] = h

            b = Bishop()
            b.player = '1'
            b.id = 'b' + str(i)
            b.position = 'A' + str(i+bp)
            bp+=2
            b.move(b)
            player1["b{0}".format(i)] = b

            k = Knight()
            k.player = '1'
            k.id = 'k' + str(i)
            k.position = 'A' + str(i+kp)
            kp+=4
            k.move(k)
            player1["k{0}".format(i)] = k

        kk = King()
        kk.player = '1'
        kk.id = 'kk1'
        kk.position = 'A4'
        kk.move(kk)
        player1["kk1"] = kk
        
        q = Queen()
        q.player = '1'
        q.id = 'q1'
        q.position = 'A3'
        q.move(q)
        player1["q1"] = q

        hp = 0
        kp = 1
        bp = 2
        player2 = {}
        for i in range(8):
            p = Pawn()
            p.player = '2'
            p.id = 'p' + str(i)
            p.position = 'G' + str(i)
            p.move(p)
            player2["p{0}".format(i)] = p

        for i in range(2):
            h = Hook()
            h.player = '2'
            h.id = 'h' + str(i)
            h.position = 'H' + str(i+hp)
            hp+=6
            h.move(h)
            player2["h{0}".format(i)] = h

            b = Bishop()
            b.player = '2'
            b.id = 'b' + str(i)
            b.position = 'H' + str(i+bp)
            bp+=2
            b.move(b)
            player2["b{0}".format(i)] = b

            k = Knight()
            k.player = '2'
            k.id = 'k' + str(i)
            k.position = 'H' + str(i+kp)
            kp+=4
            k.move(k)
            player2["k{0}".format(i)] = k

        kk = King()
        kk.player = '2'
        kk.id = 'kk1'
        kk.position = 'H4'
        kk.move(kk)
        player2["kk1"] = kk
        
        q = Queen()
        q.player = '2'
        q.id = 'q1'
        q.position = 'H3'
        q.move(q)
        player2["q1"] = q

        return player1, player2