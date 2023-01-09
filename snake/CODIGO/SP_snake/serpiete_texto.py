import os
import tkinter

import engine.colores_e_estilos as colores_e_estilos
import time



verde = colores_e_estilos.verde
rojo = colores_e_estilos.rojo
comidacol = colores_e_estilos.CreadorDeColor(99, 0, 0, False)
comidacol.generate_color()

class Snake:
    def __init__(self, w, h, schar, bgchar):
        self.w = w
        self.h = h
        self.children = 0
        self.schar = schar
        self.bgchar = bgchar
        self.foodcords=[]
        self.bufercords = []
        self.prevcords = []
        self.nowcords = [0, 0]
        self.cordenadasy = []
    def draw_table(self):
        os.system("cls")
        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"{self.bgchar}")
            self.cordenadasy.append(cordenadasx)
        for i in self.cordenadasy:
            print("".join(i))

    def set_snake_cords(self, ycord, xcord):
        time.sleep(0.05)
        os.system("cls")
        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"{self.bgchar}")
            self.cordenadasy.append(cordenadasx)
        self.prevcords = self.nowcords
        self.cordenadasy[ycord][xcord] = f"{verde.color}{self.schar}{verde.clear}"
        self.nowcords = [ycord, xcord]
        for i in self.cordenadasy:
            print("".join(i))
        print(f"Puntos:{self.children}")
    def snake_move(self, movey, movex):
        time.sleep(0.05)
        os.system("cls")

        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"{self.bgchar}")
            self.cordenadasy.append(cordenadasx)
        self.prevcords = self.nowcords
        self.set_food()
        if self.children > 0:
            for i in self.bufercords:
                self.cordenadasy[i[0]][i[1]] = f"{verde.color}{self.schar}{verde.clear}"
        self.cordenadasy[self.nowcords[0]][self.nowcords[1]] = f"{rojo.color}{self.schar}{rojo.clear}"

        if len(self.bufercords) > self.children:
            while len(self.bufercords) > self.children:
                self.bufercords.pop(0)
            self.bufercords.append([self.nowcords[0], self.nowcords[1]])
        else:
            self.bufercords.append([self.nowcords[0], self.nowcords[1]])
        
        self.nowcords = [self.nowcords[0] + movey, self.nowcords[1] + movex]
        for i in self.cordenadasy:
            print("".join(i))
        print(f"Puntos:{self.children}")
    def set_food(self):
        for i in self.foodcords:
            self.cordenadasy[i[0]][i[1]] = f"{comidacol.color}{self.schar}{comidacol.clear}"






serpiente=Snake(50,50,"r","b")


print(serpiente.__dict__)