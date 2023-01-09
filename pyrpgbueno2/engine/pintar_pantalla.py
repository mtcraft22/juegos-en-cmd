import os
import platform
# El soporte de este modulo se finalizará en el momento de que el modulo pantalla.py se implementado
import pintar_vara_vida as pintar_vara_vida  # importación de módulo para mostrar la vara de vida dinamica
import colores_e_estilos as colores_e_estilos


def actualizar_pantalla(escenario, enemigo, jugador, comentario):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    if escenario.nombre == "combate":
        print(" ")
        print("Vida de ", end="")
        pintar_vara_vida.draw_hp_bar(jugador.vida_max, jugador.vida_act, jugador.nombre,colores_e_estilos.verde,
                                     colores_e_estilos.amarillo, colores_e_estilos.rojo)
        print("Magia de ", end="")
        pintar_vara_vida.draw_hp_bar(jugador.mana_max, jugador.mana_act, jugador.nombre, colores_e_estilos.lila,
                                     colores_e_estilos.lila, colores_e_estilos.lila)
        print("")
        print(f"                                                             ", end=" ")
        pintar_vara_vida.draw_hp_bar(enemigo.vida_max, enemigo.vida_act, enemigo.nombre, colores_e_estilos.verde,
                                     colores_e_estilos.amarillo, colores_e_estilos.rojo)
        print("----------------------------------------------------------------")
        print(f" Piso: {escenario.piso}")
        print(f" Pasta: {jugador.dinero}")
        print("----------------------------------------------------------------")
        print(" Aciones: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
        print("----------------------------------------------------------------")
        print(f"Ultimo evento: {comentario}")
        print("----------------------------------------------------------------")
    elif escenario.nombre == "tienda":
        print("----------------------------------------------------------------")
        escenario.mostrar_items()
        print("----------------------------------------------------------------")
        print(f"Apu: {comentario}")
        print("----------------------------------------------------------------")
        print(f"Dinero: {jugador.dinero}")
        print(f"delitos:{escenario.tangaciones}")
        print("----------------------------------------------------------------")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
    elif escenario.nombre == "mochila":
        print("----------------------------------------------------------------")
        escenario.mostrar_items()
        print("----------------------------------------------------------------")
        print(f"{comentario}")
        print("----------------------------------------------------------------")
        
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
    elif escenario.nombre == "Habilidades":
        print("----------------------------------------------------------------")
        escenario.mostrar_habilidades()
        print("----------------------------------------------------------------")
        print(f"{comentario}")
        print("----------------------------------------------------------------")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
    elif escenario.nombre == "Hub":
        print("seleccione destino: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
    elif escenario.nombre == "final":
        print(" ")
        print(" ", end="")
        pintar_vara_vida.draw_hp_bar(jugador.vida_max, jugador.vida_act, jugador.nombre,colores_e_estilos.verde,
                                     colores_e_estilos.amarillo, colores_e_estilos.rojo)
        print("Magia de ", end="")
        pintar_vara_vida.draw_hp_bar(jugador.mana_max, jugador.mana_act, jugador.nombre,colores_e_estilos.lila,
                                     colores_e_estilos.lila, colores_e_estilos.lila)
        print("")
        print(f"                                                             ", end=" ")
        pintar_vara_vida.draw_hp_bar(enemigo.vida_max, enemigo.vida_act, enemigo.nombre, colores_e_estilos.verde,
                                     colores_e_estilos.amarillo, colores_e_estilos.rojo)

        print("----------------------------------------------------------------")
        print(f" Piso: {escenario.piso}")
        print("----------------------------------------------------------------")
        print(" Aciones: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
        print("----------------------------------------------------------------")
        print(f"Ultimo evento: {comentario}")
        print("----------------------------------------------------------------")




