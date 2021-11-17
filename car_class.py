class car:
    def __init__(self, marca, modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.comustible = combustible
        self.cilindrada = cilindrada
    def move_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
    def move_incr(self, x, y):
        self.pos_x = += x
        self.pos_y = += y
    def get_pos(selfself):
        return self.pos_x, self.pos_y
