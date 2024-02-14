import sys

from tabulate import tabulate
from os import system
from . import menus

lista_productos = []

def registrar_producto():
  menus.borrar_pantalla()
  titulo = """
  ++++++++++++++++++++++++
  +  REGISTRO PRODUCTOS  +
  ++++++++++++++++++++++++
  """
  print(titulo)
  codigo = input("Ingresa el código del producto: ").title()
  nombre = input("Ingresa el nombre del producto: ").title()
  valor_compra = float(input("Ingresa el valor de compra: "))
  valor_venta = float(input("Ingresa el valor de venta: "))
  stock_actual = int(input("Ingesa el stock actual: "))
  stock_minimo = int(input("Ingresa el stock mínimo del producto: "))
  stock_maximo = int(input("Ingresa el stock máximo del producto: "))
  nombre_proveedor = input("Ingresa el nombre del proveedor: ").title()

  producto = {
    "codigo": codigo,
    "nombre": nombre,
    "valor de compra": valor_compra,
    "valor de venta": valor_venta,
    "stock actual": stock_actual,
    "stock minimo": stock_minimo,
    "stock maximo": stock_maximo,
    "nombre del proveedor": nombre_proveedor
  }

  for item in lista_productos:
    if item["nombre"] == nombre or item["codigo"] == codigo:
      input("Ese producto ya está en la base de datos.\nPresiona ENTER para volver al inicio")
      menus.menu_principal()

  lista_productos.append(producto)
  print(tabulate(lista_productos, headers="keys", tablefmt="grid"))
  input("\nPresiona ENTER para volver al menú principal")
  menus.menu_principal()

def visualizar_productos():
  menus.borrar_pantalla()
  titulo = """
  ++++++++++++++++++++++++++
  +  LISTADO DE PRODUCTOS  +
  ++++++++++++++++++++++++++
  """
  print(titulo)
  print(tabulate(lista_productos, headers="keys", tablefmt="grid"))
  input("Pulsa ENTER para volver")
  menus.menu_principal()

def actualizar_stock():
  menus.borrar_pantalla()
  titulo = """
  +++++++++++++++++++++++++++
  +  ACTUALIZADOR DE STOCK  +
  +++++++++++++++++++++++++++
  """
  print(titulo)

  nombre = input("\nIngresa el producto a editar: ").title()
  resultado = {}
  for producto in lista_productos:
    if producto["nombre"] == nombre or producto["codigo"] == nombre:
      resultado = producto
      break

  print(tabulate([resultado], headers="keys", tablefmt="grid"))
  stock_actual = int(input("Cuánto es el stock actual del producto? "))
  resultado["stock actual"] = stock_actual

  menus.borrar_pantalla()
  print("Ha sido exitoso, revisa la nueva tabla")
  print(tabulate([resultado], headers="keys", tablefmt="grid"))
  input("\nPresiona ENTER para continuar")
  menus.menu_principal()

def productos_criticos():
  menus.borrar_pantalla()
  titulo = """
  +++++++++++++++++++++++++++++++++
  +  PRODUCTOS EN ESTADO CRITICO  +
  +++++++++++++++++++++++++++++++++
  """
  print(titulo)
  productos_criticos = []
  for producto in lista_productos:
    if producto["stock actual"] < producto["stock minimo"]:
      productos_criticos.append(producto)
  print(tabulate(productos_criticos, headers="keys", tablefmt="grid"))
  input("Presiona ENTER para volver")
  menus.menu_principal()

def ganancia_potencial():
  menus.borrar_pantalla()
  titulo = """
  ++++++++++++++++++++++++++++++++++++++
  +  GANANCIA POTENCIAL POR PRODUCTOS  +
  ++++++++++++++++++++++++++++++++++++++
  """
  print(titulo)
  lista_ganancias = []
  for producto in lista_productos:
    ganancia = (producto["valor de venta"] - producto["valor de compra"]) * producto["stock actual"]
    newProducto = {
      "nombre": producto["nombre"],
      "ganancia potencial": ganancia
    }
    lista_ganancias.append(newProducto)
  print(tabulate(lista_ganancias, headers="keys", tablefmt="grid"))
  input("\nPresiona ENTER para volver al menu principal")
  menus.menu_principal()