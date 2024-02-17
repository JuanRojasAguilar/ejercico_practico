from tabulate import tabulate

from . import menus as mn
from .validaciones import validar_edad

listado_participantes = []
listado_categoria = {"Novato": [], "Intermedio": [], "Avanzado": []}

def buscar_participante(nombre:str):
  for participante in listado_participantes:
    if participante["nombre"] == nombre:
      return participante

def puntuar(participante1, participante2):
  nombre1 = participante1["nombre"]
  nombre2 = participante2["nombre"]
  puntos_participante1 = int(input(f"Cuántos puntos hizo {nombre1}"))
  puntos_participante2 = int(input(f"Cuántos puntos hizo {nombre2}"))

  participante1["PJ"] += 1
  participante2["PJ"] += 1

  if puntos_participante1 > puntos_participante2:
    participante1["PG"] += 1
    participante1["TP"] += 2
    participante1["PA"] += (puntos_participante1 - puntos_participante2)
    participante2["PP"] += 1
  elif puntos_participante2 > puntos_participante1:
    participante2["PG"] += 1
    participante2["TP"] += 2
    participante2["PA"] += (puntos_participante2 - puntos_participante1)
    participante1["PP"] += 1
  else:
    participante1["TP"] += 1
    participante2["TP"] += 1
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
  try:
    nombre = input("Ingrese el nombre del participante: ").title()
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    categoria = input(f"Ingrese la categoria de {nombre} (Novato, Intermedio, Avanzado): ").capitalize()
    if validar_edad(edad, categoria) == False:
      agregar_participante()
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
      mn.menu_principal()
  except ValueError:
    input("Valor no valido. Presiona ENTER para volver")
    mn.menu_principal()

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
    definir_fecha("Novato")
  elif opcion == "2":
    definir_fecha("Intermedio")
  elif opcion == "3":
    definir_fecha("Avanzado")
  else:
    registar_fecha()

def definir_fecha(categoria:str):
  if len(listado_categoria[categoria]) < 5:
    input("Todavía faltan participantes para iniciar los partidos en esta categoría.\nPresiona ENTER para voler.")
    mn.menu_principal()
  else:
    print(tabulate([listado_categoria[categoria]],tablefmt="grid"))
    participante1 = input("Ingresa el nombre del primer participante: ").title()
    participante2 = input("Ingresa el nombre del segundo participante: ").title()
    atleta1 = buscar_participante(participante1)
    atleta2 = buscar_participante(participante2)
    if atleta1["categoria"] != categoria or atleta2["categoria"] != categoria:
      input("Alguno de tus deportistas no hace parte de la categoría.\nPresiona ENTER para voler.")
      mn.menu_principal()
    puntuar(atleta1, atleta2)
    mn.borrar_pantalla()
    print(tabulate([participante1, participante2], headers="keys",tablefmt="grid"))
    input("Presiona ENTER para volver.")
    mn.menu_principal()

