numero = int(input("Introduce por teclado un numero: "))

if numero<20:
    print("Es menor que 20: ",numero)
elif numero <40:
    print("El numero esta entre 20 y 39: ",numero)
elif numero<60:
    print("El numero esta entre 40 y 59: ",numero)
elif numero > 60:
    print("El numero es mayor de 60: ",numero)