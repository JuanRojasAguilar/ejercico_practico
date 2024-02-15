from tabulate import tabulate

from . import menus as mn

listado_participantes = []
listado_categoria = {"Novato": [], "Intermedio": [], "Avanzado": []}

def buscar_participante(nombre:str):
  for participante in listado_participantes:
    if participante["nombre"] == nombre:
      return participante

def agregar_categoria(participante:dict):
  nombre = participante["nombre"]
  categoria = participante["categoria"]

  if categoria == "Novato": 
    listado_categoria["Novato"].append(nombre)
  elif categoria == "Intermedio":
    listado_categoria["Intermedio"].append(nombre)
  elif categoria == "Avanzado":
    listado_categoria["Avanzado"].append(nombre)

def agregar_participante():
  mn.borrar_pantalla()
  titulo = """
  ++++++++++++++++++++++++++++++++++++
  +  SISTEMA REGISTRO PARTICIPANTES  +
  ++++++++++++++++++++++++++++++++++
  """
  print(titulo)

  while True:
    nombre = input("Ingrese el nombre del participante: ").title()
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    categoria = input(f"Ingrese la categoria de {nombre} (Novato, Intermedio, Avanzado): ").capitalize()
    if categoria == "Novato" and edad not in range(15,16):
      print("Ilegalísimo")
      break
    nuevo_participante = {
      "nombre": nombre,
      "edad": edad,
      "categoria": categoria,
      "puntuacion": {
        "PJ": 0,
        "PG": 0,
        "PP": 0,
        "PA": 0,
        "TP": 0
      }
    }
    listado_participantes.append(nuevo_participante)
    agregar_categoria(nuevo_participante) 

    print(f"{nombre} ha sido registrado/a correctamente, quieres ingresar otro participante? S(si) Enter(no)")
    opcion = input("\n>> ").upper()
    if opcion == "S":
      agregar_participante()
    else:
      break

def registar_fecha():
  mn.borrar_pantalla()
  titulo = """
  +++++++++++++++++++++++++++++++++++
  +  REGISTRO DE FECHAS DEL TORNEO  +
  +++++++++++++++++++++++++++++++++++
  """
  print(titulo)
  print(tabulate([["1.", "Novato"], ["2.","Intermedio"], ["3.","Avanzado"]], tablefmt="grid"))
  opcion = input("\n>> ")
  if opcion == "1":
    fecha_notavos()
  elif opcion == "2":
    fecha_intermedio()
  elif opcion == "3":
    fecha_avanzado()
  else:
    registar_fecha()

def fecha_notavos():
  print(tabulate(listado_categoria["Novato"],tablefmt="grid"))
  input()

def fecha_intermedio():
  print(tabulate(listado_categoria["Intermedio"],tablefmt="grid"))
  input()

def fecha_avanzado():
  print(tabulate(listado_categoria["Avanzado"],tablefmt="grid"))
  input()

def puntuar(participante1, participante2):
  