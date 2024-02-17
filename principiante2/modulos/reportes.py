from . import estudiantes

def total_peso(clasificacion):
  contador = 0
  for estudiante in estudiantes.listado_estudiante:
    if estudiante["clasificacion"] == clasificacion:
      contador += 1

  print(f"Los estudiantes con un con clasificación {clasificacion} son {contador}")
