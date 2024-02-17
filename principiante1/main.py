lista = []
def preguntar_numero():
  numero = int(input("Ingrese un número entero positivo: "))
  if numero > 0:
    lista.append(numero)
  else:
    print("Por favor ingresa un número válido.")
    preguntar_numero()


if __name__ == "__main__":
  def main():
    contador = 0
    for _ in range(3):
        preguntar_numero()
    for numero in lista:
        contador += numero
    print(f"La suma de tus números son {contador}")
    


  main()
