import sys
from tabulate import tabulate
from .instalaciones import agregar_dependencias, mostrar_mayor_consumo

def menu_principal():
  titulo = """
  +++++++++++++++++++++++++++++++++++++++
  +  CONSUMO DE ELECTRICIDAD DISTRITAL  +
  +++++++++++++++++++++++++++++++++++++++
  """
  print(titulo)
  menu = [["1.","Registrar Dependencia"],["2.","CO2 producido"],["3.","Dependencia que produce mayor CO2"], ["4.", "Salir"]]
  print(tabulate(menu, tablefmt="grid"))
  opcion = input("\n>> ").upper()
  
  if opcion == "1":
    agregar_dependencias()
    menu_principal()
  elif opcion == "2":
    pass
  elif opcion == "3":
    mostrar_mayor_consumo()
    menu_principal()
  elif opcion == "4":
    sys.exit("Hasta la proxima!")
  else:
    menu_principal()