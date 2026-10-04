class Separador:
  def _init_(self,nombre, tamaño, color, tipos, forma):
   self.nombre = nombre
   self.tamaño = tamaño
   self.color = color
   self.tipos = tipos
   self.forma = forma
 
 
  def conocer(self):
    print(f"este separador , es {self.nombre} y tengo {self.tamaño} tambien tengo {self.color}hay {self.tipos} y {self.forma}")
