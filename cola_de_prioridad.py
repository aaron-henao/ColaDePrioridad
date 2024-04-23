class Paciente:

    def __init__(self, nombre:str, edad:int, descripcion: str, prioridad:int):

        self.nombre = nombre
        self.edad = edad
        self.descripcion = descripcion
        self.prioridad = prioridad

class DNode:

    def __init__(self, value: Paciente):
        self.value = value 
        self.next = None
        self.prev = None

class DobleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def empty(self):
        return self.head == None
    
    def append(self, e):

        new_node = DNode(e)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        return
    
    def preppend(self, e):

        if self.empty():
            self.head = self.tail = DNode(e)
        else:
            aux = DNode(e)
            aux.next = self.head
            self.head.prev = aux
            self.head = aux
        self.size +=1      

    
    def other_position(self, node:DNode):
        aux = node.prev
        aux.next = None
        node.prev = None
        aux_2 = self.tail.prev
        aux_2.next = None
        self.tail.prev = None
        aux.next = self.tail
        self.tail.prev = aux
        self.tail.next = node
        node.prev = self.tail
        self.tail = aux_2

    def delete_head(self):
        aux = self.head.next
        aux.prev = None
        self.head.next = None
        self.head = aux 
        self.size -= 1
    
    def delete(self, index):
        node = self.head
            
        for i in range(self.size):
            if node is not None:
                if i == index:
                    anterior = node.prev
                    anterior.next = None
                    node.prev = None
                    if node != self.tail:
                        siguiente = node.next
                        node.next = None
                        siguiente.prev = None
                        anterior.next = siguiente
                        siguiente.prev = anterior
                    self.tail = anterior

                    return node.value    
            node = node.next
        self.size -=1 

    def traverse(self):
        node = self.head
        while node is not None:
            print("Nombre:", node.value.nombre)
            print("Edad:", node.value.edad)
            print("Descripción:", node.value.descripcion)
            print("Prioridad:", node.value.prioridad)
            print("Prev:", node.prev.value.nombre if node.prev else "None")
            print("Next:", node.next.value.nombre if node.next else "None")
            print("----")
            node = node.next

    def show_head_and_tail(self):
        if self.head is None:
            print("La lista está vacía.")
            return
        print("Head:")
        print("Nombre:", self.head.value.nombre)
        print("Edad:", self.head.value.edad)
        print("Descripción:", self.head.value.descripcion)
        print("Prioridad:", self.head.value.prioridad)
        print("----")
        
        if self.tail is None:
            print("La lista está vacía.")
            return
        print("Tail:")
        print("Nombre:", self.tail.value.nombre)
        print("Edad:", self.tail.value.edad)
        print("Descripción:", self.tail.value.descripcion)
        print("Prioridad:", self.tail.value.prioridad)
        print("----")
        
    def traverse_from_tail(self):
        node = self.tail
        while (node is not None):
            print("Nombre:", node.value.nombre)
            print("Edad:", node.value.edad)
            print("Descripción:", node.value.descripcion)
            print("Prioridad:", node.value.prioridad)
            print("----")
            node = node.prev
    
    def show_head(self):
        node = self.head
        print("Nombre:", node.value.nombre)
        print("Edad:", node.value.edad)
        print("Descripción:", node.value.descripcion)
        print("Prioridad:", node.value.prioridad)
        print("----")
    
class cola_de_prioridad:
    def __init__(self, lista_pacientes: DobleLinkedList):
        self.lista_pacientes = lista_pacientes

    def buscar_siguiente_prioridad(self):
        paciente = self.lista_pacientes.head
        self.count = 0

        for _ in range(self.lista_pacientes.size):
            if paciente.value.prioridad == 1:
                self.count +=1
                paciente = paciente.next
        return True
        
    def agregar_paciente(self, paciente: Paciente):
        prioridad_paciente = paciente.prioridad

        if prioridad_paciente == 1 and self.lista_pacientes.size>0:

            if self.prioridad_first != 1:
                self.lista_pacientes.preppend(paciente)
            
            else:

                if self.buscar_siguiente_prioridad():
                    self.lista_pacientes.append(paciente)
                    node = self.lista_pacientes.head

                    for _ in range(self.count):

                        if node.value.prioridad == 1:
                            node = node.next

                    if node.value.prioridad != 1:

                        self.lista_pacientes.other_position(node)            
        else:
            self.lista_pacientes.append(paciente)
        self.first = self.lista_pacientes.head
        self.prioridad_first = self.first.value.prioridad

    def atender_paciente(self):
        self.lista_pacientes.show_head()
        self.lista_pacientes.delete_head()
    
    def mostrar_cola(self):
        self.lista_pacientes.traverse()

    def buscar_paciente(self, nombre):
        paciente: Paciente
        paciente = self.lista_pacientes.head

        for _ in range(self.lista_pacientes.size):
            if paciente.value.nombre == nombre:
                return paciente
            paciente = paciente.next

    def buscar_posicion_paciente(self, nombre):
        paciente = self.lista_pacientes.head 

        for i in range(self.lista_pacientes.size):
            if paciente.value.nombre == nombre:
                return i
            paciente = paciente.next
        return False
    
    def actualizar_prioridad(self, nombre, nueva_prioridad):
        paciente_nodo = self.buscar_paciente(nombre)
    
        if paciente_nodo is not None:
            paciente = paciente_nodo.value 
            if nueva_prioridad != 1:
                paciente.prioridad = nueva_prioridad
            else:
                paciente.prioridad = nueva_prioridad
                index = self.buscar_posicion_paciente(nombre)
                paciente = self.lista_pacientes.delete(index)
                self.agregar_paciente(paciente) 

# IMPLEMENTACION

ll = DobleLinkedList()
cola = cola_de_prioridad(ll)
Paciente_1 = Paciente("uno", 11, "x", 2)
Paciente_2 = Paciente("dos", 55, "x", 1)
Paciente_3 = Paciente("seis", 66, "x", 2)
Paciente_4 = Paciente("tres", 22, "x", 1)
Paciente_5 = Paciente("cuatro", 33, "x", 1)
Paciente_6 = Paciente("cinco", 44, "x", 1)
Paciente_7 = Paciente("siete", 77, "x", 2)
Paciente_8 = Paciente("ocho", 77, "x", 2)

cola.agregar_paciente(Paciente_1)
cola.agregar_paciente(Paciente_2)
cola.agregar_paciente(Paciente_3)
cola.agregar_paciente(Paciente_4)
cola.agregar_paciente(Paciente_5)
cola.agregar_paciente(Paciente_6)
cola.agregar_paciente(Paciente_7)
cola.agregar_paciente(Paciente_8)
cola.mostrar_cola()
print("*************")
cola.actualizar_prioridad("ocho", 1)
Paciente_9 = Paciente("nueve", 77, "x", 2)
cola.agregar_paciente(Paciente_9)
print("*************")
cola.mostrar_cola()
print("*************")
ll.show_head_and_tail()
print("*************")
paciente_10 = Paciente("diez", 77, "primero", 1)

ll.preppend(paciente_10)
cola.mostrar_cola()
print("*************")
ll.show_head_and_tail()
print("*************")
cola.atender_paciente()
print("*************")
cola.mostrar_cola()
print("*************")
ll.show_head_and_tail()