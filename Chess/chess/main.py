import time
from classes.createboard import Board as bd
from classes.startpostion import Position as ps
from functions.controlers import Controler
from functions.instances import Instances
from functions.player import Player
from functions.pieces import Pieces
from functions.printer import Printer

resp = 'y'
while (resp == 'y'):
    Printer.printxt('_images/chess.txt')
    print('[INFO] Loading CHESS...')
    time.sleep(2)
    b = bd()
    p = ps()
    it = Instances.instance()
    turn = 1
    Printer.printboard(p)
    while 'kk1' in it[0] and 'kk1' in it[1]:
        pp1, pp2 = Player.pieceposition(it)
        validswap = 'no'
        while validswap == 'no':
            opt = 'notvalid'
            while opt == 'notvalid':
                startpos, finalpos = Player.option(turn)
                if startpos in b.positions and finalpos in b.positions and Controler.ckplt(startpos, it, turn):
                        opt = 'valid'
                else:
                    print('[ERROR] Invalid position! Type again...')
            piecename = Pieces.swap(startpos, finalpos, pp1, pp2, turn)
            if piecename[0] == 'p':
                Controler.ckpawn(piecename, startpos, finalpos,turn, it)

            nonoverlap = Controler.ckoverlap(finalpos, it, turn)
            if finalpos in it[turn-1][piecename].moves and nonoverlap:
                if piecename[:-1] != 'k':
                    valresp = input("Payer {}! Is the movement from {} to {} valid (Y/N)?".format(Player.pnum(turn), startpos, finalpos)).lower()
                    if valresp == 'y':
                        validswap = 'yes'
                else:
                    validswap = 'yes'
            else:
                Printer.printboard(p)
                if not nonoverlap:
                    print('[ERROR] Not valid movent (from {} t0 {})..'.format(startpos, finalpos))
                    print('Overlap pieces! Try again...')
                else:
                    print('[ERROR] Not valid movent (from {} t0 {})..'.format(startpos, finalpos))
                    print('Possible positions are: {}. Try again...'.format(it[turn-1][piecename].moves))
        p = Controler.posupdate(startpos, finalpos, p)
        
        overtake, k , t= Controler.ckovertake(finalpos, it, turn)
        
        if overtake:
            it = Pieces.rmpiece(k, it, t)
        it = Instances.instanceup(turn, piecename, finalpos, it)
        
        if Controler.ckcheck(it, turn):
            print("Player {}! The KING is in CHECK!".format(Player.pnum(turn)))
            Controler.st()

        Printer.printboard(p)
        turn = Player.switch(turn)

    print("CONGRATULATIONS PLAYER {}.\n YOU ARE THE WINNER!".format(Controler.ckwin(it)))
    Controler.st()
    resp = input('New game (Y/N)?').lower()

if __name__ == "__main__":
    pass