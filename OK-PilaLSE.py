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

class ListaLigada:

  def __init__(self):
    self.cabeza = None
    self.tamano = 0

  def unir(self, dato):
    nodo = Nodo(dato, None)

    if self.cabeza == None:
      self.cabeza = nodo
    else:
      posicion_actual = self.cabeza

      while posicion_actual.siguiente:
        posicion_actual = posicion_actual.siguiente

      posicion_actual.siguiente = nodo

    self.tamano += 1


# Instancia de la clase
pila = []  

print("Ingreso de las claves")
print("Ingresa A")
pila.append("A")
print(pila, "\n")

print("Ingresa B")
pila.append("B")
print(pila, "\n")

print("Ingresa C")
pila.append("C")
print(pila, "\n")

print("Ingresa D")
pila.append("D")
print(pila, "\n")

print("Elimina 1 elemento")
pila.pop()
print(pila, "\n")