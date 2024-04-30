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
        if index < 0 or index >= self.size:
            return None

        node = self.head
        if index == 0:
            self.head = node.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            for _ in range(index):
                node = node.next
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            if node == self.tail:
                self.tail = node.prev

        self.size -= 1
        return node.value
 

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
    
    def show_value(self, e):
        node = self.head

        for i in range(self.size):
            if i == e:
                print("Nombre:", node.value.nombre)
                print("Edad:", node.value.edad)
                print("Descripción:", node.value.descripcion)
                print("Prioridad:", node.value.prioridad)
                print("----")
            node = node.next

    
    
class cola_de_prioridad:
    def __init__(self, lista_pacientes: DobleLinkedList):
        self.lista_pacientes = lista_pacientes
        self.prioridad_1 = 0
        self.prioridad_2 = 0
        self.prioridad_3 = 0
 
    def agregar_paciente(self, paciente: Paciente):
        prioridad_paciente = paciente.prioridad
        
        if prioridad_paciente == 1 and self.lista_pacientes.size > 0:
            self.prioridad_1 += 1
            if self.prioridad_first != 1:
                self.lista_pacientes.preppend(paciente)
            else:
                self.lista_pacientes.append(paciente)
                node = self.lista_pacientes.head

                for _ in range(self.prioridad_1):
                    if node is not None and node.value.prioridad == 1:
                        node = node.next

                if node is not None and node.value.prioridad != 1:
                    self.lista_pacientes.other_position(node)

        elif prioridad_paciente == 2 and self.lista_pacientes.size > 0:
            self.prioridad_2 += 1
            
            if self.lista_pacientes.size == 1:
                if self.lista_pacientes.head.value.prioridad != 1:
                    self.lista_pacientes.preppend(paciente)
                else:
                    self.lista_pacientes.append(paciente)
            else:
                self.lista_pacientes.append(paciente)
                node = self.lista_pacientes.head
                prioridad = self.prioridad_1 + self.prioridad_2
                for _ in range(prioridad):
                    if node is not None and (node.value.prioridad == 1 or node.value.prioridad == 2):
                        node = node.next

                if node is not None and node.value.prioridad != 1:
                    self.lista_pacientes.other_position(node) 
        else:
            if paciente.prioridad == 1:
                self.prioridad_1 += 1
            elif paciente.prioridad == 2:
                self.prioridad_2 += 1
            else:
                self.prioridad_3 += 1
            self.lista_pacientes.append(paciente)
        
        self.first = self.lista_pacientes.head
        self.prioridad_first = self.first.value.prioridad


    def atender_paciente(self):
        self.lista_pacientes.show_value(0)
        self.lista_pacientes.delete_head()

    def buscar_paciente(self, nombre):
        paciente: Paciente
        paciente = self.lista_pacientes.head

        for _ in range(self.lista_pacientes.size):
            if paciente.value.nombre == nombre:
                return paciente
            paciente = paciente.next

    def buscar_posicion_paciente_nombre(self, nombre):
        paciente = self.lista_pacientes.head 

        for i in range(self.lista_pacientes.size):
            if paciente.value.nombre == nombre:
                return i
            paciente = paciente.next
        return False
    
    def buscar_posicion_paciente_prioridad(self, prioridad):
        paciente = self.lista_pacientes.head 

        for i in range(self.lista_pacientes.size):
            if paciente.value.prioridad == prioridad:
                return i
            paciente = paciente.next
        return False
    
    def actualizar_prioridad(self, nombre, nueva_prioridad):
        paciente_nodo = self.buscar_paciente(nombre)
    
        if paciente_nodo is not None:
            paciente = paciente_nodo.value 
            if nueva_prioridad != 1:
                paciente.prioridad = nueva_prioridad

                if paciente.prioridad == 2 and nueva_prioridad == 3:
                    self.prioridad_2 -= 1
                    self.prioridad_3 += 1
                else:
                    self.prioridad_3 -= 1
                    self.prioridad_2 += 1
            else:

                if paciente.prioridad == 2:
                    self.prioridad_2 -= 1
                else:
                    self.prioridad_3 -= 1
                paciente.prioridad = nueva_prioridad
                index = self.buscar_posicion_paciente_nombre(nombre)
                paciente = self.lista_pacientes.delete(index)
                self.agregar_paciente(paciente)

    
    def atender_grupo(self):
        if self.prioridad_1 > self.prioridad_2 and self.prioridad_1 > self.prioridad_3:
            node = self.lista_pacientes.head
            for _ in range(self.prioridad_1):
                    self.lista_pacientes.show_value(0)
                    self.lista_pacientes.delete_head()
                    self.prioridad_1 -= 1
            node = node.next
        
        elif self.prioridad_2 > self.prioridad_1 and self.prioridad_2 > self.prioridad_3:
            node = self.lista_pacientes.head
            
            for _ in range(self.lista_pacientes.size):
            
                if node.value.prioridad == 2:
                    index = self.buscar_posicion_paciente_prioridad(2)
                    self.lista_pacientes.show_value(index)
                    self.lista_pacientes.delete(index)
                    self.prioridad_2 -= 1
                node = node.next
        
        elif self.prioridad_3 > self.prioridad_1 and self.prioridad_3 > self.prioridad_2:
            node = self.lista_pacientes.head
            
            for _ in range(self.lista_pacientes.size):
            
                if node.value.prioridad == 3:
                    index = self.buscar_posicion_paciente_prioridad(3)
                    self.lista_pacientes.show_value(index)
                    self.lista_pacientes.delete(index)
                    self.prioridad_3 -= 1
                node = node.next
        
        elif self.prioridad_1 == self.prioridad_2 and self.prioridad_1 > self.prioridad_3:
            node = self.lista_pacientes.head
            for _ in range(self.prioridad_1):
                    self.lista_pacientes.show_value(0)
                    self.lista_pacientes.delete_head()
                    self.prioridad_1 -= 1
            node = node.next
        
    
        elif self.prioridad_2 == self.prioridad_3 and self.prioridad_2 > self.prioridad_1:
            node = self.lista_pacientes.head
            for _ in range(self.lista_pacientes.size):
            
                if node.value.prioridad == 2:
                    index = self.buscar_posicion_paciente_prioridad(2)
                    self.lista_pacientes.show_value(index)
                    self.lista_pacientes.delete(index)
                    self.prioridad_2 -= 1
                node = node.next
        
        elif self.prioridad_3 == self.prioridad_1 and self.prioridad_3 > self.prioridad_2:
            node = self.lista_pacientes.head
            for _ in range(self.prioridad_1):
                    self.lista_pacientes.show_value(0)
                    self.lista_pacientes.delete_head()
                    self.prioridad_1 -= 1
            node = node.next

    def mostrar_cola(self):
        self.lista_pacientes.traverse()

    def mostrar_contadores(self):
        print(self.prioridad_1)
        print(self.prioridad_2)
        print(self.prioridad_3)
    



# IMPLEMENTACION

ll = DobleLinkedList()
cola = cola_de_prioridad(ll)
Paciente_1 = Paciente("tres", 66, "x", 2)
Paciente_2 = Paciente("uno", 11, "x", 1)
Paciente_3 = Paciente("cuatro", 44, "x", 2)
Paciente_4 = Paciente("dos", 22, "x", 1)
Paciente_5 = Paciente("cinco", 33, "x", 2)
Paciente_6 = Paciente("seis", 55, "x", 3)
Paciente_7 = Paciente("siete", 88, "x", 3)
Paciente_8 = Paciente("ocho", 99, "x", 3)

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
cola.mostrar_contadores()
print("*************")
ll.show_head_and_tail()
print("*************")
cola.atender_grupo()
print("*************")
cola.mostrar_cola()
print("*************")
ll.show_head_and_tail()