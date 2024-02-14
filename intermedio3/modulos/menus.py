from os import system
import sys

from tabulate import tabulate
from modulos.productos import registrar_producto, visualizar_productos, actualizar_stock, productos_criticos, ganancia_potencial

def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def menu_principal():
  borrar_pantalla()
  titulo = """
    ++++++++++++++++++++++++++++++++
    +  ADMINISTRADOR DE PRODUCTOS  +
    ++++++++++++++++++++++++++++++++
  """
  print(titulo)
  menu = [["1.","Registrar producto"],["2.","Visualizar lista de productos"], ["3.", "Actualizar Stock"],["4.", "Productos en estado critico"], ["5.", "Ganancia Potencial"], ["6.", "Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  option = input("\n>> ")

  if option == "1":
    registrar_producto()
  elif option == "2":
    visualizar_productos()
  elif option == "3":
    actualizar_stock()
  elif option == "4":
    productos_criticos()
  elif option == "5":
    ganancia_potencial()
  elif option == "6":
    sys.exit("Hasta luego!")
  else:
    menu_principal()