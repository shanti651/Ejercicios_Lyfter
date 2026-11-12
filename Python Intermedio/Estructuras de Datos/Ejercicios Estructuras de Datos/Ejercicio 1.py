class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Stack:
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nodo = Nodo(dato)
        nodo.siguiente = self.tope
        self.tope = nodo

    def pop(self):
        if self.tope is None:
            raise IndexError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def imprimir(self):
        actual = self.tope
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente


if __name__ == "__main__":
    pila = Stack()
    pila.push(10)
    pila.push(20)
    pila.push(30)

    pila.imprimir()

    pila.pop()
    print("---")
    pila.imprimir()