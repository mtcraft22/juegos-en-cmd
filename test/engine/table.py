import os
import engine.colores_e_estilos as d

class table:
    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.nowcords=[0,0]
        self.schar="█"
        self.cordenadasy=[]
        self.bgchar="█"
    def draw(self):
        for i in self.cordenadasy:
            print("".join(i))
    def draw_table(self):
        os.system("cls")
        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"{self.bgchar}")
            self.cordenadasy.append(cordenadasx)
        
    def set_player_cords(self, ycord, xcord):
        os.system("cls")
        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"{self.bgchar}")
            self.cordenadasy.append(cordenadasx)
        self.prevcords = self.nowcords
        self.cordenadasy[ycord][xcord] = f"{d.verde.color}{self.schar}{d.verde.clear}"
        self.nowcords = [ycord, xcord]
        
        
    def player_move(self, movey, movex):
        os.system("cls")
        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"{self.bgchar}")
            self.cordenadasy.append(cordenadasx)
        self.prevcords = self.nowcords
        self.cordenadasy[self.nowcords[0]][self.nowcords[1]] = f"{d.rojo.color}{self.schar}{d.rojo.clear}"
        self.nowcords = [self.nowcords[0] + movey, self.nowcords[1] + movex]
        
        