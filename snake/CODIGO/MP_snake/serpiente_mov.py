import time
import engine.contadorguapo as contadorguapo
import serpiete_texto
import cliente_net
import win32api
import random
import pickle
HEADSIZE=10
snake = serpiete_texto.MultiplayerSnake(50, 50, "█", "█")
net=cliente_net.Network()
net.get_id()
print(net.id)
snake.children = 0
dt = bytes(f"{len(pickle.dumps((net.id,snake))):<{HEADSIZE}}","utf-8")+pickle.dumps((net.id,snake))
def app():
    for i in range(random.randint(5,14)):
        snake.foodcords.append([random.randint(2, snake.h - 2), random.randint(2, snake.w - 2)])
    while True:
        snakes=net.send(dt)
        snake.draw_table()
        if win32api.GetKeyState(0x44) < 0:
            while True:
                # time.sleep(0.05)
                snake.snake_move(0, 1)
                contadorguapo.set_tabla(snake.children)
                if snake.nowcords in snake.foodcords:
                    snake.foodcords.remove(snake.nowcords)
                    snake.children += 1
                    snake.foodcords.append([random.randint(2, snake.h - 2), random.randint(2, snake.w - 2)])
                if snake.nowcords in snake.bufercords[:-1]:
                    snake.snake_move(0, 1)
                    print(snake.bufercords)
                    print(snake.nowcords)
                    raise ValueError("colision con serpiente")
                if win32api.GetKeyState(0x44) < 0 or win32api.GetKeyState(0x57) < 0 or win32api.GetKeyState(
                        0x41) < 0 or win32api.GetKeyState(0x53) < 0 or win32api.GetKeyState(
                        0x51) < 0 or win32api.GetKeyState(0x45) < 0:
                    break
        elif win32api.GetKeyState(0x57) < 0:
            while True:
                # time.sleep(0.05)
                snake.snake_move(-1, 0)
                contadorguapo.set_tabla(snake.children)
                if snake.nowcords in snake.foodcords:
                    snake.foodcords.remove(snake.nowcords)
                    snake.children += 1
                    snake.foodcords.append([random.randint(2, snake.h - 2), random.randint(2, snake.w - 2)])
                if snake.nowcords in snake.bufercords[:-1]:
                    snake.snake_move(-1, 0)
                    print(snake.bufercords)
                    print(snake.nowcords)
                    raise ValueError("colision con serpiente")
                if win32api.GetKeyState(0x44) < 0 or win32api.GetKeyState(0x57) < 0 or win32api.GetKeyState(
                        0x41) < 0 or win32api.GetKeyState(0x53) < 0 or win32api.GetKeyState(
                        0x51) < 0 or win32api.GetKeyState(0x45) < 0:
                    break
        elif win32api.GetKeyState(0x41) < 0:
            while True:
                # time.sleep(0.05)
                snake.snake_move(0, -1)
                contadorguapo.set_tabla(snake.children)
                if snake.nowcords in snake.foodcords:
                    snake.foodcords.remove(snake.nowcords)
                    snake.children += 1
                    snake.foodcords.append([random.randint(2, snake.h - 2), random.randint(2, snake.w - 2)])
                if snake.nowcords in snake.bufercords[:-1]:
                    snake.snake_move(0, -1)
                    print(snake.bufercords)
                    print(snake.nowcords)
                    raise ValueError("colision con serpiente")
                if win32api.GetKeyState(0x44) < 0 or win32api.GetKeyState(0x57) < 0 or win32api.GetKeyState(
                        0x41) < 0 or win32api.GetKeyState(0x53) < 0 or win32api.GetKeyState(
                        0x51) < 0 or win32api.GetKeyState(0x45) < 0:
                    break
        elif win32api.GetKeyState(0x53) < 0:
            while True:
                # time.sleep(0.05)
                snake.snake_move(1, 0)
                contadorguapo.set_tabla(snake.children)
                if snake.nowcords in snake.foodcords:
                    snake.foodcords.remove(snake.nowcords)
                    snake.children += 1
                    snake.foodcords.append([random.randint(2, snake.h - 2), random.randint(2, snake.w - 2)])
                if snake.nowcords in snake.bufercords[:-1]:
                    snake.snake_move(1, 0)
                    print(snake.bufercords)
                    print(snake.nowcords)
                    raise ValueError("colision con serpiente")
                if win32api.GetKeyState(0x44) < 0 or win32api.GetKeyState(0x57) < 0 or win32api.GetKeyState(
                        0x41) < 0 or win32api.GetKeyState(0x53) < 0 or win32api.GetKeyState(
                        0x51) < 0 or win32api.GetKeyState(0x45) < 0:
                    break
        elif win32api.GetKeyState(0x51) < 0:
            snake.children -= 1
            print(snake.children)
            time.sleep(0.1)
        elif win32api.GetKeyState(0x45) < 0:
            snake.children += 1
            print(snake.children)
            time.sleep(0.1)
        elif win32api.GetKeyState(0x4A) < 0:
            print(snake.bufercords,snakes)
            time.sleep(0.1)

app()
