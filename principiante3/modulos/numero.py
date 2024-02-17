from tabulate import tabulate

lista_numeros = []

def ingresar_numeros():
  try:
    numero = int(input("Por favor, ingresa un número entero positivo: "))
  except ValueError:
    input("El valor ingresado no es válido")
    ingresar_numeros()
  else:
    if numero > 0:
      lista_numeros.append(numero)
      ingresar_numeros()
    elif numero == 0:
      ingresar_numeros()
    else:
     reporte_numeros()

def reporte_numeros():
  pares = 0
  suma_pares = 0
  suma_impares = 0
  menores_10 = 0
  rango_20_50 = 0
  mayor_100 = 0
  for numero in lista_numeros:
    if numero % 2 == 0:
      suma_pares += numero
      pares += 1
    else:
      suma_impares += numero
    if numero < 10:
      menores_10 += 1
    elif numero <= 50 or numero >= 20:
      rango_20_50 += 1
    elif numero > 100:
      mayor_100 += 1

  promedio_pares = suma_pares / len(lista_numeros)
  promedio_impares = suma_impares / len(lista_numeros)

  dict_numeros = {
    "total_numeros": len(lista_numeros),
    "total_pares": pares,
    "promedio_pares": "{:.2f}".format(promedio_pares),
    "promedio_impares": "{:.2f}".format(promedio_impares),
    "numeros_menores_a_10": menores_10,
    "numeros_entre_20_y_50": rango_20_50,
    "numeros_mayores_100": mayor_100
  }
  print(tabulate([dict_numeros], headers="keys", tablefmt="grid"))
