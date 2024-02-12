listado_estudiante = []

def agregar_estudiante():
  while True:
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
    option = input(f"Listo, {nombre} ha sido agregado a la base de datos.\n\nQuieres añadir otro estudiante? S(si) N(no)")

    if option == "S":
      pass
    else:
      break

def buscar_estudiante(nombre:str):
  for estudiante in listado_estudiante:
    if estudiante["nombre"].title() == nombre:
      return estudiante
    elif estudiante["identificacion"].title() == nombre:
      return estudiante
    else:
      pass   
  
