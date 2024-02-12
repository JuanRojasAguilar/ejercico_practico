import sys
import os
from tabulate import tabulate

from . import calcular_imc as imc
from . import estudiantes

def borrar_pantalla():
  if sys.plataform.startswith("linux"):
    os.system("clear")
  else:
    os.system("cls")

def menu_principal():
  borrar_pantalla()
  print("Bienvenido!")
  print("\n1.Agregar estudiantes\n2.Calcular IMC\n3.Salir")

  option = input(">> ")
  if option == "1":
    borrar_pantalla()
    estudiantes.agregar_estudiante()
  elif option == "2":
    borrar_pantalla()
    imc.calcular_imc()
  elif option == "3":
    borrar_pantalla()
    menu_reportes()
  else:
    sys.exit()

def menu_reportes():
  tabla_menu = [["A", "Cuantos estudiantes se encuentran en el peso ideal"], ["B.", "Cuantos estudiantes se encuentran en OBESIDAD GRADO I"], ["C.", "Cuantos estudiantes se encuentran en OBESIDAD GRADO II"],["D.","Cuantos estudiantes se encuentran en OBESIDAD GRADO III"], ["E.","Cuantos estudiantes se encuentran en SOBREPESO"], ["F.","Salir"]]
  print(tabulate(tabla_menu,tablefmt="grid"))

  option = input(">> ").upper()
