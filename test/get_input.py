import readchar, os, time

import engine.table as table

class Shoter (table.table):
    def __init__(self, h, w):
        super().__init__(h, w)
        self.shooting=False
        self.shootcords=[self.nowcords[0]-1,self.nowcords[1]]
        

shoter = Shoter(49,49)
shoter.set_player_cords(1,1)
while True:
    shoter.draw()
    k= readchar.readchar()
    if k == "w":
        shoter.player_move(-1,0)
    if k == "s":
        shoter.player_move(1,0)
    if k == "d":
        shoter.player_move(0,1)
    if k == "a":
        shoter.player_move(0,-1)
    if k== readchar.key.SPACE:
        shoter.shooting=True
        shoter.player_move(0,0)
    print(shoter.nowcords)
      