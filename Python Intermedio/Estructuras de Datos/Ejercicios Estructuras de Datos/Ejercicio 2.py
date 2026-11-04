class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class Deque:
    def __init__(self):
        self.inicio = None
        self.final = None

    def push_left(self, dato):
        nodo_nuevo = Nodo(dato)

        if self.inicio is None:
            self.inicio = nodo_nuevo
            self.final = nodo_nuevo
        else:
            nodo_nuevo.siguiente = self.inicio
            self.inicio.anterior = nodo_nuevo
            self.inicio = nodo_nuevo

    def push_right(self, dato):
        nodo_nuevo = Nodo(dato)

        if self.final is None:
            self.inicio = nodo_nuevo
            self.final = nodo_nuevo
        else:
            nodo_nuevo.anterior = self.final
            self.final.siguiente = nodo_nuevo
            self.final = nodo_nuevo

    def pop_left(self):
        dato = self.inicio.dato

        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = None

        return dato

    def pop_right(self):
        dato = self.final.dato

        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.final = self.final.anterior
            self.final.siguiente = None

        return dato

    def imprimir(self):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente


# pruebas
dq = Deque()
dq.push_right(10)
dq.push_right(20)
dq.push_left(5)

dq.imprimir()

print("---")

dq.pop_left()
dq.pop_right()
dq.imprimir()