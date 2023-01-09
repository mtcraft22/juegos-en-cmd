import classes.classes_entidades as entidad
import classes.classes_ecenario as escenarios
import classes.classes_objetos as items
import engine.pantalla as pantalla
# cargamos los archivos .json coresponientes y procedemos a la declaración
import json
import os
Gameobjs = {}
enemigos_classes = []
lista_enemigos_json = []
os.chdir("./data/datagame/enemies")
for i in os.listdir(os.getcwd()):
    lista_enemigos_json.append(i)

print(f"enemigos: {lista_enemigos_json}")

for i in os.listdir(f"{os.getcwd()}"):
    with open(f"{i}", "r") as enem:
        enemigos_dic = json.loads(enem.read())
    enemigo_class = entidad.Enemigos(enemigos_dic)
    enemigos_classes.append(enemigo_class)
for i in range(len(enemigos_classes)):
    print(enemigos_classes[i].nombre)
    print(enemigos_classes[i].ataque)
    print(enemigos_classes[i].defensa)
lista_enemigos_completa = enemigos_classes
os.chdir("./..")
# declaramos las entidades que combaten

J = entidad.Jugador(5, "Juan Carlos", 2, 1, 20)

# declaramos los bosses
boses_classes = []
lista_boses_json = []

os.chdir("./boses")
for i in os.listdir(os.getcwd()):
    lista_boses_json.append(i)

print(lista_boses_json)

for i in os.listdir(f"{os.getcwd()}"):
    with open(f"{i}", "r") as enem:
        boses_dic = json.loads(enem.read())
    enemigo_class = entidad.Boss(boses_dic)
    boses_classes.append(enemigo_class)
for i in range(len(boses_classes)):
    print(boses_classes[i].habilidad)

os.chdir("./..")

# declaramos las instancias de los objectos

poción = items.Poción(6, 10, "Poción")
poción_mediana = items.Poción(12, 20, "Poción_mediana")
escudo = items.Escudo(5, 55, "Te añade escudo en el combate")

lista_enemigos_completa = entidad.lista_enemigos

# declaramos los escenarios
Hub = escenarios.Escenarios(nombre="Hub", aciones=["Tienda", "Combate", "Salir", "Guardar"])
com = escenarios.Combate(nombre="combate", aciones=["atacar", "defender", "objecto", "habilidad"])
tienda = escenarios.Tienda(items=items.lista_items, nombre="tienda", aciones=["comprar", "vender", "robar", "ir hub"])
final = escenarios.Combate(nombre="final", aciones=[])
mochila_es = escenarios.Tienda(items=J.mochila, nombre="mochila", aciones=[])
import classes.classes_habilidad
tienda_habilides=escenarios.Tienda(items=classes.classes_habilidad.habilidades_classes,nombre="Habilidades",aciones=["adquidir", "Robar", "Desadquidir"])
