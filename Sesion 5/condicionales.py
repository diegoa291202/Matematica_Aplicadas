# EJEMPLO1
edad = int(input("¿Cuantos años tienes?"))
if edad < 0:
     print("No se puede tener una edad negativa")
elif edad>=0 and edad < 18:
    print("Es usted menor de edad")
else:
    print ("Es usted es mayor de edad")

# EJEMPLO 2
numero = int(input("Escriba un número"))
if numero % 2 ==0 and numero % 4 !=0:
    print(f"{numero} es multiplo de dos")
elif numero % 4 == 0:         
    print(f"{numero} es multiplo de cuatro y de dos")
else:
    print(f"{numero} no es multiplo de dos")
