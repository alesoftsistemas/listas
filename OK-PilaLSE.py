# Estructura de Datos y Algoritmos
# Facultad de Ciencias Exactas y Naturales
# Universidad Nacional de Catamarca
# Título: Pilas en una Lista Simple Encadenada
# Descripción: 1. Declarar una estructura de PILA como Lista Simple Encadenada que permita:
#              2. Almacenar las claves {A,B,C,D}
#              3. Eliminar 1 elemento (LIFO)  

class Nodo():

  def __init__(self, dato, siguiente):
    self.dato = dato
    self.siguiente = siguiente

print("PILA en Lista Simple Encadenada \n")
pila = []  # Iniciamos la pila vacia
print("Pila =", pila, "\n")

print("Ingreso de las claves")
print("Ingresa A")
pila.append("A")
print("Pila =", pila, "\n")

print("Ingresa B")
pila.append("B")
print("Pila =", pila, "\n")

print("Ingresa C")
pila.append("C")
print("Pila =", pila, "\n")

print("Ingresa D")
pila.append("D")
print("Pila =", pila, "\n")

print("Elimina 1 elemento")
pila.pop()
print("Pila =",pila, "\n")