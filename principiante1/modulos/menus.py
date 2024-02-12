import sys
from . import calcular_imc as imc
from . import estudiantes

def menu_principal():
  print("Bienvenido!")
  print("\n1.Agregar estudiantes\n2.Calcular IMC\n3.Salir")

  option = input(">> ")
  if option == "1":
    estudiantes.agregar_estudiante()
  elif option == "2":
    imc.calcular_imc()
  else:
    sys.exit()