class Dulce:
    def __init__(self, tipo, sabor, tamaño, forma, color, textura):
        self.tipo = tipo
        self.sabor = sabor
        self.tamaño = tamaño 
        self.forma = forma
        self.color = color
        self.textura = textura
        
    def mostrar(self):
        print(f"Este dulce es de Tipo: {self.tipo} ,sabor: {self.sabor} ,tamaño: {self.tamaño} ,forma: {self.forma} ,color: {self.color} ,textura: {self.textura} ")
 