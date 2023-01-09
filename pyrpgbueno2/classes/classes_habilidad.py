import os
import random
import json

habilidades_classes = []
lista_habilidades_json = []
# TODO:quitar logs
print("final")
os.system("dir")
os.chdir("./pyrpgbueno2/data/datagame/passive")
for i in os.listdir(os.getcwd()):
    lista_habilidades_json.append(i)

print(lista_habilidades_json)


class Habilidades:
    def __init__(self, a):
        self.nombre = a["nombre"]
        self.config = a["config"]
        self.estados = a["estados"]
        self.aciones = a["acion"]
        self.ataca = []

    def ataca(self):
        for a in range(self.config["ataque"]["probabilidad"]):
            self.ataca.append(True)
        for a in range(100 - self.config["ataque"]["probabilidad"]):
            self.ataca.append(False)
        return random.choice(self.ataca)

    def acion(self):
        match self.aciones:
            case "Paraliza":
                return "esta habilidad paraliza"
            case "Envenena":
                return "esta habilidad envenena"
            case "Cavia objecto":
                return "esto canvia los items"
            case "Roba objecto":
                return "esto roba un item"
            case "Canvia habilidad":
                return "esto canvia la habilidad"
            case "Roba habilidad":
                return "esto roba una habilidad"
            case _:
                print(f"[FATAL] Error en la lectura de Json de habilidades: {self.nombre}")
                print(f"No se cargara la siguiente abilidad: {self.nombre}")
                return "0"


parsed_hab = []

for i in os.listdir(f"{os.getcwd()}"):
    with open(f"{i}", "r", encoding="utf-8") as enem:
        habilidades_dic = json.loads(enem.read())
    habilidad_class = Habilidades(habilidades_dic)
    parsed_hab.append(habilidad_class)
os.chdir("../../..")
print("directorio final del modulo de las habilidades \n")
print(os.getcwd())
