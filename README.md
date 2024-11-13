# Programa de Simulación de Restaurante
## Equipo
- Froylan Adair Villegas Castro
- Diego Juan Manuel Salvador Garcia Reyna
- Hector Alejandro Perez Cornejo
- Isay Montejano Quirino
- Cesar Mocivais Aguilar
- Daniel Rodriguez Burnes
- Maximiliano Lugo Zabala
- Aurelio Flores Nava


## Descripcion del programa
El programa simula un restaurante con 5 mesas y 3 camareros, cada mesa realiza un pedido al azar del menú y los camareros se encargan de preparar los distintos pedidos y entregarlos.

Para representar las mesas y los camareros se crearon clases que extienden la clase `Thread`; el menu se representa con un diccionario en el que se encuentran los platillos y el tiempo de preparacion de cada uno y la lista de ordenes se representó mediante una `Queue`.

Se crean 5 hilos de clase mesa y 3 hilos de clase mesero al ejecutar el programa.

Cada hilo clase mesa selecciona al azar un elemento del menú, y lo ingresa a la `Queue`.
 
Mientras tanto los hilos de mesero intentan extraer elementos de la Queue, los prepara (lo que se simula mediante un `time.sleep())` y los entrega. Los meseros dejan de preparar cuando al intentar sacar elementos se produce una excepción que indica que la `Queue` está vacia (que ya se prepararon todos los pedidos).

## Ejecución
Para ejecutar el programa hay que esribir en una terminal que se encuentre en el directorio

`python Multithreading.py` 
