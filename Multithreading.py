import threading
import time
import random
from queue import Queue


menu = {
    "Pizza": 5,         #5 segundos para preparar una pizza de peperoni
    "Hamburguesa": 3,   #3 segundos para preparar una hamburguesa con todo
    "Ensalada": 2,      #2 segundos para preparar una ensalada Cesar
    "Sushi": 6,         #6 segundos para preparar sushi
    "Pasta": 4          #4 segundos para preparar pasta
}


pedido_queue = Queue()

class Mesa(threading.Thread):
    def __init__(self, id_mesa):
        super().__init__()
        self.id_mesa = id_mesa

    def run(self):
        pedido = random.choice(list(menu.keys()))
        print(f"Mesa {self.id_mesa}: Pedido de {pedido}")
        pedido_queue.put((self.id_mesa, pedido))

class Camarero(threading.Thread):
    def __init__(self, id_camarero):
        super().__init__()
        self.id_camarero = id_camarero

    def run(self):
        while True:
            try:
                id_mesa, pedido = pedido_queue.get(timeout=1)
            except:
                break

            tiempo_preparacion = menu[pedido]
            print(f"Camarero {self.id_camarero}: Preparando {pedido} para Mesa {id_mesa} ")
            time.sleep(tiempo_preparacion)  

            print(f"Camarero {self.id_camarero}: Entregando {pedido} a Mesa {id_mesa}")
            pedido_queue.task_done()

mesas = [Mesa(i) for i in range(1, 6)]
camareros = [Camarero(i) for i in range(1, 4)]

for mesa in mesas:
    mesa.start()
for camarero in camareros:
    camarero.start()
for mesa in mesas:
    mesa.join()


pedido_queue.join()
print("Todos los pedidos han sido entregados.")
