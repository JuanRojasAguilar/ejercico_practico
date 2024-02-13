from . import menus
from . import estudiantes

def calcular_imc():
  while True:
    estudiante = estudiantes.buscar_estudiante()
    peso = float(input("Por favor, agrega tu peso actual en kilogramos: "))
    altura = float(input("Por favor, ingresa tu altura actual en metros: "))
    input("Se está calculando el peso... Dale ENTER para continuar")
    imc = peso/(pow(altura, 2))
    categoria = ''
    if imc >= 18.5 and imc <= 24.9:
      categoria = "NORMAL"
    elif imc >= 25 and imc <= 29.9:
      categoria = "SOBREPESO"
    elif imc >= 30 and imc <= 34.9:
      categoria = "OBESIDAD I"
    elif imc >= 35 and imc <= 39.9:
      categoria = "OBESIDAD II"
    elif imc >= 40 and imc < 100:
      categoria = "OBESIDAD III"
    else:
      return print(f"Tu imc parece ser de {imc:.2f}, por favor confirma los datos o visita a un experto de la salud")
    
    estudiante["clasificacion"] = categoria
    print(f"Actualmente tu imc es de {imc:.2f}, eso te pondría en la categoría {categoria}")

    opcion = input("Quieres continuar? S(si) Enter(no)").upper()
    if opcion == "S":
      calcular_imc() 
    else:
      menus.menu_principal() 
  
