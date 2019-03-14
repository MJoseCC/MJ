def Suma(a,b):
     return a + b

def Resta(a,b):
    return a - b

def Multiplicacion(a,b):
    return a * b

def Division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

def Exponencial(a,b):
    return a ** b

num1 = input("Introduce por teclado el primer numero: ")
num2 = input("Introduce por teclado el segundo numero: ")
diccionario = {1:Suma,2:Resta,3:Multiplicacion,4:Division,5:Exponencial}

try:
    for c, d in diccionario.items():
        print(c, ":", d)
    operacion = int(input("Introduce la operacion deseada a realizar con los dos numeros: "))
    resultado = int(diccionario[operacion](int(num1), int(num2)))
    print(resultado)
except:
        print("Esa opcion no es valida")
