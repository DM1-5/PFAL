import numpy as np

def verificar(vector):
  """Verifica que todos los elementos de un vector sean enteros positivos"""
  if (vector < 0).any() or (vector % 1 != 0).any():
    return False
  return True

class PFAL: 
  def __init__(self):
    self.pizzas = np.array([[5,3,3],[4,6,2],[7,4,2]])
    self.ventas = np.array([1,2,3])
    self.precios = np.array([100,200,300])
    self.inventario = np.array([10,10,10])

# getters and setters
  def getPizzas(self):
    return self.pizzas

  def setPizzas(self, pizzas):
    self.pizzas = pizzas

  def getVentas(self):
    return self.ventas

  def setVentas(self, ventas):
    self.ventas = ventas

  def getPrecios(self):
    return self.precios

  def setPrecios(self, precios):
    self.precios = precios

  def getInventario(self):
    return self.inventario

  def setInventario(self, inventario):
    self.inventario = inventario

# Operaciones
  def total_ventas(self):
    """Calcula el valor total de las ventas"""
    return np.dot(self.ventas, self.precios)

  def ventasTipo(self):
    """Calcula el valor de las ventas por tipo de pizza"""
    return self.ventas * self.precios
    
  def descontar(self, pizza):
    """Descuenta los ingredientes necesarios para la pizza escogida"""
    temp = self.inventario - pizza
    if (verificar(temp)):
      self.inventario = temp
      return 0
    else:
      print("No hay suficiente inventario")
      return -1

  def agregar(self,compras):
    """Agrega ingredientes de la compra al inventario"""
    if (verificar(compras)):
      self.inventario = self.inventario + compras
      return 0
    else: 
      print("No se puede agregar")
      return -1
    
  def ingredientes(self, tipo):
    """Muestra una cadena de texto con los ingredientes necesarios para crear una pizza"""
    return f"Harina: {self.pizzas[tipo][0]}, Queso: {self.pizzas[tipo][1]}, Tomate: {self.pizzas[tipo][2]}"
  
  def strinventario(self):
    """Muestra una cadena de texto con los ingredientes en el inventario"""
    return f"Harina: {self.inventario[0]}, Queso: {self.inventario[1]}, Tomate: {self.inventario[2]}"
  

print("Cargado correctamente")

if __name__ == "__main__":
  app = PFAL()
  print(app.ingredientes(1))
  print(app.strinventario())
  #print(app.total_ventas())
  #print(app.ventasTipo())
  #print(app.inventario)
  app.descontar(np.array([1,2,3]))
  print(app.inventario)
  app.agregar(np.array([0.1,2,3]))
  print(app.inventario)
  #print(app.inventario)
  #print(app.getInventario())
  #app_string = str(app)
  #print(app_string)