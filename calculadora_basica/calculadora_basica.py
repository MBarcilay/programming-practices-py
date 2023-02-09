operacion = input("""¿Qué operación deseas realizar? 
      \n 1. Suma 
      \n 2. Resta 
      \n 3. Multiplicación 
      \n 4. División
      \n 5. Salir 
      \n""")

numero1 = input("Primer número: ")

numero2 = input("Segundo número: ")

if operacion == "1":
    print("El resultado de la suma es: ", int(numero1) + int(numero2))

elif operacion == "2":
    print("El resultado de la suma es: ", int(numero1) - int(numero2))
elif operacion == "3":
    print("El resultado de la suma es: ", int(numero1) * int(numero2))
elif operacion == "4":
    print("El resultado de la suma es: ", int(numero1) / int(numero2))
elif operacion == "5":
    print("Adios")
else:
    print("Operación no válida")
