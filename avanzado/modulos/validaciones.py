def validar_edad(edad:int,categoria:str):
  if edad < 15:
    input("Tu participante es muy joven para estar registrado en este juego.\nPresiona ENTER para volver.")
    return False
  elif categoria == "Novato" and edad not in range(15,16):
    input("El participante debe tner entre 15 y 16 años para participar en esta categoría.\nPresiona ENTER para volver.")
    return False
  elif categoria == "Intermedio" and edad not in range(17,20):
    input("El participante debería tener entre 17 y 20 años de edad para estar en esta categoría.\nPresiona ENTER para volver.")
    return False
  elif categoria not in ["Novato", "Intermedio", "Avanzado"]:
    input("La categoría ingresada no parece ser válida.\nPresiona ENTER para volver")
    return False

