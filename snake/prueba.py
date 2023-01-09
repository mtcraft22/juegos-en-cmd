import CODIGO.minigames.snake.serpiente_mov as snake
import threading,time

run=True
def timer():
    time.sleep(5)
    run=False
juego=threading.Thread(target=timer,args=[])
juego.start()
snake.game_snake(run)

print("se acabo el tiempo")

