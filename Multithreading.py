import threading
import time
import random
from queue import Queue

# Opciones de comida y tiempos de preparación
menu = {
    "Pizza": 5,         # 5 segundos para preparar una pizza
    "Hamburguesa": 3,   # 3 segundos para preparar una hamburguesa
    "Ensalada": 2,      # 2 segundos para preparar una ensalada
    "Sushi": 6,         # 6 segundos para preparar sushi
    "Pasta": 4          # 4 segundos para preparar pasta
}

# Cola de pedidos
pedido_queue = Queue()

# Simulación de las mesas (clientes)
class Mesa(threading.Thread):
    def __init__(self, id_mesa):
        super().__init__()
        self.id_mesa = id_mesa

    def run(self):
        # Escoger un pedido al azar del menú
        pedido = random.choice(list(menu.keys()))
        print(f"Mesa {self.id_mesa}: Pedido de {pedido}")
        pedido_queue.put((self.id_mesa, pedido))

# Simulación de los camareros
class Camarero(threading.Thread):
    def __init__(self, id_camarero):
        super().__init__()
        self.id_camarero = id_camarero

    def run(self):
        while True:
            try:
                # Tomar un pedido de la cola
                id_mesa, pedido = pedido_queue.get(timeout=1)
            except:
                # Salir del bucle si no hay más pedidos en la cola
                break

            # Preparar el pedido con el tiempo específico
            tiempo_preparacion = menu[pedido]
            print(f"Camarero {self.id_camarero}: Preparando {pedido} para Mesa {id_mesa} ")
            time.sleep(tiempo_preparacion)  # Simula el tiempo de preparación

            # Entregar el pedido
            print(f"Camarero {self.id_camarero}: Entregando {pedido} a Mesa {id_mesa}")
            pedido_queue.task_done()

# Crear hilos de mesas y camareros
mesas = [Mesa(i) for i in range(1, 6)]
camareros = [Camarero(i) for i in range(1, 4)]

# Iniciar los hilos de las mesas
for mesa in mesas:
    mesa.start()

# Iniciar los hilos de los camareros
for camarero in camareros:
    camarero.start()

# Esperar a que todas las mesas hayan realizado su pedido
for mesa in mesas:
    mesa.join()

# Esperar a que todos los pedidos sean atendidos
pedido_queue.join()
print("Todos los pedidos han sido entregados.")
