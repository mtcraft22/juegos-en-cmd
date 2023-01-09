
import engine.contadorguapo as contadorguapo
import engine.colores_e_estilos as colores_e_estilos
import os
class table:
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def draw_table(self):
        os.system("cls")
        self.cordenadasy = []
        for y in range(self.h):
            cordenadasx = []
            for x in range(self.w):
                cordenadasx.append(f"5")
            self.cordenadasy.append(cordenadasx)
        for i in self.cordenadasy:
            print("".join(i))

class alien:
    def __init__(self,**kwargs):
        self.color = kwargs["color"]
        self.vel = kwargs["vel"]
        self.sprite = kwargs["sprite"]
        self.sprite2 = kwargs["sprite2"]
class bunquer:
    pass
class player:
    pass

ufo=[
    ["","","","","",""]
    ["","","","","",""]
    ["","","","","",""]
    ["","","","","",""]
    
   
]

tabla=table(150,150)
tabla.draw_table()