import os
import pickle
import declaaraciones
import otros.indicar_acion as indicar_acion




class Saves_managment:
    def __init__(self):
        os.system("dir")
        os.chdir("./data/saves/")
        self.lista_ficheros = []
        for i in os.listdir():
            self.lista_ficheros.append(i)

    @staticmethod
    def load_save_file(self):
        if len(self.lista_ficheros) != 0:
            declaaraciones.os.chdir("./../../data/saves")
            Cargado = open(self.selecionpartida(), "rb")
            Jugador_info = pickle.load(Cargado)
            # print(Jugador_info[0].nombre,Jugador_info[0].mochila, Jugador_info[1].tangaciones)
            declaaraciones.J.dinero = Jugador_info[0].dinero
            declaaraciones.J.nombre = Jugador_info[0].nombre
            declaaraciones.J.mochila = Jugador_info[0].mochila
            declaaraciones.tienda.tangaciones = Jugador_info[1].tangaciones
            declaaraciones.os.chdir("./../../..")
        else:
            print("No se cargo nigun fichero")

    @staticmethod
    def create_save(self, nombre):
        open(f"{nombre}.prpg", "x")
        self.lista_ficheros.clear()
        for i in os.listdir():
            self.lista_ficheros.append(i)

    @staticmethod
    def selecionpartida(self):
        id = 0
        for j in self.lista_ficheros:
            id += 1
            print(f"{id}. {j}")
        fichero = indicar_acion.preguntar_acion(self.lista_ficheros, "Selecione el fichero a cargar enter para continuar: ")
        return self.lista_ficheros[fichero]


saves_managment = Saves_managment()