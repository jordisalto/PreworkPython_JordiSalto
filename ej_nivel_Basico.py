
print("1: Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.")

def verif_par (num):
  if num %2==0:
    print("el numero es par")
  else:
    print("el número es impar")

num=int(input("ingresar un número:    "))
verif_par(num)

print("2: Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.")
def factorial (num):
  resultado=1
  for i in range(1, num+1):
    resultado *=i
  return resultado

num =int(input("ingrese un valor:   "))
factorial (num)
print(" el factorial de ",num,  "es", factorial(num))

print("3: Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos")
def contar (cadena):
  return len(str(cadena))

cadena=int(input("introduce un valor:  "))
contar(cadena)
print(cadena, "tiene", contar(cadena), "digitos")

print("4: Dada una lista de números, crea una función que devuelva el número máximo de la lista.")

def encontrar_maximo(valores): 
  maximo = valores[0] 
  for numero in range(1, len(valores)):
    if valores[numero] > maximo:
      maximo= lista[numero]
  return maximo
lista = [5, 12, 3, 8, 9] 
print("El número máximo es:", encontrar_maximo(lista))


print("5: Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.")
def sumar_digitos(numero):
  suma=0
  while numero>0:
    suma = suma + numero%10 
    numero = numero//10
  return suma
  
num=int(input("ingresa un numero: "))
print("La suma de los dígitos es", sumar_digitos(num))


print("6: Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento la función, y devuelva el MCM.")

def mcm(a,b):
  if a == 0 or b == 0: 
    return 0 
  else: 
    maximo = max(a, b) 
    while True: 
      if (maximo % a == 0) and (maximo % b == 0): 
        return maximo
      maximo += 1 
      
num1 = int(input("Ingresar primer número: ")) 
num2 = int(input("Ingresar segundo número: ")) 
print("El MCM es:", mcm(num1, num2))


print("7: Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo")
def area_triangulo (base, altura):
   return (base * altura)/2

altura=float(input("indicar altura del triangulo: "))
base=float(input("Indicar base del triangulo: "))
print("El área del triangulo es:", area_triangulo(base, altura))


print("8: Crea una función que, dado un número, verifique si un número es positivo,negativo o cero.")
def comprobar_signo(num):
  if num>0: 
    return "positivo"
  elif num<0: 
    return "negativo"
  else:
    return "es cero"
  
num=float(input("intertar valor a comprobar: "))
print("el valor introducido",num, "es", comprobar_signo(num))


print("9:Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.")
def contar_letras(palabra):
  contador=0
  for letra in palabra:
    if letra.isalpha():
      contador +=1
  return contador
palabra=input("Escribir palabra: ")
print("la cantidad de letras de la palabra ", palabra, "es", contar_letras(palabra))


print("10:Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto. ")
def valor_absoluto(lista):
  for i in range(len(lista)):
    lista[i]=abs(lista[i])
  return lista

numeros=list([(-5), -6, -20, -9])
print(numeros)
print("el valor aboluto de los numeros es: ", valor_absoluto(numeros))


print("11: Crea una función que, dado un número, verifique si un número es primo.")
def verificar_primo(num):
  if num<=1:
    return False
  for i in range(2,num):
    if num % i ==0:
      return False
  return True
  
num=int(input("Introducir numero: "))
if verificar_primo(num):
  print("Es primo")
else:
  print("no es primo")

print("12:Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números. ")
#aplicando el método de euclides
def mcd(n1, n2):
  while n2:
    n1, n2 = n2, n1%n2
  return n1
n1=int(input("Introduce perimer numero"))
n2=int(input("introduce segundo numero"))
print("el MCD de",n1, "y", n2, "es: ", mcd(n1,n2))
