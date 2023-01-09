import math
import platform, os
import colores_e_estilos

class Pantalla:

    @staticmethod
    def draw_hp_bar(v_max, v_act, color_a=colores_e_estilos.verde, color_b=colores_e_estilos.amarillo,
                    color_c=colores_e_estilos.rojo, scale=1):
        print("[", end="")
        color = color_a.clear
        p = v_act / v_max
        if p <= 0.2:
            color = color_c.color
        elif 0.5 >= p > 0.2:
            color = color_b.color
        elif p > 0.5:
            color = color_a.color
        for i in range(max(math.ceil(v_act / scale), 0)):
            print(color + "█", end=color_a.clear)
        for i in range(max(math.floor((v_max - v_act) / scale), 0)):
            print(" ", end="")
        print("] ", end="")
        print(f"{v_act}/{v_max} PS\n")

    @staticmethod
    def draw_screen(iscombat, showitems, escenario, jugador, enemigo, comentarios):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        if iscombat:
            print("----------------------------------------------------------------")
            print(" ")
            print("Vida de "f"{jugador.nombre}", end="")
            Pantalla.draw_hp_bar(jugador.vida_max, jugador.vida_act)
            print("Magia de "f"{jugador.nombre}", end="")
            Pantalla.draw_hp_bar(jugador.mana_max, jugador.mana_act,
                                 color_a=colores_e_estilos.lila, color_b=colores_e_estilos.lila,
                                 color_c=colores_e_estilos.lila)
            print("")
            print(f"Vida de {enemigo.nombre}       ", end=" ")
            Pantalla.draw_hp_bar(enemigo.vida_max, enemigo.vida_act)
        if showitems:
            escenario.mostrar_items()
        print("----------------------------------------------------------------")
        if escenario.nombre != "Tienda" and escenario.nombre != "mochila":
            print(f" Piso: {escenario.piso}")
        
        print(f" Pasta: {jugador.dinero}")
        print("----------------------------------------------------------------")
        print(" Aciones: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
        print("----------------------------------------------------------------")
        print(f"Ultimo evento: {comentarios}")
        print("----------------------------------------------------------------")
