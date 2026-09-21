class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nodo_nuevo = Nodo(dato)

        if self.raiz is None:
            self.raiz = nodo_nuevo
        else:
            self.insertar_ayuda(self.raiz, nodo_nuevo)

    def insertar_ayuda(self, nodo_actual, nodo_nuevo):
        if nodo_nuevo.dato < nodo_actual.dato:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nodo_nuevo
            else:
                self.insertar_ayuda(nodo_actual.izquierda, nodo_nuevo)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nodo_nuevo
            else:
                self.insertar_ayuda(nodo_actual.derecha, nodo_nuevo)

    def imprimir(self):
        self.imprimir_ayuda(self.raiz)

    def imprimir_ayuda(self, nodo_actual):
        if nodo_actual is not None:
            self.imprimir_ayuda(nodo_actual.izquierda)
            print(nodo_actual.dato)
            self.imprimir_ayuda(nodo_actual.derecha)


# pruebas
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)

arbol.imprimir()