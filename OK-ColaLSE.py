# Estructura de Datos y Algoritmos
# Facultad de Ciencias Exactas y Naturales
# Universidad Nacional de Catamarca
# Título: Pilas en una Lista Simple Encadenada
# Descripción: 1. Declarar una estructura de COLA como Lista Simple Encadenada que permita:
#              2. Almacenar las claves {A,B,C,D}
#              3. Eliminar 1 elemento (LIFO)  

class Nodo():

  def __init__(self, dato, siguiente):
    self.dato = dato
    self.siguiente = siguiente

print("COLA en Lista Simple Encadenada \n")
cola = [] # Iniciamos la cola vacia
print("Cola =", cola, "\n")

print("Ingreso de las claves")
print("Ingresa A")
cola.append("A")
print("Cola =", cola, "\n")

print("Ingresa B")
cola.append("B")
print("Cola =", cola, "\n")

print("Ingresa C")
cola.append("C")
print("Cola =", cola, "\n")

print("Ingresa D")
cola.append("D")
print("Cola =", cola, "\n")

print("Eliminar clave")
del cola[0]
print("Cola =", cola, "\n")
