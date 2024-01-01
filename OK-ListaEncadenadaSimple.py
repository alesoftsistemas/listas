# Estructura de Datos y Algoritmos
# Facultad de Ciencias Exactas y Naturales
# Universidad Nacional de Catamarca
# Título: Ejemplo de operaciones con Listas Simples Encadenadas 
# Descripción: 1. Declarar una estructura de Lista Simple Encadenada que permita:
#              2. Almacenar los elementos {A,B,C}  
#              3. Almacenar el elemento {D} por el FRONT 
#              4. Almacenar el elemento {X} en la posición [2]

# Creamos la clase node
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 

    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la lista
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)  
    
    # Método para agregar elementos en una posicion intermedia de la lista
    def add(self, position: int, element):
        if position == 0:
            self.head = node(data=element, nextNode=self._firstNode)
        else:
            currentNode = self.head
            for _ in range(0, position - 1):
                currentNode = currentNode.next
            currentNode.next = node(data=element, next=currentNode.next)

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para eliminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" → ")
            node = node.next

# Instancia de la clase
s = linked_list() 

# Verificamos de la Lista esta creada y vacía. 
print("1. Declarar una estructura de Lista Simple Encadenada")
print("Lista vacía: ", s.is_empty())
print(" \n")

# Agregamos las primeras claves por el END
s.add_at_end("A") 
s.add_at_end("B") 
s.add_at_end("C") 
print("2.Almacenar las claves {A,B,C}")
s.print_list() # Imprimimos la lista de nodos
print(" \n")

# Agregamos otra clave por el FRONT
s.add_at_front("D") 
print("3.Almacenar la clave {D} por el FRONT")
s.print_list() 
print("\n")

# Agregamos otra clave por una posición intermedia
s.add(2, "X") 
print("4. Almacenar la clave {X} en la posición [2]")
s.print_list() 
print()
print(" \n")

# Eliminamos una clave por una posición intermedia
s.delete_node("B")
print("5. Eliminar la clave {B}")
s.print_list() # Imprimimos la lista de nodos
print(" \n")