from . import menus
listado_estudiante = []

def agregar_estudiante():
  menus.borrar_pantalla()
  identificacion = input("Por favor, ingresa el número de identificación: ").title()
  nombre = input("Por favor, ingresa el nombre del estudiante: ").title()
  edad = int(input(f"Ingresa la edad de {nombre}: "))
  estudiante = {
    "identificacion": identificacion,
    "nombre": nombre,
    "edad": edad,
    "IMC": 0,
    "clasificacion": ""
  }
  listado_estudiante.append(estudiante)
  option = input(f"Listo, {nombre} ha sido agregado a la base de datos.\n\nQuieres añadir otro estudiante? S(si) N(no)").upper()
  print(listado_estudiante)
  if option == "S":
    agregar_estudiante()
  else:
    menus.menu_principal()

def buscar_estudiante():
  nombre = input("Por favor ingresa el nombre del estudiante a buscar: ").title()
  for estudiante in listado_estudiante:
    if estudiante["nombre"] == nombre or estudiante["identificacion"] == nombre:
      respuesta = estudiante
      break
  return respuesta
