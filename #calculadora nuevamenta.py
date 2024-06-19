#calculadora nuevamenta
#resta
def resta (a,b):
  resta = a-b
  return (resta)

#divición

def divición (a,b):
    try:
        divición= a/b
    except ZeroDivisionError as o :
        print("no se puede dividir por cero")
    return (divición) 
#Suma
def suma(num1, num2):
    return num1+num2

#Multiplicacion
def multiplicacion(num1,num2):
    return num1*num2

