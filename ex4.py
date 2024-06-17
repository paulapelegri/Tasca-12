class frutas():
    def __init__(self, nombre, color, forma):
        self.nombre=nombre
        self.color=color
        self.forma=forma
    def soy_nombre(self):
        print("Soy una {}".format(self.nombre))
    def soy_color (self):
        print("Soy de color {}".format(self.color))
    def soy_forma(self):
        print("Soy {}".format(self.forma))

class Uva(frutas):
    def __init__(self, nombre, color, forma):
        super().__init__(nombre, color, forma)

class Sandia(frutas):
    def __init__(self, nombre, color, forma):
        super().__init__(nombre, color, forma)

class Ciruela(frutas):
    def __init__(self, nombre, color, forma):
        super().__init__(nombre, color, forma)

#PP


def pex4():
    a=[Uva("uva", "verde", "redonda"), Sandia("sandia", "verde", "ovalada"), Ciruela("ciruela","morado", "circular")]
    for e in a:
        e.soy_nombre()
        e.soy_color()
        e.soy_forma()