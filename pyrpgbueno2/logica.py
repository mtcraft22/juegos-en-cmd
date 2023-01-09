import random
import time
import pickle
import saves_managment.Saves_managment
import saves_managment.declaaraciones as declaaraciones
import engine.pantalla as pantalla
import engine.pintar_pantalla as pintar_pantalla
import lista_enemigos_por_nivel
import otros.indicar_acion as indicar_acion
declaaraciones.os.system("dir")
productos = declaaraciones.items.lista_items
declaaraciones.os.system("color")

# Combatimos
def combate():
    #elegimos al enemigo y seteamos los productos de la tienda
    ene = random.choice(lista_enemigos_por_nivel.sacar_lista_nivel(declaaraciones.com.piso))
    declaaraciones.mochila_es.Items_ala_venta = declaaraciones.J.mochila
    #mientras los componentes del combate esten vivos, combatimos
    while declaaraciones.J.vida_act > 0 and ene.vida_act > 0:
        #pintamos la interfaz y el ecenario
        pantalla.Pantalla.draw_screen(True, False, declaaraciones.com, declaaraciones.J, ene,
                                      f" {declaaraciones.J.mochila}")
        #preguntamos por la acion del jugador
        acion = indicar_acion.preguntar_acion(declaaraciones.com.aciones)
        if acion == 0:
            declaaraciones.J.atacar(ene)
            pantalla.Pantalla.draw_screen(True, False, declaaraciones.com, declaaraciones.J, ene,
                                          f" Inflingistes {declaaraciones.J.ataque - ene.defensa} de daño ")
            time.sleep(0.5)
            ene.atacar(declaaraciones.J)

            pantalla.Pantalla.draw_screen(True, False, declaaraciones.com, declaaraciones.J, ene,
                                          f" Te hicieron {ene.ataque - declaaraciones.J.defensa} de daño ")
        elif acion == 2:

            pantalla.Pantalla.draw_screen(False, True, declaaraciones.mochila_es, declaaraciones.J, ene, "Mi mochila")
            item_us = indicar_acion.preguntar_acion(declaaraciones.mochila_es.aciones,
                                                    "Introduce ID de producto a usar o enter para salir ")
            if item_us==None:
                continue
            try:
                declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                declaaraciones.J.mochila.pop(item_us)
            except IndexError:
                pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,"Introduce un valor correcto:")
            except TypeError:
                pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,"Introduce un valor correcto:")
            while item_us > len(declaaraciones.J.mochila):
                
                pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,"Mi mochila")
                item_us = indicar_acion.preguntar_acion(declaaraciones.mochila_es.aciones,
                                                        "Introduce ID de producto a usar o enter para salir ")
                if type(item_us) != int:
                    break
                try:
                    declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                    pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                    declaaraciones.J.mochila.pop(item_us)
                except IndexError:
                    pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,"Introduce un valor correcto:")
                except TypeError:
                    pantalla.Pantalla.draw_screen(False,True,declaaraciones.mochila_es,declaaraciones.J,None,"Introduce un valor correcto:")
            continue
        elif acion == 3:
            pantalla.Pantalla.draw_screen(False,True,declaaraciones.habilidades,declaaraciones.J,None,"Mis habilidades")
            item_us = indicar_acion.preguntar_acion(declaaraciones.habilidades.aciones,
                                                    "Introduce ID de producto a usar o enter para salir ")
            if type(item_us) != int:
                continue
            try:
                declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                pantalla.Pantalla.draw_screen(False,True,declaaraciones.habilidades,declaaraciones.J,None, f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                declaaraciones.J.mochila.pop(item_us)
            except IndexError:
                pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades, None, declaaraciones.J,
                                                    "Introduce un valor correcto:")

            while item_us > len(declaaraciones.J.mochila):
                pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades, None, declaaraciones.J, "Mi mochila")
                item_us = indicar_acion.preguntar_acion(declaaraciones.habilidades.aciones,
                                                        "Introduce ID de producto a usar o enter para salir ")
                if type(item_us) != int:
                    break
                try:
                    declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                    pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades, None, declaaraciones.J,
                                                        f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                    declaaraciones.J.mochila.pop(item_us)
                except IndexError:
                    pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades, None, declaaraciones.J,
                                                        "Introduce un valor correcto:")
            continue
    pintar_pantalla.actualizar_pantalla(declaaraciones.final, ene, declaaraciones.J,
                                        f" final combate, llendo al hub ")

    if declaaraciones.J.vida_act <= 0:
        declaaraciones.J.vida_act = declaaraciones.J.vida_max / 2
        ene.vida_act = ene.vida_max
    elif ene.vida_act <= 0:
        pasta = random.randint(ene.min_coin, ene.max_coin)
        declaaraciones.J.dinero += pasta
        ene.vida_act = ene.vida_max
        pintar_pantalla.actualizar_pantalla(declaaraciones.final, ene, declaaraciones.J, f"Recivistes {pasta} coin/s ")
        time.sleep(0.5)

    selecionar()

# Tienda
def comprar():
    pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "Bienvenido al baludaque")
    acion = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones)
    if acion == 0:
        pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "¿Que desea comprar?")
        item = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones, "Introduce la id del item: ")
        if declaaraciones.J.dinero >= productos[item].coste:
            declaaraciones.J.mochila.append(productos[item])
            nombres = [productos[item].nombre]
            declaaraciones.J.dinero -= productos[item].coste
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J,
                                                f"compraste {productos[item].nombre}")
            if declaaraciones.tienda.tangaciones > 0:
                declaaraciones.tienda.tangaciones -= 1
                pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J,
                                                    f"Como has comprado te descuento un robo robos pendientes "
                                                    f"{declaaraciones.tienda.tangaciones}")
            print("Su mochila: ", nombres)
            input("sal")
            comprar()
        else:
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J,
                                                f"No tienes suficiente dinero ¿A lo mejor me puedes robar ?")
    #En caso que eliga robar un item 
    if acion == 2:
        item = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones, "Introduce la id del item: ")
        declaaraciones.J.mochila.append(productos[item])
        nombres = [productos[item].nombre]
        pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J,
                                            f"ahora incrementaré un 25% los precios por tonto, cuidado que lo pagaras")
        declaaraciones.tienda.tangaciones += 1
        # si la cantidad de robos esta entre 5 y 10 entoces solo le quitamos el dinero
        if 5 < declaaraciones.tienda.tangaciones <= 10:
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J,
                                                f"Me daras toda la pasta por cometer acciones poco licitas")
            declaaraciones.J.dinero = 0
        # si los robos son superiodes a 10 entoces le quitamos todos los items
        elif declaaraciones.tienda.tangaciones >= 10:
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J,
                                                f"Me daras toda la mochila por cometer acciones poco licitas")
            declaaraciones.J.mochila.clear()
        #incremento el coste de los items en caso de robo en 25%
        for i in declaaraciones.tienda.Items_ala_venta:
            i.coste *= 1.25
        print("Su mochila: ", nombres)
        input("sal")
        comprar()

    if acion == 3:
        selecionar()

#HUB
def selecionar():
    dataobj = [declaaraciones.J, declaaraciones.tienda]
    pintar_pantalla.actualizar_pantalla(declaaraciones.Hub, None, None, None)
    acion = indicar_acion.preguntar_acion(declaaraciones.Hub.aciones)
    if acion == 0:
        comprar()
    if acion == 1:
        combate()
    if acion == 3:
        declaaraciones.os.system("dir")
        declaaraciones.os.chdir("./pyrpgbueno2/data/saves")
        iden = 0
        for i in saves_managment.lista_ficheros:
            iden += 1
            print(f"{iden}. {i}")

        try:
            fichero = int(input("Indique numero del archivo a sobreescribir o Enter para archivo nuevo "))
        except ValueError:
            fichero = input("Indique nombre de nuevo archivo ")
        if type(fichero) == int:

            fichero_sel = saves_managment.lista_ficheros[fichero - 1]
            data = open(f"{fichero_sel}", "wb")
            pickle.dump(dataobj, data)

        else:
            # data = open(f"{fichero}.prpg", "x")
            with open(f"{fichero}.prpg", "wb") as data:
                pickle.dump(dataobj, data)

        declaaraciones.os.chdir("./../../..")


combate()
