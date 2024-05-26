# Proyecto final algebra lineal

Este proyecto consiste en la abstraccion de un negocio de pizzas mediante algebra lineal

Tendrá las siguientes estructuras de datos:

## Matriz Pizzas

Cada una de las componentes del vector **pizza[i]** son la cantidad de ingredientes necesarios para crearla.

## Vectores

### Ventas

Representa el numero de unidades vendidas de cada tipo de pizza.

### Precios

Representa el valor unitario de cada tipo pizza.

### Inventario

Representa la cantidad de ingredientes disponibles.

### Compras

Representa la cantidad de ingredientes comprados.

```python

import numpy as np

pizzas = np.array([[5,3,3],[4,6,2],[7,4,2]])

ventas = np.array([1,2,3])

precios = np.array([100,200,300])

inventario = np.array([10,10,10])

compras = np.array([1,2,3])

```

## Operaciones de algebra lineal y su utilidad

### Suma

Suma del vector **compras** al vector **inventario**.

``` python

#Aumentar el inventario con las compras
nInventario = inventario + compras
print(f"Inventario+ (numpy):{nInventario} ")

def aumentar(inventario, compras):
    # ciclo iterando el vector desde el indice 
    resultado = []
    for i in range(len(ventas)):
        resultado.append(inventario[i] + compras[i])
    return resultado

iInventario = aumentar(inventario, compras)
print(f"Inventario+ (ciclo): {iInventario}")

```

### Resta

Resta del vector **inventario** al vector **pizza[i]** pedida.

``` python

# Descontar las pizzas vendidas del inventario
nDescuento = inventario - pizzas[1]
print(f"Inventario- (numpy): {nDescuento} ")

def descontar(inventario, pizza):
    # ciclo iterando el vector desde el indice 
    resultado = []
    for i in range(len(ventas)):
        resultado.append(inventario[i] - pizza[i])
    return resultado

iDescuento = descontar(inventario, pizzas[1])
print(f"Inventario- (ciclo): {iDescuento}")

```

### Producto punto

Producto punto entre el vector **precio** y vector **ventas** para el calculo de las ganancias totales.

``` python

# Calcula el total de ventas
total_ventas = np.dot(ventas,precios)
print(f"Total de ventas (numpy): {total_ventas}")

def total_ventas(ventas, precios):
    # ciclo iterando el vector desde el indice 
    total = 0
    for i in range(len(ventas)):
        total += ventas[i] * precios[i]
    return total

total_ventas = total_ventas(ventas, precios)

print(f"Total ventas (ciclo): {total_ventas}")

```

### Multiplicacion

Multiplicacion componente a componente entre el vector **precio** y el vector **ventas** para el calculo de las ganancias por cada tipo de pizza.

``` python

#Calcula la cantidad de pizzas vendidas de cada tipo 
nTotal_pizza = ventas * precios
print(f"Ventas por pizza (numpy): {nTotal_pizza} ")

def ventas_tipo(ventas, precios):
    # ciclo iterando el vector desde el indice 
    resultado = []
    for i in range(len(ventas)):
        resultado.append(ventas[i] * precios[i])
    return resultado

iTotal_pizza = ventas_tipo(ventas, precios)
print(f"Total ventas (ciclo): {iTotal_pizza}")

```

### Resolucion de sistemas

A unas ganancias obtenidas calcular la cantidad de pizzas y sus tipos que se pueden realizar.
