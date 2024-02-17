import sys
from os import system

from tabulate import tabulate
from .participantes import agregar_participante, registar_fecha
from .reportes import menu_reportes

def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def menu_principal():
  borrar_pantalla()
  titulo = """
  +++++++++++++++++++++++++++++
  +  TORNEO DE TENIS DE MESA  +
  +++++++++++++++++++++++++++++
  """
  print(titulo)
  menu = [["1.", "Agregar participante"], ["2.", "Registrar fecha"], ["3.","Reportes"], ["4.","Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    agregar_participante()
    menu_principal()
  elif opcion == "2":
    registar_fecha()
    menu_principal()
  elif opcion == "3":
    menu_reportes()
    menu_principal()
  elif opcion == "4":
    sys.exit("Hasta luego!")
  else:
    menu_principal()