import numpy as np
import prettytable as pt
import math

def verificar(vector):
  """Verifica que todos los elementos de un vector sean enteros positivos"""
  if (vector < 0).any() or (vector % 1 != 0).any():
    return False
  return True

class PFAL: 
  def __init__(self):
    self.pizzas = np.array([[5,3,3],
                            [4,6,2],
                            [7,4,2]])
    
    self.ventas = np.array([0,0,0])

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

  def ventas_tipo(self):
    """Calcula el valor de las ventas por tipo de pizza"""
    return self.ventas * self.precios
    
  def fabricar(self, tipo):
    """Fabrica la pizza descontando los ingredientes del inventario."""
    temp = self.inventario - self.pizzas[tipo]
    if (verificar(temp)):
      self.inventario = temp
      self.ventas[tipo] = self.ventas[tipo] + 1
      return 0
    else:
      print("No hay suficiente inventario")
      return -1

  def comprar(self,lista):
    """Agrega ingredientes de la compra al inventario"""
    compras = np.array(lista)
    if (verificar(compras)):
      self.inventario = self.inventario + compras
      return 0
    else: 
      print("No se puede agregar")
      return -1
    
  def pizzas_posibles(self):
    """Retorna el numero de pizzas que se pueden realizar con el inventario actual."""
    result = []
    # Crea una lista con el numero mas pequeño de los ingredientes en el inventario dividido por los ingredientes de cada pizza.
    for i in range(len(self.pizzas)):
      #print(f"Iteracion {i+1}: \n")
      #print(self.inventario / self.pizzas[i])
      result.append(math.floor(min(self.inventario / self.pizzas[i])))
    return result
    

  def str_ingredientes(self, tipo):
    """Muestra una cadena de texto con los ingredientes necesarios para crear una pizza"""
    pretty_table = pt.PrettyTable()
    pretty_table.field_names = ["Harina", "Queso", "Tomate"]
    pretty_table.add_row(self.pizzas[tipo])
    return pretty_table.get_string()
  
  def str_inventario(self):
    """Muestra una cadena de texto con los ingredientes en el inventario"""
    pretty_table = pt.PrettyTable()
    pretty_table.field_names = ["Harina", "Queso", "Tomate"]
    pretty_table.add_row(self.inventario)
    return pretty_table.get_string()
  
  def str_ventas(self):
    """Muestra una cadena de texto con las ventas realizadas"""
    pretty_table = pt.PrettyTable()
    pretty_table.field_names = ["Pizza 1", "Pizza 2", "Pizza 3"]
    pretty_table.add_row(self.ventas)
    return pretty_table.get_string()
  
  def str_ventasTipo(self):
    """Muestra una cadena de texto con las ventas por tipo de pizza"""
    pretty_table = pt.PrettyTable()
    pretty_table.field_names = ["Pizza 1", "Pizza 2", "Pizza 3"]
    pretty_table.add_row(self.ventas_tipo())
    return pretty_table.get_string()
  
  def str_pizzasPosibles(self):
    """Muestra una cadena de texto con las ventas por tipo de pizza"""
    pretty_table = pt.PrettyTable()
    pretty_table.field_names = ["Pizza 1", "Pizza 2", "Pizza 3"]
    pretty_table.add_row(self.pizzas_posibles())
    return pretty_table.get_string()
  

print("Libreria PFAL cargada correctamente")

if __name__ == "__main__":
  print("Hello world!")
  pfal = PFAL()
  print("----------------------Llamado a pizzas posibles----------------------")
  print(pfal.str_pizzasPosibles())