'''
Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''
'''
print('Ejercicio1: Define una función que tome dos números y retorne su suma.')
def sumade(number1,number2):
  num=number1+number2
  print('La suma es',num)

print('ingresa un numero')
number1= int(input())
print('ingresa un numero')
number2= int(input())
sumade(number1,number2)

print('Ejercicio 2: Define una función que tome un número y retorne su factorial.')

def factorial (valor):
  fact=1
  incre=1  
  while incre<=valor:
    fact=fact*incre
    incre = incre + 1
  print('el factorial es', fact)
  
print('ingresa un numero para calcular su factorial')
valor= int(input())
factorial(valor)

print('Ejercicio 3: Define una función que tome un número y determine si es primo.')

def primo (valor2):
  for n in range(2, valor2):
    if valor2%n==0:
      print('no es numero primo', n,'es divisor')
      return False
    print('es primo')
    return True
valor2= int(input('introduce un valor para calcular si es primo'))
primo(valor2)
'''

'''print("Ejercicio 4: Define una función que reciba una lista de números y retorne la suma de ellos.")
lista=[]
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
#print(lista)
def suma_val (lista):
  res=sum(lista)
  print(res)
suma_val(lista)'''

print('Ejercicio 5: Define una función que reciba una cadena de texto y retorne la cadena en reversa')

def inv(text):
  n = len(text)
  inverso =""
  for n in text:
    inverso = n+inverso
  print("Texto invertido:", inverso)

text=str(input("Introducir un texto:    "))
print("texto original:", text)
inv(text)