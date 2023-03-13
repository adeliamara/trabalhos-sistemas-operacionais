import threading
import time

def move_cart(name, speed):
    distance = 0
    while distance < 50:
        distance += speed
        track = "-" * distance + name
        print(track)
        time.sleep(0.3)

thread1 = threading.Thread(target=move_cart, args=("Carrinho 1", 3))
thread2 = threading.Thread(target=move_cart, args=("Carrinho 2", 5))

thread1.start()
thread2.start()


