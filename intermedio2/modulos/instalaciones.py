import sys
from os import system
from tabulate import tabulate

listado_instalaciones = [
  {
    "instalacion": "Alcaldia",
    "dependencias": [],
    "valor kilovatios/hora": 1500,
  },
  {
    "instalacion": "Biblioteca",
    "dependencias": [],
    "valor kilovatios/hora": 3000
  },
  {
    "instalacion": "Universidad",
    "dependencias": [],
    "valor kilovatios/hora": 800
  },
  {
    "instalacion": "Planta energetica",
    "dependencias": [],
    "valor kilovatios/hora": 500
  },
  {
    "instalacion": "Bienestar Infantil",
    "dependencias": [],
    "valor kilovatios/hora": 2300
  }
]

dependencia_mayor_consumo = {"nombre": "", "consumo": 0}

def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def buscar_instalacion():
  nombre = input("Por favor, ingrese el nombre de la instalación: ").title()
  for instalacion in listado_instalaciones:
    if instalacion["instalacion"] == nombre:
      respuesta = instalacion
      break
  return respuesta

def agregar_dependencias():
  borrar_pantalla()
  titulo = """
  ++++++++++++++++++++++++++
  +  AGREGAR DEPENDENCIAS  +
  ++++++++++++++++++++++++++
  """
  print(titulo)
  print(tabulate(listado_instalaciones,headers="keys", tablefmt="grid"))
  instalacion = buscar_instalacion()
  nombre = input("Ingrese el nombre de la dependencia a agregar: ").title()
  potencia = float(input("Ingrese la potencia del dispositivo: "))
  uso = float(input("Ingrese un estimado semanal de horas uso del dispositivo: "))
  dependencia = {
    "nombre": nombre,
    "potencia": potencia,
    "horas": uso
  }
  instalacion["dependencias"].append(dependencia)
  actualizar_consumo()

  input(f"{nombre} se ha agregado con éxito.\nPresione ENTER para volver")

def actualizar_consumo():
  for instalacion in listado_instalaciones:
    for dependencia in instalacion["dependencias"]:
      consumo = (dependencia["potencia"] * dependencia["horas"])/100
      dependencia.update({"consumo": consumo})
      if consumo > dependencia_mayor_consumo["consumo"]:
        dependencia_mayor_consumo["nombre"] = dependencia["nombre"]
        dependencia_mayor_consumo["consumo"] = consumo

def mostrar_mayor_consumo():
  borrar_pantalla()
  print(tabulate([dependencia_mayor_consumo], headers="keys", tablefmt="grid"))
  input("\nPresiona ENTER para volver")