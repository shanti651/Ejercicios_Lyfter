class Volador:
    def volar(self):
        print("Puedo volar")

class Nadador:
    def nadar(self):
        print("Puedo nadar")


class Pato(Volador, Nadador):
    def hacer_sonido(self):
        print("Cuac cuac")
